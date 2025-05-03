from app import create_app, db
from app.models import User, Product

def create_mocks():
    app = create_app()
    
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        admin = User(username='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        
        products = [
            Product(name='prod1', description='Manga Blue Lock',price=999.99, quantite=10, image='is.jpg'),
            Product(name='prod2', description='Manga Blue Lock',price=29.99, quantite=50, image='is1.jpg'),
            Product(name='prod3', description='Manga Blue Lock', price=89.99, quantite=30, image='lu.jpg'),
        ]
        db.session.add_all(products)
        
        db.session.commit()
        print("✅ Mocks créés avec succès !")

if __name__ == '__main__':
    create_mocks()  