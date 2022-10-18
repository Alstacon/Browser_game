from flask import Flask, render_template, request, redirect, url_for

from classes.arena.arena import Arena
from classes.equipment.equipment import Equipment
from classes.equipment.equipment_data import EquipmentData
from classes.units.abstract_unit import BaseUnit
from classes.units.enemy_unit import EnemyUnit
from classes.units.player_unit import PlayerUnit
from classes.units.units import unit_classes


def create_app() -> Flask:
    app = Flask(__name__)

    return app


app = create_app()

heroes = {
}

arena = Arena()


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/choose_hero/', methods=['GET', 'POST'])
def choose_hero():
    equipment = Equipment()
    result: dict = {'header': "Выберите героя для себя",
                    'classes': unit_classes,
                    'weapons': equipment.get_weapon_names(),
                    'armors': equipment.get_armor_names(),
                    'url': "window.location.href='/choose_enemy/'"}
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result), 200

    if request.method == 'POST':
        data = request.values
        player = PlayerUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        player.equip_weapon(equipment.get_weapon(data.get('weapon')))
        player.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['player'] = player
        return render_template('hero_choosing.html', result=result)


@app.route('/choose_enemy/', methods=['GET', 'POST'])
def choose_enemy():
    equipment = Equipment()
    result: dict = {'header': "Выберите героя для соперника",
                    'classes': unit_classes,
                    'weapons': equipment.get_weapon_names(),
                    'armors': equipment.get_armor_names(),
                    'url': "window.location.href='/fight/'"}
    if request.method == 'GET':
        return render_template('hero_choosing.html', result=result)

    if request.method == 'POST':
        data = request.values
        enemy = EnemyUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        enemy.equip_weapon(equipment.get_weapon(data.get('weapon')))
        enemy.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['enemy'] = enemy
        return redirect(url_for('fight'), code=302)


@app.route('/fight/')
def fight():
    arena.start_game(heroes['player'], heroes['enemy'])
    return render_template('fight.html', heroes=heroes, battle_result=arena._end_game(), result=arena.next_turn())


if __name__ == "__main__":
    app.run()
