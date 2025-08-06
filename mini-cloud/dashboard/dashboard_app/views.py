import os
import yaml
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Path to users.json
USERS_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'users.json')

def _read_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump([], f)
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def _write_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def dashboard_view(request):
    tools = []
    tools_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools')

    for filename in os.listdir(tools_dir):
        if filename.endswith('-compose.yml'):
            with open(os.path.join(tools_dir, filename), 'r') as f:
                try:
                    compose_data = yaml.safe_load(f)
                    for service_name, service_data in compose_data.get('services', {}).items():
                        labels = service_data.get('labels', {})
                        if isinstance(labels, list):
                            labels = dict(item.split('=') for item in labels)

                        if 'mini-cloud.tool.name' in labels:
                            tools.append({
                                'name': labels.get('mini-cloud.tool.name'),
                                'description': labels.get('mini-cloud.tool.description'),
                                'category': labels.get('mini-cloud.tool.category'),
                                'port': labels.get('mini-cloud.tool.port'),
                            })
                except yaml.YAMLError as e:
                    print(f"Error parsing {filename}: {e}")

    return render(request, "index.html", {"tools": tools})

def account_view(request):
    return render(request, "account.html")

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')

            users = _read_users()
            if any(u['email'] == email for u in users):
                return JsonResponse({'success': False, 'message': 'User with this email already exists.'})

            users.append({'username': username, 'email': email, 'password': password})
            _write_users(users)
            return JsonResponse({'success': True, 'message': 'Registration successful.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            users = _read_users()
            user = next((u for u in users if u['email'] == email and u['password'] == password), None)

            if user:
                return JsonResponse({'success': True, 'message': 'Login successful.', 'user': user['username']})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid email or password.'})
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def get_users(request):
    if request.method == 'GET':
        users = _read_users()
        # Do not send passwords to the frontend
        safe_users = [{'username': u['username'], 'email': u['email']} for u in users]
        return JsonResponse(safe_users, safe=False)
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)
