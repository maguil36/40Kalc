from random import random
from statistics import mean
from statistics import stdev
import numpy as np
from pi_dice import dice3, dice6
##functions for monte carlo sim
def min_expect(lw1, ld):
	if round(sum(lw1) - mean(ld) - 2*stdev(ld)) < 0:
		return ("0")
	else:
		return (str(round(sum(lw1) - mean(ld) - 2*stdev(ld))))
def max_expect(lw1, ld):
	if round(sum(lw1) - mean(ld) + 2*stdev(ld)) > sum(lw1):
		return(str(sum(lw1)))
	else:
		return (str(round(sum(lw1) - mean(ld) + 2*stdev(ld))))
def shots_blast(noe, blst):
	if blst == 'blast D3':
		if noe >= 6:
			return(3)
		else:
			return (dice3())
	elif blst == 'D3':
		return (dice3())
	elif blst == 'blast D6':
		d0 = dice6()
		if noe >= 11:
			return(6)
		elif noe >= 6 and d0 < 3:
			return(3)
		else:
			return (d0)
	elif blst == 'D6':
		return (dice6())
	elif blst == 'blast 2D3':
		d0, d1 = dice3(), dice3()
		if noe >= 11:
			return(6)
		elif noe >= 6 and d0 + d1 < 3:
			return(3)
		else:
			return (d0 + d1)
	elif blst == '2D3':
		return (dice3()+dice3())
	elif blst == 'blast 2D6':
		d0, d1 = dice6(), dice6()
		if noe >= 11 and d0 + d1 < 6:
			return(6)
		elif noe >= 6 and d0 + d1 < 3:
			return(3)
		else:
			return (d0 + d1)
	elif blst == '2D6':
		return (dice6()+dice6())
	elif btn_blst["text"] == 'blast 4D6':
		d0, d1, d2, d3 = dice6(), dice6(), dice6(), dice6()
		if noe >= 11 and d0 + d1 + d2 + d3 < 6:
			return(6)
		else:
			return (d0 + d1 + d2 + d3)
	else:
		return (dice6()+dice6()+dice6()+dice6())
def hitting(exp, bs, flm, dak, hit_rr, exp_int, h6iw, dict_0, dict_1):
	if h6iw != "6 wound on":
		if exp != "explode off":
			if hit_rr == "reroll off":
				r0 = random()

				if r0 < 1/6:
					return exp_int
				elif r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r1 = random()
					dict_1['rh'] -= 1
					if r1 < 1/6:
						return exp_int
					elif r1 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1 = random(), random()

				if r0 < 1/6:
					return exp_int
				elif r0 > 5/6 and r1 < 1/6:
					return exp_int
				elif r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1 = random(), random()

				if r0 < 1/6:
					return exp_int
				elif r0 > bs and r1 < 1/6:
					return exp_int
				elif r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0)
		elif dak == "dakka on":
			if hit_rr == "reroll off":
				r0, r1 = random(), random()
			
				if r0 < 1/6 and r1 < bs:
					return (2)
				elif r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r2 = random()
					dict_1['rh'] -= 1
					if r2 < 1/6 and r1 < bs:
						return (2)
					elif r1 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1, r2, r3 = random(), random(), random(), random()

				if r0 < 1/6 and r1 < bs:
					return (2)
				elif r0 > 5/6 and r1 < 1/6 and r2 < bs:
					return (2)
				elif r0 < 1/6 and r1 > 5/6 and r2 < bs:
					return (2)
				elif r0 > 5/6 and r1 < 1/6 and r0 > 5/6 and r3 < bs:
					return (2)
				elif r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1, r2, r3 = random(), random(), random(), random()

				if r0 < 1/6 and r1 < bs:
					return (2)
				elif r0 > bs and r1 < 1/6 and r0 < bs:
					return (2)
				elif r0 < 1/6 and r0 > bs and r0 < bs:
					return (2)
				elif r0 > bs and r1 < 1/6 and r2 > bs and r3 < bs:
					return (2)
				elif r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0)
		elif flm != "flame off":
			if flm == "flame D3":
				return (dice3())
			elif flm == "flame D6":
				return (dice6())
			elif flm == "flame 2D6":
				return (dice6()+dice6())
		else:
			if hit_rr == "reroll off":
				r0 = random()

				if r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r1 = random()
					dict_1['rh'] -= 1
					if r1 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1 = random(), random()

				if r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1 = random(), random()
				if r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0)
	else:
		if exp != "explode off":
			if hit_rr == "reroll off":
				r0 = random()
				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return exp_int-1
				elif r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r1 = random()
					dict_1['rh'] -= 1
					if r1 < 1/6:
						dict_0["l6hiw"] += 1
						return exp_int-1
					elif r1 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1 = random(), random()

				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return exp_int-1
				elif r0 > 5/6 and r1 < 1/6:
					dict_0["l6hiw"] += 1
					return exp_int-1
				elif r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1 = random(), random()

				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return exp_int-1
				elif r0 > bs and r1 < 1/6:
					dict_0["l6hiw"] += 1
					return exp_int-1
				elif r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0)
		elif dak == "dakka on":
			if hit_rr == "reroll off":
				r0, r1 = random(), random()
				if r0 < 1/6 and r1 < 1/6:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 < 1/6 and r1 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 < 1/6 and r1 > bs:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r2 = random()
					dict_1['rh'] -= 1
					if r2 < 1/6 and r1 < 1/6:
						dict_0["l6hiw"] += 2
						return (0)
					elif r2 < 1/6 and r1 < bs:
						dict_0["l6hiw"] += 1
						return (1)
					elif r2 < 1/6 and r1 > bs:
						dict_0["l6hiw"] += 1
						return (0)
					elif r2 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1, r2, r3 = random(), random(), random(), random()
				if r0 < 1/6 and r1 < bs:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 > 5/6 and r1 < 1/6 and r2 < bs:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 < 1/6 and r1 > 5/6 and r2 < bs:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 > 5/6 and r1 < 1/6 and r0 > 5/6 and r3 < bs:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 < 1/6 and r1 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 > 5/6 and r1 < 1/6 and r2 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 < 1/6 and r1 > 5/6 and r2 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 > 5/6 and r1 < 1/6 and r0 > 5/6 and r3 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1, r2, r3 = random(), random(), random(), random()
				if r0 < 1/6 and r1 < 1/6:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 > bs and r1 < 1/6 and r0 < 1/6:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 < 1/6 and r0 > bs and r0 < 1/6:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 > bs and r1 < 1/6 and r2 > bs and r3 < 1/6:
					dict_0["l6hiw"] += 2
					return (0)
				elif r0 < 1/6 and r1 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 > bs and r1 < 1/6 and r0 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 < 1/6 and r0 > bs and r0 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 > bs and r1 < 1/6 and r2 > bs and r3 < bs:
					dict_0["l6hiw"] += 1
					return (1)
				elif r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0)
		else:
			if hit_rr == "reroll off":
				r0 = random()
				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 < bs:
					return (1)
				elif r0 > bs and dict_1['rh'] == 1:
					r1 = random()
					dict_1['rh'] -= 1
					if r1 < 1/6:
						dict_0["l6hiw"] += 1
						return (0)
					elif r1 < bs:
						return (1)
					else: 
						return (0)
				else:
					return (0)
			elif hit_rr == "reroll 1s":
				r0, r1 = random(), random()
				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 > 5/6 and r1 < 1/6:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 < bs:
					return (1)
				elif r0 > 5/6 and r1 < bs:
					return (1)
				else:
					return (0)
			else:
				r0, r1 = random(), random()
				if r0 < 1/6:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 > bs and r1 < 1/6:
					dict_0["l6hiw"] += 1
					return (0)
				elif r0 < bs:
					return (1)
				elif r1 < bs:
					return (1)
				else:
					return (0) 
def wounding(wnd, wnd_rr, mwo6, dict_0, dict_1):
	if mwo6 != "6 no mw":
		if wnd_rr == "reroll off":
			r0 = random()
			if r0 < 1/6:
				dict_0["lmw"] += 1
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r0 > wnd and dict_1['rw'] == 1:
				r1 = random()
				dict_1['rw'] -= 1
				if r1 < 1/6:
					dict_0["lmw"] += 1
					dict_0["leapad"] += 1
					return (0)
				elif r1 < wnd:
					return (1)
				else: 
					return (0)
			else:
				return (0)
		elif wnd_rr == "reroll 1s":
			r0, r1 = random(), random()
			if r0 < 1/6:
				dict_0["lmw"] += 1
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r0 > 5/6 and r1 < 1/6:
				dict_0["lmw"] += 1
				dict_0["leapad"] += 1
				return (0)
			elif r0 > 5/6 and r1 < wnd:
				return (1)
			else:
				return (0)
		else:
			r0, r1 = random(), random()
			if r0 < 1/6:
				dict_0["lmw"] += 1
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r1 < 1/6:
				dict_0["lmw"] += 1
				dict_0["leapad"] += 1
				return (0)
			elif r1 < wnd:
				return (1)
			else:
				return (0)
	else:
		if wnd_rr == "reroll off":
			r0 = random()
			if r0 < 1/6:
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r0 > wnd and dict_1['rw'] == 1:
				r1 = random()
				dict_1['rw'] -= 1
				if r1 < 1/6:
					dict_0["leapad"] += 1
					return (0)
				elif r1 < wnd:
					return (1)
				else: 
					return (0)
			else:
				return (0)
		elif wnd_rr == "reroll 1s":
			r0, r1 = random(), random()
			if r0 < 1/6:
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r0 > 5/6 and r1 < 1/6:
				dict_0["leapad"] += 1
				return (0)
			elif r0 > 5/6 and r1 < wnd:
				return (1)
			else:
				return (0)
		else:
			r0, r1 = random(), random()
			if r0 < 1/6:
				dict_0["leapad"] += 1
				return (0)
			elif r0 < wnd:
				return (1)
			elif r1 < 1/6:
				dict_0["leapad"] += 1
				return (0)
			elif r1 < wnd:
				return (1)
			else:
				return (0)
def save(sav, sv_rr, dict_1):
	if sv_rr == "reroll off":
		r0 = random()
		if r0 > sav and dict_1['rs'] == 1:
			r1 = random()
			dict_1['rs'] -= 1
			if r1 < sav:
				return (0)
			else: 
				return (1)
		elif r0 > sav:
			return (1)
		else:
			return (0)
	elif sv_rr == "reroll 1s":
		r0, r1 = random(), random()

		if r0 > 5/6 and r1 < sav:
			return (0)
		if r0 > sav:
			return (1)
		else:
			return (0)
	else:
		r0, r1 = random(), random()

		if r0 > sav and r1 < sav:
			return (0)
		elif r0 > sav:
			return (1)
		else:
			return (0)
def save2(sv_eap, sv_rr, dict_1):
	if sv_rr == "reroll off":
		r0 = random()
		if r0 > sv_eap and dict_1['rs'] == 1:
			r1 = random()
			dict_1['rs'] -= 1
			if r1 < sv_eap:
				return (0)
			else: 
				return (1)
		elif r0 > sv_eap:
			return (1)
		else:
			return (0)
	elif sv_rr == "reroll 1s":
		r0, r1 = random(), random()

		if r0 > 5/6 and r1 < sv_eap:
			return (0)
		if r0 > sv_eap:
			return (1)
		else:
			return (0)
	else:
		r0, r1 = random(), random()

		if r0 > sv_eap and r1 < sv_eap:
			return (0)
		elif r0 > sv_eap:
			return (1)
		else:
			return (0)
def mw_number(mwo6):
	if mwo6 == "6 no mw":
		return (0)
	elif mwo6 == "6 1 mw":
		return (1)
	elif mwo6 == "6 D3 mw":
		return (dice3())
	elif mwo6 == "6 D6 mw":
		return (dice6())
def damage_mw(mwd, lw, mmw, fnp_mw, mwo6):
	if mmw != 0 and mwd > mmw:
		d = mmw
	else:
		d = mwd

	if fnp_mw == "fnp mw 6":
		for i in range(0, d):
			r2 = random()
			if r2 > 5/6:
				d = d -1
	elif fnp_mw == "fnp mw 5":
		for i in range(0, d):
			r2 = random()
			if r2 > 4/6:
				d = d -1
	elif fnp_mw == "fnp mw 4":
		for i in range(0, d):
			r2 = random()
			if r2 > 3/6:
				d = d -1
	if lw == []:
		lw = []
	else:
		while d > 0:
			if lw == []:
				d = 0
			elif lw[0] > 0:
				lw = [lw[0] - 1] + lw[1:len(lw)]
				d = d - 1
			elif lw[0] == 0:
				lw = lw[1:len(lw)]
	return (lw)
def damage(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp):
	if dam_int != 0:
		d = dam_int
	elif rr_d == "reroll d off":
		if dam_d3 == "d d3":
			d = dice3()
		elif dam_d3 == "d 2d3":
			d = dice3()+dice3()
		elif dam_d3 == "d 3d3":
			d = dice3()+dice3()+dice3()
		elif dam_d6 == "d d6":
			d = dice6()
		elif dam_d6 == "d 2d6":
			d = dice6()+dice6()
	elif rr_d == "reroll d on":
		if dam_d3 == "d d3":
			d0, d1 = dice3(), dice3()
			if d0 > d1:
				d2 = d0
			else:
				d2 = d1
			d = d2
		elif dam_d3 == "d 2d3":
			d0, d1, d2, d3 = dice3(), dice3(), dice3(), dice3()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			if d2 > d3:
				d5 = d2
			else:
				d5 = d3
			d = d4+d5
		elif dam_d3 == "d 3d3":
			d0, d1, d2, d3, d4, d5 = dice3(), dice3(), dice3(), dice3(), dice3(), dice3()
			if d0 > d1:
				d6 = d0
			else:
				d6 = d1
			if d2 > d3:
				d7 = d2
			else:
				d7 = d3
			if d4 > d5:
				d8 = d4
			else:
				d8 = d5
			d = d6+d7+d8
		elif dam_d6 == "d d6":
			d0, d1 = dice6(), dice6()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			d = d4
		elif dam_d6 == "d 2d6":
			d0, d1, d2, d3 = dice6(), dice6(), dice6(), dice6()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			if d2 > d3:
				d5 = d2
			else:
				d5 = d3
			d = d4+d5 

	if dam_min > 1 and d < dam_min:
		d = dam_min

	if dam_add != 0 and d + dam_add <= 0:
		d = 1
	elif dam_add != 0:
		d = dam_add + d

	if fnp == "fnp 6":
		for i in range(0, d):
			r2 = random()
			if r2 > 5/6:
				d = d -1
	elif fnp == "fnp 5":
		for i in range(0, d):
			r2 = random()
			if r2 > 4/6:
				d = d -1
	elif fnp == "fnp 4":
		for i in range(0, d):
			r2 = random()
			if r2 > 3/6:
				d = d -1

	if lw == []:
		lw = []
	elif d_co == 'd carry on':
		while d > 0:
			if lw == []:
				d = 0
			elif lw[0] > 0:
				lw = [lw[0] - 1] + lw[1:len(lw)]
				d = d - 1
			elif lw[0] == 0:
				lw = lw[1:len(lw)]
	elif lw[0] - d > 0:
		lw = [lw[0] - d] + lw[1:len(lw)]
	elif lw[0] - d <= 0:
		lw = lw[1:len(lw)]
	return (lw)
def damage2(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp, ed6):
	if dam_int != 0:
		d = dam_int
	elif rr_d == "reroll d off":
		if dam_d3 == "d d3":
			d = dice3()
		elif dam_d3 == "d 2d3":
			d = dice3()+dice3()
		elif dam_d3 == "d 3d3":
			d = dice3()+dice3()+dice3()
		elif dam_d6 == "d d6":
			d = dice6()
		elif dam_d6 == "d 2d6":
			d = dice6()+dice6()
	elif rr_d == "reroll d on":
		if dam_d3 == "d d3":
			d0, d1 = dice3(), dice3()
			if d0 > d1:
				d2 = d0
			else:
				d2 = d1
			d = d2
		elif dam_d3 == "d 2d3":
			d0, d1, d2, d3 = dice3(), dice3(), dice3(), dice3()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			if d2 > d3:
				d5 = d2
			else:
				d5 = d3
			d = d4+d5
		elif dam_d3 == "d 3d3":
			d0, d1, d2, d3, d4, d5 = dice3(), dice3(), dice3(), dice3(), dice3(), dice3()
			if d0 > d1:
				d6 = d0
			else:
				d6 = d1
			if d2 > d3:
				d7 = d2
			else:
				d7 = d3
			if d4 > d5:
				d8 = d4
			else:
				d8 = d5
			d = d6+d7+d8
		elif dam_d6 == "d d6":
			d0, d1 = dice6(), dice6()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			d = d4
		elif dam_d6 == "d 2d6":
			d0, d1, d2, d3 = dice6(), dice6(), dice6(), dice6()
			if d0 > d1:
				d4 = d0
			else:
				d4 = d1
			if d2 > d3:
				d5 = d2
			else:
				d5 = d3
			d = d4+d5 

	d += ed6

	if dam_min > 1 and d < dam_min:
		d = dam_min

	if dam_add != 0 and d + dam_add <= 0:
		d = 1
	elif dam_add != 0:
		d = dam_add + d

	if fnp == "fnp 6":
		for i in range(0, d):
			r2 = random()
			if r2 > 5/6:
				d = d -1
	elif fnp == "fnp 5":
		for i in range(0, d):
			r2 = random()
			if r2 > 4/6:
				d = d -1
	elif fnp == "fnp 4":
		for i in range(0, d):
			r2 = random()
			if r2 > 3/6:
				d = d -1

	if lw == []:
		lw = []
	elif d_co == 'd carry on':
		while d > 0:
			if lw == []:
				d = 0
			elif lw[0] > 0:
				lw = [lw[0] - 1] + lw[1:len(lw)]
				d = d - 1
			elif lw[0] == 0:
				lw = lw[1:len(lw)]
	elif lw[0] - d > 0:
		lw = [lw[0] - d] + lw[1:len(lw)]
	elif lw[0] - d <= 0:
		lw = lw[1:len(lw)]
	return (lw)	
def start():
	lh, lws, ls, ld, j = [], [], [], [], 0
	bs, blst, exp, exp_int = (7-int(bs_int["text"]))/6, btn_blst["text"], btn_exp["text"], exp_attacks()
	dak, flm, hit_rr, h6iw = btn_dka["text"], btn_flm["text"], def_h_rr(), btn_h6iw["text"]
	wnd, wnd_rr, mmw, mwo6, ed6 = (7-int(w_int["text"]))/6, def_w_rr(), max_mw(), btn_mw6["text"], extra_damage_6()
	sav, sv_rr = (7-int(sv_int["text"]))/6, def_s_rr()
	sv_eap, noe, lw1, ia = (sav + (int(btn_6eap["text"][0:2]))/6), number_of_enemies(), [w()]*number_of_enemies(), intial_attacks()
	dam_int, dam_d3, dam_d6, dam_min, dam_add = int(d_int["text"]), btn_d_d3["text"], btn_d_d6["text"], int(min_d_int["text"]), int(d_add_int["text"])
	rr_d, fnp, fnp_mw, d_co = btn_rr_d["text"], btn_d_fnp["text"], btn_d_fnp_mw["text"], btn_d_co["text"]

	while j < 10000:
		lw, dict_0, dict_1 = lw1, {"lmw": 0, "leapad": 0, "l6hiw":0,}, rr_one()
		if blst == 'blast off':
			attacks = ia
		else:
			attacks = sum(((shots_blast(noe, blst))) for i in range (0, ia))
		hits = sum((hitting(exp, bs, flm, dak, hit_rr, exp_int, h6iw, dict_0, dict_1)) for i in range (0, attacks))
		lh.append(hits+dict_0["l6hiw"])
		wounds = sum((wounding(wnd, wnd_rr, mwo6, dict_0, dict_1)) for i in range(0, hits))
		lws.append(wounds+dict_0["leapad"]+dict_0["l6hiw"])
		saves = sum((save(sav, sv_rr, dict_1)) for i in range(0, wounds+dict_0["l6hiw"]))
		saves2 = sum(save2(sv_eap, sv_rr, dict_1) for i in range(0, dict_0["leapad"]))
		ls.append(saves+saves2)
		mwd = sum(mw_number(mwo6) for i in range(0, dict_0["lmw"]))
		lw = damage_mw(mwd, lw, mmw, fnp_mw, mwo6)
		for i in range(0, saves):
			lw = damage(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp)
		for i in range(0, saves2):
			lw = damage2(lw, dam_int, dam_d3, dam_d6, rr_d, dam_min, dam_add, d_co, fnp, ed6)
		remaining = sum(lw)
		ld.append(remaining)
		j += 1
	avg_hit_int["text"] = round(mean(lh))
	stdev_hit_int["text"] = round(stdev(lh))
	avg_w_int["text"] = round(mean(lws))
	stdev_w_int["text"] = round(stdev(lws))
	avg_sv_int["text"] = round(mean(ls))
	stdev_sv_int["text"] = round(stdev(ls))
	avg_d_int["text"] = round(sum(lw1) - mean(ld))
	stdev_d_int["text"] = round(stdev(ld)) 
	percent_remaining["text"] = f'{min_expect(lw1, ld)} - {max_expect(lw1, ld)}'