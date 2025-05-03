from app import create_app, db
from app.models import Utilisateur

def create_test_user():
    app = create_app()
    with app.app_context():
        # Vérifier si l'utilisateur test existe déjà
        test_user = Utilisateur.query.filter_by(email='test@test.com').first()
        
        if test_user:
            print(f"L'utilisateur test existe déjà: {test_user.email} (username: {test_user.nom_utilisateur})")
            # Réinitialiser le mot de passe pour être sûr
            test_user.definir_mot_de_passe('test')
            db.session.commit()
            print("Mot de passe réinitialisé à 'test'")
        else:
            # Créer l'utilisateur test
            new_user = Utilisateur(
                nom_utilisateur='test',
                email='test@test.com'
            )
            new_user.definir_mot_de_passe('test')
            db.session.add(new_user)
            db.session.commit()
            print(f"Nouvel utilisateur test créé: {new_user.email} (username: {new_user.nom_utilisateur})")
        
        # Afficher tous les utilisateurs
        print("\nListe de tous les utilisateurs:")
        users = Utilisateur.query.all()
        for user in users:
            print(f"- {user.email} (username: {user.nom_utilisateur})")

if __name__ == '__main__':
    create_test_user()
