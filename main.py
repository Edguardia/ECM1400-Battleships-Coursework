from flask import Flask, render_template, request, jsonify, session
import components
import game_engine
import mp_game_engine


app = Flask(__name__)

players = {"player": [],
           "ai": []}


def user_ship_placement():
    """creates the initial board and ships for each player"""
    for user in players:
        players[user] = [
            components.initialise_board(), components.create_battleships()]
    players["ai"][0] = components.place_battleships(
        players["ai"][0], players["ai"][1], algorithm="random")


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    """interacts with the placment decorator screen"""
    if request.method == "GET":
        return render_template("placement.html", ships=players["player"][1], board_size=10)

    elif request.method == "POST":
        board_data = request.get_json()
        print(board_data)
        components.place_battleships(
            players["player"][0], players["player"][1], board_data, algorithm='custom')
        return jsonify({"message": "recieved"}), 200


@app.route("/", methods=["GET"])
def root():
    """interacts with the root decorator screen"""
    if request.method == "GET":
        return render_template("main.html", player_board=players["player"][0])


@app.route("/attack", methods=["GET", "POST"])
def flask_attack():
    if 'playerHits' not in session or 'aiHits' not in session or 'needed_hits' not in session:
        session['playerHits'] = 0
        session['aiHits'] = 0
        session['needed_hits'] = sum(players["ai"][1].values())

    if request.method == "GET":

        x = request.args.get('x')
        y = request.args.get('y')
        ai_turn = mp_game_engine.generate_attack(players["player"][0])
        ai_hit_or_miss = game_engine.attack(
            ai_turn, players["player"][0], players["player"][1])
        hit_or_miss = game_engine.attack(
            (int(x), int(y)), players["ai"][0], players["ai"][1])

        if ai_hit_or_miss is True:
            session['aiHits'] += 1

        if hit_or_miss is True:
            session['playerHits'] += 1

        if session['playerHits'] == session['needed_hits']:
            return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn, "finished": "You Win!"})

        if session['aiHits'] == session['needed_hits']:
            return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn, "finished": "You Lose!"})

        return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn})


if __name__ == "__main__":
    user_ship_placement()
    app.secret_key = 'dsjadiasojdajidoai'

    app.run(debug=True)
