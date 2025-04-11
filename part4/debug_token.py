import jwt
import sys
from datetime import datetime

token = sys.argv[1] if len(sys.argv) > 1 else None

if not token:
    print("Veuillez fournir un token JWT en argument")
    sys.exit(1)

if token.startswith('Bearer '):
    token = token[7:]

try:

    decoded = jwt.decode(token, options={"verify_signature": False})
    print("\nToken décodé avec succès!")

    if 'sub' in decoded:
        print(f"Subject (identité): {decoded['sub']} (type: {type(decoded['sub']).__name__})")
        
        if isinstance(decoded['sub'], dict):
            print(f"  ID: {decoded['sub'].get('id')}")
            print(f"  Admin: {decoded['sub'].get('is_admin')}")
    
    if 'exp' in decoded:
        exp_time = datetime.fromtimestamp(decoded['exp'])
        print(f"Expiration: {exp_time}")

    print("\nClaims supplémentaires:")
    for key, value in decoded.items():
        if key != 'sub':
            print(f"  {key}: {value}")
            
except Exception as e:
    print(f"Erreur lors du décodage du token: {e}")
    import traceback
    traceback.print_exc()