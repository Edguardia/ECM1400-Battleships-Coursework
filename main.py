"""module for flask application"""
import secrets
from flask import Flask, render_template, request, jsonify, session
import yaml
import components
import game_engine
import mp_game_engine
from base_logger import logger

with open("config.yaml", "r", encoding='utf-8') as file:
    config = yaml.safe_load(file)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SESSION_TYPE'] = 'memcached'

players = {"player": [],
           "ai": []}


@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    """interacts with the placement decorator screen"""
    if request.method == "GET":
        session.clear()
        for user in players:
            players[user] = [
                components.initialise_board(int(config['board_size'])), components.create_battleships(), []]
        players["ai"][0] = components.place_battleships(
            players["ai"][0], players["ai"][1], algorithm="random")
        return render_template("placement.html", ships=players["player"][1], board_size=len(players["player"][0]))

    if request.method == "POST":
        board_data = request.get_json()
        print(board_data)
        components.place_battleships(
            players["player"][0], players["player"][1], board_data=board_data, algorithm='custom')
        return jsonify({"message": "received"}), 200


@app.route("/", methods=["GET"])
def root():
    """interacts with the root decorator screen"""
    if request.method == "GET":
        return render_template("main.html", player_board=players["player"][0])


@app.route("/attack", methods=["GET", "POST"])
def process_attack():
    """interacts with the attack decorator screen"""

    if 'playerHits' not in session or 'aiHits' not in session or 'needed_hits' not in session:
        session['playerHits'] = 0
        session['aiHits'] = 0
        session['needed_hits'] = sum(players["ai"][1].values())

    if request.method == "GET":
        ai_previous_target = True
        ai_turn = (0, 0)
        x = request.args.get('x')
        y = request.args.get('y')
        player_target_coordinates = (int(x), int(y))
        if player_target_coordinates in players["player"][2]:
            return

        while ai_previous_target is True:
            ai_turn = mp_game_engine.generate_attack(len(players["player"][0]))
            if ai_turn not in players["ai"][2]:
                ai_previous_target = False
                players["ai"][2].append(ai_turn)

        ai_hit_or_miss = game_engine.attack(
            ai_turn, players["player"][0], players["player"][1])
        hit_or_miss = game_engine.attack(
            (int(x), int(y)), players["ai"][0], players["ai"][1])

        players["player"][2].append(player_target_coordinates)
        if ai_hit_or_miss is True:
            session['aiHits'] += 1

        if hit_or_miss is True:
            session['playerHits'] += 1

        if session['playerHits'] == session['needed_hits'] and session['aiHits'] == session['needed_hits']:
            return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn, "finished": "Draw!"})

        if session['playerHits'] == session['needed_hits']:
            return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn, "finished": "You Win!"})

        if session['aiHits'] == session['needed_hits']:
            return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn, "finished": "You Lose!"})

        return jsonify({"hit": hit_or_miss, "AI_Turn": ai_turn})


if __name__ == "__main__":

    logger.info("Starting Flask Application")
    app.run(debug=True)
