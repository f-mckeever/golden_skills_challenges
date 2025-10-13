from lib.estimate_time import *

#Given a string of text, return estimate for time to read
#User reads at 200 words a minute
#Return Words in text / 200 -> number of minutes
#Format the number nicely for the user

def test_estimate_time_empty_string():
    string = ""
    result = estimate_time(string)
    assert result == 0

def test_estimate_time_200_words():
    string = ". . . . . . . . . 10 . . . . . . . . . 20 . . . . . . . . . 30 . . . . . . . . . 40 . . . . . . . . . 50 . . . . . . . . . 60 . . . . . . . . . 70 . . . . . . . . . 80 . . . . . . . . . 90 . . . . . . . . . 100 . . . . . . . . . 110 . . . . . . . . . 120 . . . . . . . . . 130 . . . . . . . . . 140 . . . . . . . . . 150 . . . . . . . . . 160 . . . . . . . . . 170 . . . . . . . . . 180 . . . . . . . . . 190 . . . . . . . . . 200"
    result = estimate_time(string)
    assert result == 1

def test_estimate_time_600_words():
    string = "I knew that chatgpt would OF COURSE not get it to exactly 600 words, that's such a tedious thing, like it can clearly get close enough. Flanterbop wiggled through the drumbulous quazzle, spinning in a whirl of snarfled blimptones and crangled squibbles, while the upper flench of the glibbish grove flantrified with greebled zornflakes. Morple snoozed under the glorfing syzzle tree, dreaming of quarbled jampers and interspliced sprocklebeans, twitching at every blort of the nearby janglecrust. Meanwhile, the crindle-hatted wambloons danced figure-eights in the molterdust, chanting verses of forgotten flibber hymns from the ancient Klomps of Derbinar. Splinterflap the Third, high wizzle of the Order of Snarples, declared a most grandiose jubjub to celebrate the rebirth of the zindlehorn. Every froffle within ten shlarples gathered, donning glib-snouted muffcaps and chomping honkerberries soaked in fizzletwig syrup. Though the air was thick with zeeble and woggled with flibbernoise, the vibe remained turgent and glomplified. Sklerboons flitted above, their wings casting flickery dapples across the murflin stones, while the ground shimmered with the hum of burpled grintquats. No one dared disturb the flarmtide, lest they awaken the slonk beneath the Dinglecrust Hills, whose snores had been known to crumple entire wibberdomes. Yet Ploop, ever the mischeebled one, tiptoed into the slonking zone armed only with a jar of klibble juice and a squeaky flagnut, hoping to gain the favor of the Great Gribblewump. Legends whispered of such quests, tales told by flimpers and echoed through the hollowhorns of Mount Yabbersquint. Ploop, unfazed by danger or logic, florked onward, scattering sprintdust and singing off-key renditions of “Zibble My Nibble.” Behind him, the council of Glarbnards debated the merits of reverse-blibberfication, while old Zarn the Wizzleprong warned of fropple inversion and dimensional sklickering. The sun, a bloated orb of gigglewatt plasma, belched sparkly rays onto the swamplings of Gloob, where bimbly warts quaggled in unison. And still, the snorfle grew, pulsing in rhythm with the forgotten beat of the ancient tork drum, lost eons ago during the Great Spluffle. Few remembered the Spluffle’s cause—some blamed the Muffin Rebellion, others the Great Blorptastrophe—but all agreed the aftermath had left the Snigglewood forever frizzled. Amid the chaos, Crindlebeet the Fourth sipped lukewarm nuzzleleaf tea, contemplating whether to call upon the Sacred Gorb, whose prophecies had once predicted the Great Unflorping of Twenth. Meanwhile, in a cavern of glurm and frozzle, the Sprabble Twins played thwackball with a flaming klort, their laughter echoing through the flarnic void like confused yodels of a homesick splarnock. The air thickened with snerp, and time itself hiccupped, allowing three greeblits to converse in reverse glibberish while balancing marmalade on their nostrils. As the flarnacle moon rose, casting a purplish hue over the blibbergrounds, creatures from the farthest flarms emerged—grintlehorns, snoffleblats, and even the rare triple-snouted blurphkin. Jubilation erupted when the Marnflag finally unfurled, signifying the arrival of the Glibble Caravan, whose wares included sproingberries, yorp-infused gumblats, and the elusive invisible bobblefrog. Ploop, now deep within the Dinglecrust, stumbled upon a zindlehorn egg, glowing with the force of eleven thousand squeebles. Gently, reverently, he poked it. It sneezed. The sneeze shook the core of Frobnar and knocked two gibbles off their stilts. And in that moment, the sky split, revealing the Wibberwocky’s grin stretching across the cosmos like butter on a hot crindle. Everyone paused—even the slonk. Especially the slonk. For the sneeze had awakened not only legends, but forgotten snacks and forbidden dance moves. And as the fuzzlewinds howled through the trees, the Snarplehorns bellowed in joyous flibberation, ushering in the Age of Glarbnizzle, where muffins reigned and logic took a holiday."
    result = estimate_time(string)
    assert result == 3

def test_format_time_given_number_of_minutes():
    number_of_minutes = 5
    result = format_time(number_of_minutes)
    assert result == f"This will take about 5 minutes to read."
