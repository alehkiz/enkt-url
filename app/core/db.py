from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemySessionUserDatastore
from flask.cli import with_appcontext
import click

db = SQLAlchemy(session_options={'autoflush': True})

from app.models.security import User, Role

user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    # db.drop_all()
    # db.create_all()
    click.echo('Banco de dados inicializado...')
    from app.models.security import User
    from app.models.network import Network
    network = Network.query.filter(Network.ip == '0.0.0.0').first()
    if network is None:
        network = Network()
        network.ip = '0.0.0.0'
        db.session.add(network)
        db.session.commit()
    
    anon = User.query.filter(User.username == 'ANON').first()
    
    if anon is None:
        anon = User()
        anon.id = 4
        anon.username = 'ANON'
        anon.name = 'ANON'
        anon.email = 'anon@localhost'
        anon.created_network_id = network.id
        anon._password = '123'
        anon.current_login_network_id = network.id
        anon.temp_password = True
        db.session.add(anon)
        db.session.commit()
        click.echo('Usuário anonimo adicionado')

    admin = User.query.filter(User.username == 'admin').first()
    if admin is None:
        admin = User()
        admin.username = 'admin'
        admin.name = 'admin'
        admin.email = 'admin@localhost'
        admin.created_network_id = network.id
        admin.current_login_network_id = network.id
        admin.password = 'Abc123'
        admin.active = True
        admin.temp_password = False
        db.session.add(admin)
        db.session.commit()
        click.echo('Administrador criado...')

    admin_role = Role.query.filter(Role.name == 'admin').first()
    if admin_role is None:
        admin_role = Role()
        admin_role.level = 0
        admin_role.name = 'admin'
        admin_role.description = 'Administrator'
        db.session.add(admin_role)
        admin.roles.append(admin_role)
        db.session.commit()
    
    # man_user = Role.query.filter(Role.name == 'manager_user').first()
    # if man_user is None:
    #     man_user = Role()
    #     man_user.level = 1
    #     man_user.name = 'manager_user'
    #     man_user.description = 'Gerenciador de Usuários'
    #     db.session.add(man_user)
    #     db.session.commit()

    # man_cont = Role.query.filter(Role.name == 'manager_content').first()
    # if man_cont is None:
    #     man_cont = Role()
    #     man_cont.level = 2
    #     man_cont.name = 'manager_content'
    #     man_cont.description = 'Gerenciador de Conteúdo'
    #     db.session.add(man_cont)
    #     db.session.commit()

    # aux_cont = Role.query.filter(Role.name == 'aux_content').first()
    # if aux_cont is None:
    #     aux_cont = Role()
    #     aux_cont.level = 3
    #     aux_cont.name = 'aux_content'
    #     aux_cont.description = 'Colaborador de Conteúdo'
    #     db.session.add(aux_cont)
    #     db.session.commit()

    # support_cont = Role.query.filter(Role.name == 'support').first()
    # if support_cont is None:
    #     support_cont = Role()
    #     support_cont.level = 5
    #     support_cont.name = 'support'
    #     support_cont.description = 'Suporte'
    #     db.session.add(support_cont)
    #     db.session.commit()

    # view_cont = Role.query.filter(Role.name == 'viewer_content').first()
    # if view_cont is None:
    #     view_cont = Role()
    #     view_cont.level = 5
    #     view_cont.name = 'viewer_content'
    #     view_cont.description = 'Visualizador de Conteúdo'
    #     db.session.add(view_cont)
    #     db.session.commit()


    click.echo('Tabelas necessárias populadas')