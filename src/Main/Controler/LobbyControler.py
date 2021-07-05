from flask import Request, render_template, session


def lobbyControler(request: Request,party_id):
    if 'uuid' in session:
        # Le player existe deja
        uuid = session["uuid"];
    else:
        print("Aucun uuid dans la session")
    print("player uuid : "+str(uuid))
    print(session)
    return render_template('lobby.html',party_id=party_id,uuid=uuid)