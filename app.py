from flask import Flask, render_template, request, redirect, url_for

from classes.arena.arena import Arena
from classes.equipment.equipment import Equipment
from classes.equipment.equipment_data import EquipmentData
from classes.units.abstract_unit import BaseUnit
from classes.units.enemy_unit import EnemyUnit
from classes.units.player_unit import PlayerUnit
from classes.units.units import unit_classes

app = Flask(__name__)

heroes = {}

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

    elif request.method == 'POST':
        data = request.values
        player = PlayerUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        player.equip_weapon(equipment.get_weapon(data.get('weapon')))
        player.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['player'] = player
        return redirect('/choose_enemy/')


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

    elif request.method == 'POST':
        data = request.values
        enemy = EnemyUnit(data.get('name'), unit_classes.get(data.get('unit_class')))
        enemy.equip_weapon(equipment.get_weapon(data.get('weapon')))
        enemy.equip_armor(equipment.get_armor(data.get('armor')))
        heroes['enemy'] = enemy
        return redirect('/fight/')


@app.route('/fight/')
def fight():
    arena.start_game(heroes['player'], heroes['enemy'])
    return render_template('fight.html', heroes=heroes)


@app.route('/fight/hit')
def fight_hit():
    return render_template('fight.html', heroes=heroes, result=arena.player_hit(), battle_result=arena.next_turn())


@app.route('/fight/use_skill')
def use_skill():
    arena.player_use_skill()
    return render_template('fight.html', heroes=heroes)


@app.route('/fight/pass_turn')
def pass_turn():
    arena.next_turn()
    return render_template('fight.html', heroes=heroes)


@app.route('/fight/end_fight')
def end_fight():
    return render_template('fight.html', heroes=heroes, result=arena.end_game())


if __name__ == "__main__":
    app.run()
