/*
https://www.codewars.com/kata/boardgame-fight-resolve/javascript
Write a function fightResolve that takes the attacking and defending
piece as input parameters, and returns the winning piece. It may be
the case that both the attacking and defending piece belong to the same
player, in which the function must return minus one (-1).

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

function fightResolve(defender, attacker) {
	// Check if the defender and the attacker are uppercase or lowercase
	defenderIsUpper = defender === defender.toUpperCase();
	attackerIsUpper = attacker === attacker.toUpperCase();
	defenderIsLower = defender === defender.toLowerCase();
	attackerIsLower = attacker === attacker.toLowerCase();

	// If both pieces are uppercase or lowercase (i.e., both belong to the\
	// same player), then return -1
	if ( (defenderIsUpper && attackerIsUpper) || (defenderIsLower && attackerIsLower) ) {
		return -1;
	}
	// When the defender and the attacker are of the same type, the attacker wins
	if (defender.toLowerCase() === attacker.toLowerCase()) {
		return attacker;
	}

	// Each character is the "strength" of the piece (character) at the same\
	// index in `defenders`
	const attackers = "apsk";
	const defenders = "ksap";

	// Loop through the above strings: if the attacker is the "strength" of the\
	// defender, then the defender wins; else the attacker wins
	for (let i=0; i<attackers.length; i++) {

		// Check if this defender from `defenders` is the one given as input
		if (defenders[i] === defender.toLowerCase()) {

			// Check if the input attacker is the one the defender is strong\
			// against. If so the defender wins
			if (attackers[i] === attacker.toLowerCase() ) {
				return defender;
			}
			// If the attacker is not the one the defender is strong against,\
			// the attacker wins
			else {
				return attacker;
			}
		}
	}
}


console.log(fightResolve('K', 'a'));
console.log(fightResolve('A', 'a'));
console.log(fightResolve('A', 'p'));
console.log(fightResolve('k', 'P'));
console.log(fightResolve('p', 'A'));
console.log(fightResolve('S', 'P'));
console.log(fightResolve('A', 'K'));
console.log(fightResolve('k', 's'));
console.log(fightResolve('p', 'a'));