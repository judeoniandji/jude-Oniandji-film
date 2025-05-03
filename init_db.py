from app import create_app, db
from app.models import Utilisateur, Media
from datetime import datetime

def init_database():
    """Initialise la base de données avec un utilisateur test et des médias"""
    app = create_app()
    with app.app_context():
        # Créer un utilisateur test s'il n'existe pas déjà
        if not Utilisateur.query.filter_by(email='test@test.com').first():
            utilisateur = Utilisateur(
                nom_utilisateur='test',
                email='test@test.com'
            )
            utilisateur.definir_mot_de_passe('test')
            db.session.add(utilisateur)
            db.session.commit()
            print("Utilisateur test créé avec succès !")
        else:
            utilisateur = Utilisateur.query.filter_by(email='test@test.com').first()
            print("Utilisateur test existe déjà.")

        # Liste de films à ajouter
        films = [
            {
                'titre': 'Inception',
                'type': 'film',
                'genre': 'Science-fiction',
                'note': 4.5,
                'commentaire': 'Un chef-d\'œuvre du cinéma moderne',
                'coup_de_coeur': True,
                'annee': 2010,
                'duree': '2h28'
            },
            {
                'titre': 'Le Parrain',
                'type': 'film',
                'genre': 'Drame',
                'note': 5.0,
                'commentaire': 'Un classique incontournable',
                'coup_de_coeur': True,
                'annee': 1972,
                'duree': '2h55'
            },
            {
                'titre': 'Pulp Fiction',
                'type': 'film',
                'genre': 'Crime',
                'note': 4.8,
                'commentaire': 'Un film culte de Tarantino',
                'coup_de_coeur': True,
                'annee': 1994,
                'duree': '2h34'
            },
            {
                'titre': 'Le Seigneur des Anneaux: La Communauté de l\'Anneau',
                'type': 'film',
                'genre': 'Fantaisie',
                'note': 4.7,
                'commentaire': 'Une épopée fantastique extraordinaire',
                'coup_de_coeur': True,
                'annee': 2001,
                'duree': '2h58'
            },
            {
                'titre': 'The Dark Knight',
                'type': 'film',
                'genre': 'Action',
                'note': 4.9,
                'commentaire': 'Le meilleur film de super-héros',
                'coup_de_coeur': True,
                'annee': 2008,
                'duree': '2h32'
            }
        ]

        # Liste de séries à ajouter
        series = [
            {
                'titre': 'Breaking Bad',
                'type': 'serie',
                'genre': 'Drame',
                'note': 5.0,
                'commentaire': 'Une des meilleures séries jamais créées',
                'coup_de_coeur': True,
                'annee': 2008,
                'nombre_saisons': 5,
                'nombre_episodes': 62
            },
            {
                'titre': 'Game of Thrones',
                'type': 'serie',
                'genre': 'Fantaisie',
                'note': 4.7,
                'commentaire': 'Une série épique avec une fin controversée',
                'coup_de_coeur': False,
                'annee': 2011,
                'nombre_saisons': 8,
                'nombre_episodes': 73
            },
            {
                'titre': 'Stranger Things',
                'type': 'serie',
                'genre': 'Science-fiction',
                'note': 4.5,
                'commentaire': 'Une série nostalgique des années 80',
                'coup_de_coeur': True,
                'annee': 2016,
                'nombre_saisons': 4,
                'nombre_episodes': 34
            },
            {
                'titre': 'The Office',
                'type': 'serie',
                'genre': 'Comédie',
                'note': 4.8,
                'commentaire': 'La meilleure comédie de bureau',
                'coup_de_coeur': True,
                'annee': 2005,
                'nombre_saisons': 9,
                'nombre_episodes': 201
            },
            {
                'titre': 'Black Mirror',
                'type': 'serie',
                'genre': 'Science-fiction',
                'note': 4.6,
                'commentaire': 'Une série dystopique sur la technologie',
                'coup_de_coeur': False,
                'annee': 2011,
                'nombre_saisons': 5,
                'nombre_episodes': 22
            }
        ]

        # Ajouter les films
        for film_data in films:
            if not Media.query.filter_by(titre=film_data['titre'], utilisateur_id=utilisateur.id).first():
                film = Media(utilisateur_id=utilisateur.id, **film_data)
                db.session.add(film)
                print(f"Film ajouté : {film_data['titre']}")

        # Ajouter les séries
        for serie_data in series:
            if not Media.query.filter_by(titre=serie_data['titre'], utilisateur_id=utilisateur.id).first():
                serie = Media(utilisateur_id=utilisateur.id, **serie_data)
                db.session.add(serie)
                print(f"Série ajoutée : {serie_data['titre']}")

        db.session.commit()
        print("Base de données initialisée avec succès !")

if __name__ == '__main__':
    init_database()
