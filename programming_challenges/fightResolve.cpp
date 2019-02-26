/*
https://www.codewars.com/kata/boardgame-fight-resolve/cpp
Write a function fightResolve that takes the attacking and defending
piece as input parameters, and returns the winning piece. It may be
the case that both the attacking and defending piece belong to the same
player, in which the function must return zero as a character ('0').

The pieces of Player 1 are represented in lowercase, while the pieces of
Player 2 are uppercase. There are only four types of pieces: archer,
pikeman, swordsamn and knight. The table for the results of each matchup
is the following:

(Attacker→)
(Defender↓)		
				Archer		Pikeman		Swordsman	Knight
Knight			Defender	Attacker	Attacker	Attacker
Swordsman		Attacker	Defender	Attacker	Attacker
Archer			Attacker	Attacker	Defender	Attacker
Pikeman			Attacker	Attacker	Attacker	Defender
*/

#include <cstring>
#include <string>
#include <iostream>
using namespace std;


// This solution has two strings: one with the possible defenders and another with which\
// contains the type of unit each defender is strong against. If the index of the\
// attacker and the defender match in those strings, the defender wins, else the attacker\
// wins
char fightResolve (char defender, char attacker) {

	// If both the defender and the attacker pieces are uppercase or lowercase\
	// it means they are both pieces of the same player. Thus, return '0'
	if ( (isupper(defender) and isupper(attacker)) or (islower(defender) and islower(attacker)) ) {
		return '0';
	}
	// When the matchup is between two pieces of the same type the attacker wins
	if (tolower(defender) == tolower(attacker) ) {
		return attacker;
	}

	// Each character is the "strength" of the piece (character) at the same index in `defenders`
	string attackers = "apsk";
	string defenders = "ksap";

	// Loop through the above strings: if the attacker is the "strength" of the defender,\
	// then the defender wins; else the attacker wins
	for (int i=0; i<4; i++) {
		
		// Check if this defender from `defenders` is the one given as input
		if (defenders[i] == tolower(defender)) {
			
			// Check if the input attacker is the one the defender is strong against. If so\
			// the defender wins
			if (attackers[i] == tolower(attacker)) {
				return defender;
			}
			// If the attacker is not the one the defender is strong against, the attacker wins
			else {
				return attacker;
			}
		}
	}
}


// This implementation uses a switch statement for every type of defender. If the attacker is\
// the one the defender is strong against, then the defender wins, else the attacker wins
char fightResolveV2 (char defender, char attacker) {

	// If both the defender and the attacker pieces are uppercase or lowercase\
	// it means they are both pieces of the same player. Thus, return '0'
	if ( (isupper(defender) and isupper(attacker)) or (islower(defender) and islower(attacker)) ) {
		return -1;
	}
	// When the matchup is between two pieces of the same type the attacker wins
	if (tolower(defender) == tolower(attacker) ) {
		return attacker;
	}

	// Convert the attacker and the defender characters to lowercase to facilitate\
	// comparisons (we still return the character in its correct form, but we use\
	// them lowercase for comparisons since we only care for the type of unit not\
	// whose player the unit belongs to)
	char lowerDef = tolower(defender);
	char lowerAtt = tolower(attacker);

	// Create a switch statement for every type of defender: if the attacker is the one\
	// the defender is strong to, the defender wins; else the attacker wins
	switch (lowerDef) {
		case ('k'):
			if (lowerAtt == 'a') {
				return defender;
			}
			else {
				return attacker;
			}
			break;

		case ('s'):
			if (lowerAtt == 'p') {
				return defender;
			}
			else {
				return attacker;
			}
			break;

		case ('a'):
			if (lowerAtt == 's') {
				return defender;
			}
			else {
				return attacker;
			}
			break;

		case ('p'):
			if (lowerAtt == 'k') {
				return defender;
			}
			else {
				return attacker;
			}
			break;

	}
}

int main() {
	cout << fightResolve('K', 'a') << "\n";
	cout << fightResolve('A', 'a') << "\n";
	cout << fightResolve('A', 'p') << "\n";
	cout << fightResolve('k', 'P') << "\n";
	cout << fightResolve('p', 'A') << "\n";
	cout << fightResolve('S', 'P') << "\n";
	cout << fightResolve('A', 'K') << "\n";
	cout << fightResolve('k', 's') << "\n";
	cout << fightResolve('p', 'a') << "\n";
}