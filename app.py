from flask import Flask, render_template, request, redirect

from assets import char_information, heroes, equipment, arena
from classes.units.enemy_unit import EnemyUnit
from classes.units.player_unit import PlayerUnit
from classes.units.units import unit_classes

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/choose_hero/', methods=['GET', 'POST'])
def choose_hero():
    char_information['header'] = "Выберите героя для себя"
    char_information['url'] = "window.location.href='/choose_enemy/'"
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=char_information), 200

    elif request.method == 'POST':
        data = request.values
        player = PlayerUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        player.equip_weapon(equipment.get_weapon(data.get('weapon')))
        player.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['player'] = player
        return redirect('/choose_enemy/'), 302


@app.route('/choose_enemy/', methods=['GET', 'POST'])
def choose_enemy():
    char_information['header'] = "Выберите героя для соперника"
    char_information['url'] = "window.location.href='/fight/'"
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=char_information), 200

    elif request.method == 'POST':
        data = request.values
        enemy = EnemyUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        enemy.equip_weapon(equipment.get_weapon(data.get('weapon')))
        enemy.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['enemy'] = enemy
        return redirect('/fight/'), 302


@app.route('/fight/')
def fight():
    arena.start_game(heroes['player'], heroes['enemy'])
    return render_template('fight.html', heroes=heroes)


@app.route('/fight/hit')
def fight_hit():
    if arena.game_is_running:
        return render_template('fight.html', heroes=heroes, result=arena.player_hit())
    else:
        return render_template('fight.html', heroes=heroes, battle_result=arena.next_turn())


@app.route('/fight/use_skill')
def use_skill():
    if arena.game_is_running:
        return render_template('fight.html', heroes=heroes, result=arena.player_use_skill())
    else:
        return render_template('fight.html', heroes=heroes, battle_result=arena.next_turn())


@app.route('/fight/pass_turn')
def pass_turn():
    return render_template('fight.html', heroes=heroes, battle_result=arena.next_turn())


@app.route('/fight/end_fight')
def end_fight():
    return render_template("index.html", heroes=heroes)


if __name__ == "__main__":
    app.run()
