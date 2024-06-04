#-------------------------------------------------------------------------------
# Name:        W40k combat simulator
# Purpose:     Fun and learning :)
# Author:      nemanja
# Created:     19-02-2024
# Copyright:   (c) nemanja 2024
# Licence:     <Free>
# Version:     W1.1K
#Instrukcije: Unosite redom potrebne informacije i sistem obracuna sve na kraju.
#Novi unosi su blast, cover i plunging fire.
#Ne unosi se vise broj kockica vec koliko ima modela i attack karakteristika oruzja.
#-------------------------------------------------------------------------------
import random
import sys

def main():
    #--------------------------- Unit/Model setings ----------------
    #attacking models
    print("---------------------- Unit/Model setings ---------------------")
    print("Enter number of ATTACKING models in unit:")
    attacking_models = int(input())
    if attacking_models == 0:
        print("You must enter number 1 or above.")
        sys.exit()
    #defending models
    print("Enter number of DEFENDING models in unit:")
    defending_models = int(input())
    if defending_models == 0:
        print("You must enter number 1 or above.")
        sys.exit()
    print("Enter enemy Toughness")
    enemy_toughness = int(input())
    print("Enter armor save:")
    armor_save = int(input())
    #--------------------------- To Hit ----------------------------
    #input1  type and number of attacks
    print("--------------------------- To Hit ----------------------------")
    print("Your BS/WS skill:")
    model_weapon_skill = int(input())
    print("Enter 1 if number of att is whole number or 0 if number is D6, 2D6, D6+1 od D3")
    type_of_number_att = int(input())
    number_of_attacks = 0
    number_of_models = attacking_models
    if type_of_number_att == 1:
        print("Enter attack characteristic of weapon A)")
        noa = int(input())
        number_of_attacks = noa * number_of_models
    else:
        print("Enter attack characteristic of Weapon: D6, D6+1, 2D6 or D3")
        type_of_attacks = input()
        dx_roll_list = []
        if type_of_attacks == "D6":
            for i in range(0, number_of_models):
                dx_roll = random.randint(1,6)
                dx_roll_list.append(dx_roll)
                dx_sum = sum(dx_roll_list)
                number_of_attacks = dx_sum
        elif type_of_attacks == "D6+1":
            for i in range(0, number_of_models):
                dx_roll = random.randint(1,6)
                dx_roll += 1
                dx_roll_list.append(dx_roll)
                dx_sum = sum(dx_roll_list)
                number_of_attacks = dx_sum
        elif type_of_attacks == "2D6":
            noa = number_of_models + number_of_models
            for i in range(0, noa):
                dx_roll = random.randint(1,6)
                dx_roll_list.append(dx_roll)
                dx_sum = sum(dx_roll_list)
                number_of_attacks = dx_sum
        elif type_of_attacks == "D3":
            for i in range(0, number_of_models):
                dx_roll = random.randint(1,3)
                dx_roll_list.append(dx_roll)
                dx_sum = sum(dx_roll_list)
                number_of_attacks = dx_sum
    # blast pravilo
    print("Is there Blast rule for weapon? y or n")
    blast_conf = str(input())
    if blast_conf == "y" and defending_models != 1:
        blast = defending_models // 5
        number_of_attacks = blast * attacking_models + number_of_attacks
    else:
        pass
    #var and list
    hit_roll = 0
    miss_roll = 0
    hit_roll_list = []
    miss_roll_list = []
    dice_roll_list = []
    attack = number_of_attacks
    skill = model_weapon_skill
    #rolling to hit
    for i in range(0, attack):
        d6_roll = random.randint(1, 6)
        if skill <= d6_roll <= 6:
            hit_roll += 1
            hit_roll_list.append(d6_roll)
            dice_roll_list.append(d6_roll)
        else:
            miss_roll += 1
            miss_roll_list.append(d6_roll)
            dice_roll_list.append(d6_roll)
    #spajanje listi
    d6_dice = " "
    d6_hit = " "
    d6_miss = " "
    dice_roll_str = d6_dice.join(str(e) for e in dice_roll_list)
    hit_roll_str = d6_hit.join(str(e) for e in hit_roll_list)
    miss_roll_str = d6_miss.join(str(e) for e in miss_roll_list)

    #output1 to hit phase results
    if hit_roll >= 1:
        print("------------Hit roll------------")
        print(f"Dice roll results : {dice_roll_str}.")
        print(f"Attackers successful rolls are: {hit_roll_str}.")
        print(f"Attackers unsuccessful rolls are: {miss_roll_str}")
        print(f"Attacker roll {number_of_attacks} and hit defenders with {hit_roll} attacks.")
        print(f"{miss_roll} attacks missed the target.")
        print("------------Hit roll------------")
    else:
        print("------------Hit roll------------")
        print(f"Dice roll results : {dice_roll_str}")
        print(f"Wow, that is really a badd roll. Zero hits.")
        print("------------Hit roll------------")
        sys.exit()
    stage = 1
    #---------------------------- To Wound ----------------------------
    #input2 weapon strength
    print(" ")
    print("---------------------------- To Wound ----------------------------")
    print("Enter strength of weapon:")
    weapon_strength = int(input())
    #var and list
    num_of_attacks = hit_roll
    toughtnes = enemy_toughness
    strenght = weapon_strength
    need_to_wound = 0
    wound_roll_pen = 0
    wound_roll_def = 0
    wound_roll_list = []
    wound_pen_list = []
    wound_def_list = []
    #chek what roll need for wound
    if strenght == toughtnes:
        need_to_wound = 4
    elif strenght > toughtnes:
        if strenght - toughtnes >= 2:
            need_to_wound = 2
        else:
            need_to_wound = 3
    elif strenght < toughtnes:
        if toughtnes - strenght >= 2:
            need_to_wound = 6
        else:
            need_to_wound = 5
    print(" ")
    print(f"Attackers need {need_to_wound} to wound defenders models.")
    print(" ")
    #rolling to wound
    for i in range(0, num_of_attacks):
        wound_roll = random.randint(1, 6)
        if wound_roll >= need_to_wound:
            wound_roll_pen += 1
            wound_pen_list.append(wound_roll)
            wound_roll_list.append(wound_roll)
        else:
            wound_roll_def += 1
            wound_roll_list.append(wound_roll)
            wound_def_list.append(wound_roll)

    #spajanje wound listi
    d6_wound_roll = " "
    d6_wound_pen = " "
    d6_wound_def = " "
    dice_roll_str = d6_wound_roll.join(str(e) for e in wound_roll_list)
    def_roll_str = d6_wound_def.join(str(e) for e in wound_def_list)
    pen_roll_str = d6_wound_pen.join(str(e) for e in wound_pen_list)
    #output wound roll
    if wound_roll_pen >= 1:
        print("------------Wound roll------------")
        print(f"Dice roll results : {dice_roll_str}.")
        print(f"Attackers successful penetrating rolls are: {pen_roll_str}.")
        print(f"Attackers unsuccessful penetrating rolls are: {def_roll_str}.")
        print(f"Attackers roll {num_of_attacks} and wound defenders with {wound_roll_pen} attacks.")
        print(f"Defenders deflect {wound_roll_def} attacks.")
        print("------------Wound roll------------")
        print(" ")
    else:
        print("------------Wound roll------------")
        print(f"Dice roll results : {dice_roll_str}")
        print(f"Now that is a definition of a bad roll. Zero hits.")
        print("------------Wound roll------------")
        print(" ")
        sys.exit()
    stage = 2
    #---------------------------- Armor Save ----------------------------
    #input3 weapon AP and save
    print("---------------------------- Armor Save ----------------------------")
    print("Enter weapon AP:")
    weapon_ap = int(input())
    armor_save_dice = wound_roll_pen
    print("Are attacking models have plunging fire rule? y or n")
    plunging_fire = str(input())
    print("Are defending model in cover? y or n")
    cover = str(input())

    #bazne promenjive
    cover_bonus = 0
    armor_pass_roll = 0
    armor_fail_roll = 0
    armor_pass_list = []
    armor_fail_list = []
    armor_save_list = []

    #cheking modifiers
    if cover == "y":
        if armor_save <= 3 and weapon_ap == 0:
            cover_bonus = 0
        elif armor_save <= 3 and weapon_ap >= 1:
            cover_bonus = 1
        elif armor_save >= 4:
            cover_bonus = 1
    else:
        cover_bonus = 0
    if plunging_fire == "y":
        plunging_bonus = 1
    else:
        plunging_bonus = 0

    #calculating armor save
    ap_modifier = weapon_ap + plunging_bonus
    armor_save_modifier = armor_save - cover_bonus
    armor_save_roll = armor_save_modifier + ap_modifier

    print(" ")
    print(f"Defending models armor save is {armor_save_roll}.")

    if armor_save_roll > 6:
        print(" ")
        print("Defenders armor is too weak for attackers firepower.")
        print(f"All {armor_save_dice} hits inflict damage on target")
        armor_fail_roll = armor_save_dice
    else:
        for i in range(0, armor_save_dice):
            armor_roll = random.randint(1, 6)
            if armor_roll >= armor_save_roll:
                armor_pass_roll += 1
                armor_pass_list.append(armor_roll)
                armor_save_list.append(armor_roll)
            else:
                armor_fail_roll += 1
                armor_fail_list.append(armor_roll)
                armor_save_list.append(armor_roll)

        #spajanje wound listi
        d6_save_roll = " "
        d6_pase_roll = " "
        d6_failed_roll = " "
        dice_roll_str = d6_save_roll.join(str(e) for e in armor_save_list)
        pass_roll_str = d6_pase_roll.join(str(e) for e in armor_pass_list)
        failed_roll_str = d6_failed_roll.join(str(e) for e in armor_fail_list)

        #output save roll
        if armor_fail_roll == 0:
            print(" ")
            print("------------Armor save roll------------")
            print(f"Dice roll results : {dice_roll_str}.")
            print(f"Defenders successful rolls are: {pass_roll_str}.")
            print(f"Attackers weapons where to weak for defenders.")
            print("------------Armor save roll------------")
            sys.exit()
        else:
            print(" ")
            print("------------Armor save roll------------")
            print(f"Dice roll results : {dice_roll_str}.")
            print(f"Defenders successful rolls are: {pass_roll_str}.")
            print(f"Defenders unsuccessful rolls are: {failed_roll_str}")
            print(f"Defenders mange to save {armor_pass_roll} hits.")
            print(f"Attackers manage to penetrated armor whit {armor_fail_roll} hits.")
            print("------------Armor save roll------------")
    stage = 3
    #---------------------------- Damage ----------------------------
    #input4 damage
    print(" ")
    print("---------------------------- Damage ----------------------------")
    print("Enter weapon damage: D6, D6+1, 2D6 or D3 or whole number1.")
    dmg = input()
    print("Enter wounds per model")
    wounds_per_model = int(input())
    #var and list
    penetrating_hits = armor_fail_roll
    wounds = wounds_per_model
    model = wounds
    def_unit = defending_models
    weapon = ""
    passd6DmgList = []
    nod6DmgList = []
    passd61DmgList = []
    nod61DmgList = []
    passd3DmgList = []
    nod3DmgList = []

    if dmg == "D6":
        weapon = "D6"
    elif dmg == "D6+1":
        weapon = "D6+1"
    elif dmg == "D3":
        weapon = "D3"
    else:
       weapon_conv = int(dmg)
       weapon = weapon_conv

    #chkeking if here is solo model or unit, and then apply dmg
    #solo model
    if def_unit == 1:
        if weapon == "D6":
            for i in range(0, penetrating_hits):
                dmg_roll = random.randint(1, 6)
                passd6DmgList.append(dmg_roll)
            combo_dmg = sum(passd6DmgList)
            if combo_dmg >= wounds:
                model = 0
            else:
                model -= combo_dmg
        elif weapon == "D3":
            for i in range(0,penetrating_hits):
                dmg_roll = random.randint(1, 3)
                passd3DmgList.append(dmg_roll)
            combo_dmg = sum(passd3DmgList)
            if combo_dmg >= wounds:
                model = 0
            else:
                model -= combo_dmg
        elif weapon == "D6+1":
            for i in range(0, penetrating_hits):
                dmg_roll = random.randint(2, 7)
                passd61DmgList.append(dmg_roll)
            combo_dmg = sum(passd61DmgList)
            if combo_dmg >= wounds:
                model = 0
            else:
                model -= combo_dmg
        else:
            print(penetrating_hits)
            combo_dmg = penetrating_hits * weapon
            if combo_dmg >= wounds:
                model = 0
            else:
                model -= combo_dmg
    #unit
    elif def_unit > 1:
        if weapon == "D6":
            for i in range(0, penetrating_hits):
                dmg_roll = random.randint(1, 6)
                if dmg_roll >= wounds:
                    def_unit -= 1
                    passd6DmgList.append(dmg_roll)
                    if def_unit == 0:
                        break
                else:
                    nod6DmgList.append(dmg_roll)
            leftOverDmg = sum(nod6DmgList)
            for i in range(0, def_unit):
                if leftOverDmg > 0:
                    if leftOverDmg < wounds:
                        model -= leftOverDmg
                        break
                    else:
                        leftOverDmg -= wounds
                        def_unit -= 1
                else:
                    break
        elif weapon == "D6+1":
            for i in range(0, penetrating_hits):
                dmg_roll = random.randint(2, 7)
                if dmg_roll >= wounds:
                    def_unit -= 1
                    passd61DmgList.append(dmg_roll)
                    if def_unit == 0:
                        break
                else:
                    nod61DmgList.append(dmg_roll)
            leftOverDmg = sum(nod61DmgList)
            for i in range(0, def_unit):
                if leftOverDmg > 0:
                    if leftOverDmg < wounds:
                        model -= leftOverDmg
                        break
                    else:
                        leftOverDmg -= wounds
                        def_unit -= 1
                else:
                    break
        elif weapon == "D3":
            for i in range(0, penetrating_hits):
                dmg_roll = random.randint(1, 3)
                if dmg_roll >= wounds:
                    def_unit -= 1
                    passd3DmgList.append(dmg_roll)
                else:
                    nod3DmgList.append(dmg_roll)

            leftOverDmg = sum(nod3DmgList)
            for i in range(0, def_unit):
                if leftOverDmg > 0:
                    if leftOverDmg < wounds:
                        model -= leftOverDmg
                        break
                    else:
                        leftOverDmg -= wounds
                        def_unit -= 1
                else:
                    break
        else:
            if weapon >= wounds:
                for i in range(0, penetrating_hits):
                    def_unit -= 1
            elif weapon < wounds:
                combo_dmg = penetrating_hits * weapon
                print(combo_dmg)
                model = wounds
                for i in range(0, def_unit):
                    if combo_dmg > 0:
                        if combo_dmg < wounds:
                            model -= combo_dmg
                            #break
                        else:
                            combo_dmg -= wounds
                            def_unit -= 1
    stage = 4
    #output dmg
    if defending_models == 1:
        if model > 0:
            print(" ")
            print(f"Defender is left with {model} wounds left.")
        else:
            print(" ")
            print(f"Defender went to warp.")
            print("VICTORY!")
    elif defending_models > 1:
        if def_unit > 0:
            print(" ")
            if wounds == 1:
                print(f"Defender unit is still standing, and they have {def_unit} models left.")
            else:
                print(f"Defender unit is still standing, whit {def_unit} models left, one model has {model} wounds.")
        else:
            print(" ")
            print("Blood bath, you smoked the enemy unit straight to warp.")
            print("VICTORY!")
    else:
        pass

if __name__ == '__main__':
    main()
