import random
import getpass
import os
import sys
import time
import json
import string
import math
import re
from builtins import print as printf
import pprint
import difflib
SOD=":( \nYour OS Has Crashed due to RAM overload. Rebooting..."
fromcrash=False
gunch_bucks = 0
ui_colors = {
    "default": "\033[0m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m"
}
novel_installed = False
novel_total_cmds = 0
novel_cmd_counts = {}
novel_last_new_cmd = None
deepflow_active = False
centerflow_active = False
choreflow_active = False
chore = False
current_ui_color = "default"
boot_time=time.time()
command_history=[]
godstat=False
userpasses={"chronos": ""}
HIDDEN_USERS=["chronos"]
exitstatus="n"
continuetest=True
logged_out=True
mathtest="true"
userwelcomed=False
terminalstat="up"
endwords="I like chicken"
modulecount=0
modules=[]
files={}
notes=[]
group_peeps=[]
user=""
user_input_username=""
user_input_password=""
usercount=0
exit=False
delos = False
DATA_DIR="osdata"
USER_FILE=os.path.join(DATA_DIR,"users.json")
MODULE_FILE=os.path.join(DATA_DIR,"modules.json")
FILES_FILE=os.path.join(DATA_DIR,"files.json")
SETTINGS_FILE=os.path.join(DATA_DIR,"settings.json")
NOTES_FILE = os.path.join(DATA_DIR, "notes.json")
LOGIN_COOKIE_FILE = os.path.join(DATA_DIR, "login_cookie.json")
cusswords = ["fuck", "shit", "hell", "damn", "ass"]
DICT_FILE = "dictionary.json"
elements = {
'Hydrogen': { 'Number': 1, 'Symbol': 'H' },
'Helium': { 'Number': 2, 'Symbol': 'He' },
'Lithium': { 'Number': 3, 'Symbol': 'Li' },
'Beryllium': { 'Number': 4, 'Symbol': 'Be' },
'Boron': { 'Number': 5, 'Symbol': 'B' },
'Carbon': { 'Number': 6, 'Symbol': 'C' },
'Nitrogen': { 'Number': 7, 'Symbol': 'N' },
'Oxygen': { 'Number': 8, 'Symbol': 'O' },
'Fluorine': { 'Number': 9, 'Symbol': 'F' },
'Neon': { 'Number': 10, 'Symbol': 'Ne' },
'Sodium': { 'Number': 11, 'Symbol': 'Na' },
'Magnesium': { 'Number': 12, 'Symbol': 'Mg' },
'Aluminium': { 'Number': 13, 'Symbol': 'Al' },
'Silicon': { 'Number': 14, 'Symbol': 'Si' },
'Phosphorus': { 'Number': 15, 'Symbol': 'P' },
'Sulfur': { 'Number': 16, 'Symbol': 'S' },
'Chlorine': { 'Number': 17, 'Symbol': 'Cl' },
'Argon': { 'Number': 18, 'Symbol': 'Ar' },
'Potassium': { 'Number': 19, 'Symbol': 'K' },
'Calcium': { 'Number': 20, 'Symbol': 'Ca' },
'Scandium': { 'Number': 21, 'Symbol': 'Sc' },
'Titanium': { 'Number': 22, 'Symbol': 'Ti' },
'Vanadium': { 'Number': 23, 'Symbol': 'V' },
'Chromium': { 'Number': 24, 'Symbol': 'Cr' },
'Manganese': { 'Number': 25, 'Symbol': 'Mn' },
'Iron': { 'Number': 26, 'Symbol': 'Fe' },
'Cobalt': { 'Number': 27, 'Symbol': 'Co' },
'Nickel': { 'Number': 28, 'Symbol': 'Ni' },
'Copper': { 'Number': 29, 'Symbol': 'Cu' },
'Zinc': { 'Number': 30, 'Symbol': 'Zn' },
'Gallium': { 'Number': 31, 'Symbol': 'Ga' },
'Germanium': { 'Number': 32, 'Symbol': 'Ge' },
'Arsenic': { 'Number': 33, 'Symbol': 'As' },
'Selenium': { 'Number': 34, 'Symbol': 'Se' },
'Bromine': { 'Number': 35, 'Symbol': 'Br' },
'Krypton': { 'Number': 36, 'Symbol': 'Kr' },
'Rubidium': { 'Number': 37, 'Symbol': 'Rb' },
'Strontium': { 'Number': 38, 'Symbol': 'Sr' },
'Yttrium': { 'Number': 39, 'Symbol': 'Y' },
'Zirconium': { 'Number': 40, 'Symbol': 'Zr' },
'Niobium': { 'Number': 41, 'Symbol': 'Nb' },
'Molybdenum': { 'Number': 42, 'Symbol': 'Mo' },
'Technetium': { 'Number': 43, 'Symbol': 'Tc' },
'Ruthenium': { 'Number': 44, 'Symbol': 'Ru' },
'Rhodium': { 'Number': 45, 'Symbol': 'Rh' },
'Palladium': { 'Number': 46, 'Symbol': 'Pd' },
'Silver': { 'Number': 47, 'Symbol': 'Ag' },
'Cadmium': { 'Number': 48, 'Symbol': 'Cd' },
'Indium': { 'Number': 49, 'Symbol': 'In' },
'Tin': { 'Number': 50, 'Symbol': 'Sn' },
'Antimony': { 'Number': 51, 'Symbol': 'Sb' },
'Tellurium': { 'Number': 52, 'Symbol': 'Te' },
'Iodine': { 'Number': 53, 'Symbol': 'I' },
'Xenon': { 'Number': 54, 'Symbol': 'Xe' },
'Cesium': { 'Number': 55, 'Symbol': 'Cs' },
'Barium': { 'Number': 56, 'Symbol': 'Ba' },
'Lanthanum': { 'Number': 57, 'Symbol': 'La' },
'Cerium': { 'Number': 58, 'Symbol': 'Ce' },
'Praseodymium': { 'Number': 59, 'Symbol': 'Pr' },
'Neodymium': { 'Number': 60, 'Symbol': 'Nd' },
'Promethium': { 'Number': 61, 'Symbol': 'Pm' },
'Samarium': { 'Number': 62, 'Symbol': 'Sm' },
'Europium': { 'Number': 63, 'Symbol': 'Eu' },
'Gadolinium': { 'Number': 64, 'Symbol': 'Gd' },
'Terbium': { 'Number': 65, 'Symbol': 'Tb' },
'Dysprosium': { 'Number': 66, 'Symbol': 'Dy' },
'Holmium': { 'Number': 67, 'Symbol': 'Ho' },
'Erbium': { 'Number': 68, 'Symbol': 'Er' },
'Thulium': { 'Number': 69, 'Symbol': 'Tm' },
'Ytterbium': { 'Number': 70, 'Symbol': 'Yb' },
'Lutetium': { 'Number': 71, 'Symbol': 'Lu' },
'Hafnium': { 'Number': 72, 'Symbol': 'Hf' },
'Tantalum': { 'Number': 73, 'Symbol': 'Ta' },
'Tungsten': { 'Number': 74, 'Symbol': 'W' },
'Rhenium': { 'Number': 75, 'Symbol': 'Re' },
'Osmium': { 'Number': 76, 'Symbol': 'Os' },
'Iridium': { 'Number': 77, 'Symbol': 'Ir' },
'Platinum': { 'Number': 78, 'Symbol': 'Pt' },
'Gold': { 'Number': 79, 'Symbol': 'Au' },
'Mercury': { 'Number': 80, 'Symbol': 'Hg' },
'Thallium': { 'Number': 81, 'Symbol': 'Tl' },
'Lead': { 'Number': 82, 'Symbol': 'Pb' },
'Bismuth': { 'Number': 83, 'Symbol': 'Bi' },
'Polonium': { 'Number': 84, 'Symbol': 'Po' },
'Astatine': { 'Number': 85, 'Symbol': 'At' },
'Radon': { 'Number': 86, 'Symbol': 'Rn' },
'Francium': { 'Number': 87, 'Symbol': 'Fr' },
'Radium': { 'Number': 88, 'Symbol': 'Ra' },
'Actinium': { 'Number': 89, 'Symbol': 'Ac' },
'Thorium': { 'Number': 90, 'Symbol': 'Th' },
'Protactinium': { 'Number': 91, 'Symbol': 'Pa' },
'Uranium': { 'Number': 92, 'Symbol': 'U' },
'Neptunium': { 'Number': 93, 'Symbol': 'Np' },
'Plutonium': { 'Number': 94, 'Symbol': 'Pu' },
'Americium': { 'Number': 95, 'Symbol': 'Am' },
'Curium': { 'Number': 96, 'Symbol': 'Cm' },
'Berkelium': { 'Number': 97, 'Symbol': 'Bk' },
'Californium': { 'Number': 98, 'Symbol': 'Cf' },
'Einsteinium': { 'Number': 99, 'Symbol': 'Es' },
'Fermium': { 'Number': 100, 'Symbol': 'Fm' },
'Mendelevium': { 'Number': 101, 'Symbol': 'Md' },
'Nobelium': { 'Number': 102, 'Symbol': 'No' },
'Lawrencium': { 'Number': 103, 'Symbol': 'Lr' },
'Rutherfordium': { 'Number': 104, 'Symbol': 'Rf' },
'Dubnium': { 'Number': 105, 'Symbol': 'Db' },
'Seaborgium': { 'Number': 106, 'Symbol': 'Sg' },
'Bohrium': { 'Number': 107, 'Symbol': 'Bh' },
'Hassium': { 'Number': 108, 'Symbol': 'Hs' },
'Meitnerium': { 'Number': 109, 'Symbol': 'Mt' },
'Darmstadtium': { 'Number': 110, 'Symbol': 'Ds' },
'Roentgenium': { 'Number': 111, 'Symbol': 'Rg' },
'Copernicium': { 'Number': 112, 'Symbol': 'Cn' },
'Nihonium': { 'Number': 113, 'Symbol': 'Nh' },
'Flerovium': { 'Number': 114, 'Symbol': 'Fl' },
'Moscovium': { 'Number': 115, 'Symbol': 'Mc' },
'Livermorium': { 'Number': 116, 'Symbol': 'Lv' },
'Tennessine': { 'Number': 117, 'Symbol': 'Ts' },
'Oganesson': { 'Number': 118, 'Symbol': 'Og' }
}
DEFAULT_DICT = {
"abbey": ["(N) A monastery or convent building used by a religious community", "(N) The community of monks or nuns living in such a place"],
"abate": ["(V) To lessen in intensity or amount", "(V) To diminish or reduce something harmful"],
"abbey": ["(N) A monastery or convent building used by a religious community", "(N) The community of monks or nuns living in such a place"],
"abhor": ["(V) To regard with extreme disgust or hatred", "(V) To feel intense aversion toward"],
"abide": ["(V) To accept or tolerate something", "(V) To remain or continue in a place"],
"abjure": ["(V) To formally renounce a belief or claim", "(V) To reject something under oath"],
"abound": ["(V) To exist in large numbers or amounts", "(V) To be plentiful or abundant"],
"absolve": ["(V) To free someone from guilt or blame", "(V) To release from an obligation or duty"],
"accede": ["(V) To agree to a request or demand", "(V) To assume a position or office"],
"acclaim": ["(V) To praise enthusiastically and publicly", "(N) Loud approval or applause"],
"acclimate": ["(V) To adjust to a new climate or environment", "(V) To become accustomed to new conditions"],
"accretion": ["(N) A gradual buildup of layers or matter", "(N) Growth by accumulation"],
"acerbic": ["(Adj) Sharp or biting in tone or taste", "(Adj) Harshly critical or sarcastic"],
"acorn": ["(N) The nut of an oak tree", "(N) A seed that grows into an oak"],
"acorny": ["(Adj) Resembling or suggestive of an acorn", "(Adj) Having a nut-like shape or quality"],
"acrid": ["(Adj) Having a strong, unpleasantly sharp smell or taste", "(Adj) Harsh or bitter in tone"],
"acuity": ["(N) Sharpness of perception or vision", "(N) Keenness of thought or understanding"],
"acumen": ["(N) Keen insight or shrewdness", "(N) The ability to make good judgments quickly"],
"acumenous": ["(Adj) Having sharp mental insight", "(Adj) Highly perceptive or astute"],
"adage": ["(N) A traditional saying expressing a general truth", "(N) A proverb passed down through generations"],
"adamant": ["(Adj) Refusing to be persuaded", "(Adj) Firm and unyielding in attitude"],
"adduce": ["(V) To cite as evidence or proof", "(V) To offer an argument or example"],
"adept": ["(Adj) Highly skilled or proficient", "(N) A person who is very skilled at something"],
"adhere": ["(V) To stick firmly to a surface", "(V) To follow a rule or belief closely"],
"adjudge": ["(V) To consider or declare judicially", "(V) To award or assign formally"],
"admonish": ["(V) To warn or reprimand firmly", "(V) To advise or urge earnestly"],
"adobe": ["(N) A brick made of sun-dried clay", "(N) A building constructed from such bricks"],
"adorn": ["(V) To decorate or add beauty to", "(V) To enhance with ornaments or details"],
"adroit": ["(Adj) Skillful and clever, especially with the hands or mind", "(Adj) Resourceful in handling situations"],
"adulate": ["(V) To praise excessively or slavishly", "(V) To flatter in an exaggerated manner"],
"affable": ["(Adj) Friendly and easy to talk to", "(Adj) Warm and pleasant in manner"],
"affinity": ["(N) A natural liking or attraction", "(N) A similarity or connection between things"],
"affix": ["(V) To attach or fasten something", "(V) To add a signature, stamp, or label"],
"affixation": ["(N) The act of attaching something", "(N) A linguistic element added to a word"],
"afflict": ["(V) To cause pain or suffering", "(V) To trouble or distress deeply"],
"affluent": ["(Adj) Wealthy and prosperous", "(Adj) Having an abundance of resources"],
"afforest": ["(V) To plant trees in an area without forest", "(V) To convert land into woodland"],
"aggrandize": ["(V) To increase the power or wealth of something", "(V) To exaggerate the importance of something"],
"aggrieve": ["(V) To cause distress or resentment", "(V) To treat unfairly or unjustly"],
"agile": ["(Adj) Able to move quickly and easily", "(Adj) Mentally quick and resourceful"],
"ail": ["(V) To suffer from illness or discomfort", "(V) To trouble or afflict"],
"ailment": ["(N) A minor illness or disorder", "(N) A condition causing discomfort"],
"ailurophile": ["(N) A person who loves cats", "(N) Someone fond of felines"],
"aimless": ["(Adj) Without purpose or direction", "(Adj) Lacking clear goals"],
"airborne": ["(Adj) Carried through the air", "(Adj) In flight or lifted off the ground"],
"aisle": ["(N) A passage between rows of seats or shelves", "(N) A walkway in a church or store"],
"alacrity": ["(N) Cheerful readiness or eagerness", "(N) Prompt and willing response"],
"alembic": ["(N) A distilling apparatus", "(N) Something that refines or purifies"],
"alert": ["(Adj) Fully aware and attentive", "(N) A warning of danger"],
"alight": ["(V) To descend from the air and land", "(V) To step down from a vehicle"],
"alike": ["(Adj) Similar in appearance or nature", "(Adv) In the same manner"],
"alimony": ["(N) Financial support paid to a former spouse", "(N) Court-ordered maintenance after divorce"],
"allay": ["(V) To reduce fear or worry", "(V) To calm or soothe"],
"allege": ["(V) To claim something without proof", "(V) To assert as a fact"],
"alleviate": ["(V) To reduce pain or suffering", "(V) To make a problem easier to bear"],
"allot": ["(V) To distribute or assign portions", "(V) To allocate resources or time"],
"allude": ["(V) To refer indirectly to something", "(V) To hint at without stating explicitly"],
"allusive": ["(Adj) Containing indirect references", "(Adj) Suggestive rather than explicit"],
"almond": ["(N) An edible nut with a hard shell", "(N) The tree that produces these nuts"],
"aloof": ["(Adj) Emotionally distant or reserved", "(Adj) Detached or uninvolved"],
"altercate": ["(V) To argue or dispute loudly", "(V) To engage in a heated disagreement"],
"amalgamate": ["(V) To combine into a unified whole", "(V) To merge organizations or elements"],
"amass": ["(V) To gather or accumulate over time", "(V) To collect in large quantities"],
"amateur": ["(N) A person who engages in an activity for pleasure, not pay", "(Adj) Lacking professional skill"],
"amaze": ["(V) To fill with wonder or surprise", "(V) To astonish greatly"],
"amble": ["(V) To walk slowly and casually", "(V) To move at an easy, relaxed pace"],
"ambit": ["(N) The scope or extent of something", "(N) A boundary or limit"],
"ambrosial": ["(Adj) Exceptionally pleasing to taste or smell", "(Adj) Divine or heavenly in quality"],
"amiable": ["(Adj) Friendly and pleasant", "(Adj) Good-natured and likable"],
"amicable": ["(Adj) Characterized by friendliness and goodwill", "(Adj) Peaceful in tone or resolution"],
"amiss": ["(Adj) Not quite right or out of place", "(Adv) Improperly or incorrectly"],
"amorphous": ["(Adj) Without a clear shape or form", "(Adj) Lacking structure or definition"],
"amphora": ["(N) A tall ancient jar with two handles", "(N) A vessel used for storing wine or oil"],
"ample": ["(Adj) More than enough; plentiful", "(Adj) Generous in size or amount"],
"amuse": ["(V) To entertain or cause laughter", "(V) To occupy pleasantly"],
"anaclastic": ["(Adj) Curved or bent by refraction", "(Adj) Relating to optical distortion"],
"anchorite": ["(N) A religious recluse", "(N) Someone living in seclusion for spiritual reasons"],
"ancient": ["(Adj) Very old or from long ago", "(N) A person who lived in ancient times"],
"anemology": ["(N) The study of wind", "(N) A branch of meteorology focused on air movement"],
"anew": ["(Adv) Once more or again", "(Adv) In a new or different way"],
"angelic": ["(Adj) Resembling an angel in purity or kindness", "(Adj) Exceptionally good or innocent"],
"anger": ["(N) A strong feeling of displeasure", "(V) To make someone upset or annoyed"],
"anguish": ["(N) Severe mental or physical pain", "(V) To suffer extreme distress"],
"animosity": ["(N) Strong hostility or resentment", "(N) Deep-seated dislike"],
"animus": ["(N) Hostile attitude or ill will", "(N) Motivation or intent behind actions"],
"anklet": ["(N) A bracelet worn around the ankle", "(N) A decorative ankle ornament"],
"annex": ["(V) To add or attach something, especially territory", "(N) A building added to a main structure"],
"annoy": ["(V) To irritate or bother", "(V) To cause slight anger or frustration"],
"annul": ["(V) To declare something invalid", "(V) To cancel or abolish legally"],
"anodyne": ["(Adj) Not likely to offend; bland", "(N) A pain-relieving medicine"],
"anoint": ["(V) To apply oil ceremonially", "(V) To choose or bless for a role"],
"anomalous": ["(Adj) Deviating from the norm", "(Adj) Irregular or unusual"],
"antagonize": ["(V) To provoke hostility", "(V) To make someone unfriendly or opposed"],
"antecedent": ["(N) Something that comes before another", "(N) A word replaced by a pronoun"],
"anthelion": ["(N) A bright spot opposite the sun", "(N) An atmospheric optical phenomenon"],
"antipodal": ["(Adj) Situated on opposite sides of the earth", "(Adj) Completely opposite in nature"],
"antiphony": ["(N) Call-and-response singing", "(N) Alternating musical phrases"],
"antipyretic": ["(N) A fever-reducing drug", "(Adj) Reducing fever"],
"antler": ["(N) A branched horn on a deer", "(N) A bony growth shed annually"],
"anxiety": ["(N) A feeling of worry or unease", "(N) A nervous disorder marked by fear"],
"apathy": ["(N) Lack of interest or emotion", "(N) Indifference toward important matters"],
"aperture": ["(N) An opening or hole", "(N) The adjustable opening in a camera lens"],
"apex": ["(N) The highest point or peak", "(N) The tip or summit of something"],
"aphorism": ["(N) A concise statement of truth", "(N) A witty or wise saying"],
"aphelion": ["(N) The point in orbit farthest from the sun", "(N) A celestial body’s most distant orbital point"],
"apogee": ["(N) The highest or most successful point", "(N) The point in orbit farthest from Earth"],
"apothegm": ["(N) A short, instructive saying", "(N) A concise remark expressing a principle"],
"appanage": ["(N) A privilege or property granted by rank", "(N) A rightful inheritance"],
"appetite": ["(N) A desire for food", "(N) A craving or longing for something"],
"apposite": ["(Adj) Highly appropriate or relevant", "(Adj) Aptly suited to the situation"],
"apprise": ["(V) To inform or notify", "(V) To give notice to someone"],
"arbiter": ["(N) A judge or decision-maker", "(N) Someone with authority to settle disputes"],
"arbor": ["(N) A shaded garden structure", "(N) A framework supporting climbing plants"],
"arcane": ["(Adj) Understood by few; mysterious", "(Adj) Secret or obscure in meaning"],
"arcanum": ["(N) A deep secret or mystery", "(N) A hidden or specialized knowledge"],
"archer": ["(N) A person who shoots with a bow", "(N) A skilled bowman"],
"ardent": ["(Adj) Passionate or enthusiastic", "(Adj) Burning with intense feeling"],
"ardor": ["(N) Intense passion or enthusiasm", "(N) Strong devotion or eagerness"],
"arena": ["(N) A place for sports or performances", "(N) A field of conflict or activity"],
"argillaceous": ["(Adj) Containing clay", "(Adj) Made of or resembling clay"],
"argosy": ["(N) A large merchant ship", "(N) A rich supply or abundance"],
"arid": ["(Adj) Extremely dry", "(Adj) Lacking interest or excitement"],
"armada": ["(N) A large fleet of ships", "(N) A powerful naval force"],
"armillary": ["(Adj) Relating to celestial spheres", "(N) A model of the heavens"],
"armistice": ["(N) A temporary peace agreement", "(N) A suspension of hostilities"],
"aromatic": ["(Adj) Having a pleasant smell", "(Adj) Fragrant or spicy"],
"array": ["(N) An impressive display or range", "(V) To arrange or dress neatly"],
"arrogant": ["(Adj) Having an exaggerated sense of self-importance", "(Adj) Proud in an unpleasant way"],
"artful": ["(Adj) Clever or skillful", "(Adj) Deceptive or crafty"],
"articulate": ["(Adj) Able to express ideas clearly", "(V) To speak distinctly"],
"artifice": ["(N) Clever trick or device", "(N) Deceptive or ingenious strategy"],
"ascend": ["(V) To move upward", "(V) To rise to a higher position"],
"ascendancy": ["(N) A position of dominance", "(N) Controlling influence"],
"ascetic": ["(Adj) Practicing strict self-discipline", "(N) A person who lives a simple, austere life"],
"ascribe": ["(V) To attribute something to a cause", "(V) To credit a source or origin"],
"aseptic": ["(Adj) Free from contamination", "(Adj) Sterile or disinfected"],
"ashen": ["(Adj) Pale or gray like ash", "(Adj) Drained of color from shock"],
"askance": ["(Adv) With suspicion or disapproval", "(Adv) With a sideways glance"],
"askew": ["(Adj) Not straight or level", "(Adv) Crookedly or unevenly"],
"aspire": ["(V) To strive toward a goal", "(V) To have ambitious hopes"],
"assail": ["(V) To attack violently", "(V) To criticize strongly"],
"assailant": ["(N) A person who attacks", "(N) Someone who commits an assault"],
"assay": ["(V) To test the quality of a substance", "(N) An analysis of metal content"],
"assent": ["(V) To agree or approve", "(N) Official agreement"],
"assert": ["(V) To state firmly", "(V) To defend or uphold a claim"],
"assiduous": ["(Adj) Showing great care and perseverance", "(Adj) Diligent and thorough"],
"assort": ["(V) To categorize or group", "(V) To arrange into types"],
"assuage": ["(V) To ease pain or distress", "(V) To satisfy a desire"],
"aster": ["(N) A star-shaped flower", "(N) A plant of the daisy family"],
"astonish": ["(V) To surprise greatly", "(V) To amaze or impress"],
"astrolabe": ["(N) An ancient astronomical instrument", "(N) A device for measuring celestial positions"],
"astute": ["(Adj) Having sharp judgment", "(Adj) Clever and perceptive"],
"atonal": ["(Adj) Lacking a musical key", "(Adj) Not based on traditional harmony"],
"atonement": ["(N) Making amends for wrongdoing", "(N) Reconciliation or compensation"],
"atrophy": ["(V) To waste away from lack of use", "(N) A decline in effectiveness"],
"attain": ["(V) To achieve or reach", "(V) To succeed in accomplishing"],
"attest": ["(V) To provide evidence or proof", "(V) To certify formally"],
"attune": ["(V) To bring into harmony", "(V) To adjust to a situation"],
"audacious": ["(Adj) Bold and daring", "(Adj) Showing a willingness to take risks"],
"audacity": ["(N) Bold or daring behavior", "(N) Rude or disrespectful boldness"],
"audible": ["(Adj) Able to be heard", "(Adj) Loud enough to be perceived by the ear"],
"augment": ["(V) To increase or enlarge", "(V) To make something greater in size or value"],
"augur": ["(V) To predict or foretell", "(V) To be a sign of a future outcome"],
"augury": ["(N) A sign or omen of what will happen", "(N) The practice of interpreting omens"],
"august": ["(Adj) Inspiring respect or admiration", "(Adj) Grand or dignified in appearance"],
"auspice": ["(N) Support or guidance", "(N) A sign or omen indicating future success"],
"austere": ["(Adj) Strict or severe in manner", "(Adj) Plain or without decoration"],
"authentic": ["(Adj) Genuine or real", "(Adj) True to its origins"],
"autarky": ["(N) Economic independence or self-sufficiency", "(N) A system where a nation is self-reliant"],
"autochthonous": ["(Adj) Indigenous or native to a place", "(Adj) Formed in the place where found"],
"autonomy": ["(N) Self-government or independence", "(N) Freedom to make one’s own decisions"],
"autotomy": ["(N) The ability of an animal to shed a body part", "(N) Self-amputation as a defense mechanism"],
"avarice": ["(N) Extreme greed for wealth", "(N) An insatiable desire for gain"],
"avert": ["(V) To turn away or aside", "(V) To prevent something undesirable from happening"],
"avifauna": ["(N) The birds of a particular region", "(N) A collection of bird species in an area"],
"avow": ["(V) To declare openly and boldly", "(V) To acknowledge something publicly"],
"azure": ["(Adj) Bright blue like a clear sky", "(N) A deep sky-blue color"],
"baccate": ["(Adj) Berry-like or bearing berries", "(Adj) Resembling a small round fruit"],
"bailiwick": ["(N) One’s area of expertise or authority", "(N) A district under a bailiff’s jurisdiction"],
"bailment": ["(N) The delivery of goods for safekeeping", "(N) A legal relationship involving temporary possession"],
"baleful": ["(Adj) Threatening harm or evil", "(Adj) Ominous or menacing in appearance"],
"balmy": ["(Adj) Mild and pleasant", "(Adj) Soothing or refreshing"],
"balneal": ["(Adj) Relating to baths or bathing", "(Adj) Used for therapeutic bathing"],
"balustrade": ["(N) A railing supported by balusters", "(N) A protective barrier on balconies or stairs"],
"banal": ["(Adj) Lacking originality; boring", "(Adj) Overused to the point of dullness"],
"bandy": ["(V) To exchange words casually", "(V) To toss back and forth"],
"banter": ["(N) Playful teasing conversation", "(V) To joke or tease lightly"],
"barcarolle": ["(N) A Venetian boat song", "(N) A musical piece in a lilting rhythm"],
"barge": ["(N) A flat-bottomed boat for transporting goods", "(V) To move clumsily or forcefully"],
"barley": ["(N) A cereal grain used in food and drink", "(N) A hardy grass cultivated for its seeds"],
"baroque": ["(Adj) Highly ornate or extravagant", "(N) A European artistic style of the 17th century"],
"barrow": ["(N) A wheelbarrow", "(N) An ancient burial mound"],
"barycenter": ["(N) The center of mass of two orbiting bodies", "(N) The balance point between celestial objects"],
"bastille": ["(N) A fortress or prison", "(N) A place of confinement"],
"bastion": ["(N) A fortified stronghold", "(N) A person or institution strongly defending principles"],
"bathe": ["(V) To wash in water", "(V) To immerse or soak something"],
"bathyscaphe": ["(N) A deep-diving submersible vessel", "(N) A craft designed for underwater exploration"],
"bauxite": ["(N) The primary ore of aluminum", "(N) A clay-like mineral rich in alumina"],
"beacon": ["(N) A guiding or warning light", "(N) A source of inspiration or guidance"],
"beadle": ["(N) A minor parish officer", "(N) A ceremonial church official"],
"beefy": ["(Adj) Muscular or heavily built", "(Adj) Substantial or robust"],
"befall": ["(V) To happen to someone", "(V) To occur unexpectedly"],
"befit": ["(V) To be appropriate for", "(V) To suit or match properly"],
"befuddle": ["(V) To confuse or perplex", "(V) To make someone unable to think clearly"],
"beget": ["(V) To produce or bring about", "(V) To father or generate offspring"],
"begrudge": ["(V) To envy someone’s possession or enjoyment", "(V) To give reluctantly"],
"beguile": ["(V) To charm or enchant deceptively", "(V) To trick or mislead"],
"behemoth": ["(N) Something enormous and powerful", "(N) A creature of immense size"],
"behold": ["(V) To see or observe", "(V) To look upon with attention"],
"belabor": ["(V) To over-explain or dwell on excessively", "(V) To attack verbally"],
"belated": ["(Adj) Coming later than expected", "(Adj) Delayed or overdue"],
"belay": ["(V) To secure a rope in climbing", "(V) To stop or cancel an action"],
"belch": ["(V) To emit gas noisily from the stomach", "(V) To erupt or gush forth"],
"beleaguer": ["(V) To surround with difficulties", "(V) To harass persistently"],
"belie": ["(V) To give a false impression of", "(V) To contradict or misrepresent"],
"belittle": ["(V) To make someone seem unimportant", "(V) To speak of something as trivial"],
"bellicose": ["(Adj) Aggressive and eager to fight", "(Adj) Demonstrating hostility"],
"belligerent": ["(Adj) Hostile and combative", "(N) A nation or person engaged in conflict"],
"benediction": ["(N) A blessing or prayer", "(N) An expression of good wishes"],
"benign": ["(Adj) Gentle and kind", "(Adj) Not harmful or malignant"],
"benison": ["(N) A blessing or benediction", "(N) Something that brings good fortune"],
"benthic": ["(Adj) Relating to the bottom of a sea or lake", "(Adj) Living on or near the ocean floor"],
"bequeath": ["(V) To leave property by will", "(V) To pass something on to future generations"],
"berate": ["(V) To scold harshly", "(V) To criticize angrily"],
"bereft": ["(Adj) Deprived of something needed", "(Adj) Sorrowful from loss"],
"berth": ["(N) A sleeping place on a ship or train", "(V) To dock a vessel"],
"beseech": ["(V) To beg urgently", "(V) To implore earnestly"],
"beset": ["(V) To trouble persistently", "(V) To surround or attack from all sides"],
"besmirch": ["(V) To damage someone’s reputation", "(V) To make something dirty or stained"],
"bestow": ["(V) To give as a gift or honor", "(V) To confer formally"],
"betide": ["(V) To happen or occur", "(V) To befall someone"],
"bevel": ["(N) A sloping edge", "(V) To cut at an angle"],
"bewail": ["(V) To express deep sorrow", "(V) To lament loudly"],
"bewilder": ["(V) To confuse completely", "(V) To puzzle or perplex"],
"bibelot": ["(N) A small decorative object", "(N) A trinket or curiosity"],
"bifacial": ["(Adj) Having two faces or surfaces", "(Adj) Worked on both sides (archaeology)"],
"bifurcate": ["(V) To divide into two branches", "(Adj) Forked or split in two"],
"bilateral": ["(Adj) Involving two sides", "(Adj) Affecting both parties equally"],
"bilk": ["(V) To cheat or defraud", "(V) To evade payment"],
"binnacle": ["(N) A housing for a ship’s compass", "(N) A protective stand for navigation instruments"],
"biogenic": ["(Adj) Produced by living organisms", "(Adj) Resulting from biological processes"],
"biotite": ["(N) A dark mica mineral", "(N) A common component of igneous rocks"],
"birefringent": ["(Adj) Splitting light into two rays", "(Adj) Exhibiting double refraction"],
"blanch": ["(V) To whiten by removing color", "(V) To briefly boil food to loosen skins"],
"blandishment": ["(N) A flattering or coaxing remark", "(N) Words used to persuade gently"],
"blare": ["(V) To make a loud, harsh sound", "(N) A noisy, piercing blast"],
"blaspheme": ["(V) To speak irreverently about sacred things", "(V) To insult something holy"],
"blatant": ["(Adj) Obvious and offensive", "(Adj) Done openly without shame"],
"blaze": ["(V) To burn brightly", "(N) A strong flame or fire"],
"blazon": ["(V) To display prominently", "(N) A coat of arms"],
"bleak": ["(Adj) Cold and unwelcoming", "(Adj) Without hope or encouragement"],
"bleb": ["(N) A small blister or bubble", "(N) A raised fluid-filled spot"],
"bleary": ["(Adj) Blurred or dimmed from fatigue", "(Adj) Unclear in appearance"],
"blight": ["(N) A disease harming plants", "(V) To ruin or spoil"],
"blithe": ["(Adj) Cheerful and carefree", "(Adj) Showing casual indifference"],
"blitheful": ["(Adj) Full of cheerfulness", "(Adj) Joyous and lighthearted"],
"blizzard": ["(N) A severe snowstorm", "(N) A storm with strong winds and heavy snow"],
"bloat": ["(V) To swell or puff up", "(V) To expand excessively"],
"blockade": ["(N) A barrier preventing movement", "(V) To seal off a place"],
"blossom": ["(N) A flower or bloom", "(V) To develop or flourish"],
"blossomwood": ["(N) Wood from flowering trees", "(N) A poetic term for spring forests"],
"blot": ["(N) A stain or blemish", "(V) To soak up or remove liquid"],
"bludgeon": ["(V) To beat with a heavy object", "(N) A thick, heavy club"],
"bluff": ["(V) To deceive by pretending confidence", "(N) A steep cliff"],
"blunder": ["(V) To make a careless mistake", "(N) A foolish error"],
"blunt": ["(Adj) Not sharp", "(Adj) Direct to the point of rudeness"],
"bluster": ["(V) To speak loudly and boastfully", "(N) Noisy, aggressive talk"],
"bog": ["(N) A wet, marshy area", "(V) To sink or become stuck"],
"bogong": ["(N) A type of Australian moth", "(N) A mountain in southeastern Australia"],
"bogwood": ["(N) Wood preserved in peat bogs", "(N) Dark, waterlogged timber"],
"boisterous": ["(Adj) Noisy, energetic, and cheerful", "(Adj) Rowdy or unrestrained"],
"bolide": ["(N) A large meteor that explodes in the atmosphere", "(N) A brilliant fireball"],
"bolster": ["(V) To support or strengthen", "(N) A long, firm pillow"],
"bombastic": ["(Adj) Overly inflated in speech", "(Adj) High-sounding but with little meaning"],
"bonnet": ["(N) A hat tied under the chin", "(N) The hood of a car"],
"boon": ["(N) A helpful or beneficial thing", "(N) A blessing or advantage"],
"boreal": ["(Adj) Relating to northern regions", "(Adj) Characteristic of cold northern climates"],
"borate": ["(N) A salt of boric acid", "(N) A mineral containing boron"],
"borborygmus": ["(N) A rumbling noise in the intestines", "(N) Audible stomach gurgling"],
"boulder": ["(N) A large rock worn smooth by erosion", "(N) A massive stone"],
"bouleversement": ["(N) A violent upheaval", "(N) A dramatic reversal or disruption"],
"bounty": ["(N) A reward or payment", "(N) Generosity or abundance"],
"brace": ["(V) To prepare for impact", "(N) A support or reinforcement"],
"bract": ["(N) A modified leaf associated with a flower", "(N) A leaflike structure beneath a bloom"],
"bramble": ["(N) A prickly shrub", "(N) A tangle of thorny plants"],
"brambleberry": ["(N) A berry from a bramble plant", "(N) A wild blackberry-type fruit"],
"brandish": ["(V) To wave something threateningly", "(V) To display boldly"],
"bravado": ["(N) A show of boldness intended to impress", "(N) Swaggering confidence"],
"brawl": ["(N) A noisy fight", "(V) To fight roughly"],
"brawn": ["(N) Physical strength", "(N) Muscular power"],
"bray": ["(V) To make a loud donkey-like cry", "(N) A harsh, loud sound"],
"braze": ["(V) To join metals by melting a filler", "(V) To solder using high heat"],
"brazen": ["(Adj) Bold and shameless", "(V) To face something boldly"],
"breach": ["(N) A violation or gap", "(V) To break through"],
"breadth": ["(N) The width of something", "(N) Broad range or scope"],
"breakwater": ["(N) A barrier protecting a shore from waves", "(N) A structure reducing coastal erosion"],
"breccia": ["(N) A rock composed of broken fragments", "(N) Angular mineral debris cemented together"],
"bregma": ["(N) The junction of skull bones", "(N) A point on the top of the head"],
"breviloquent": ["(Adj) Speaking briefly", "(Adj) Using few words"],
"brevity": ["(N) Concise expression", "(N) Shortness in duration"],
"brim": ["(N) The edge of a container", "(V) To be full to the top"],
"brimstone": ["(N) Sulfur, especially in biblical contexts", "(N) Fiery punishment or damnation"],
"brindle": ["(Adj) Streaked with dark markings", "(N) A coat pattern in animals"],
"brisk": ["(Adj) Quick and energetic", "(Adj) Refreshingly cool"],
"bristle": ["(V) To react angrily or defensively", "(N) A short, stiff hair"],
"broach": ["(V) To bring up a topic for discussion", "(V) To pierce or open"],
"brocade": ["(N) Richly decorative fabric", "(N) Cloth woven with raised patterns"],
"brood": ["(V) To think anxiously or gloomily", "(N) A group of young animals"],
"brook": ["(N) A small stream", "(V) To tolerate or endure"],
"broom": ["(N) A cleaning brush with bristles", "(N) A shrub with yellow flowers"],
"broth": ["(N) A savory liquid from simmered meat or vegetables", "(N) A thin soup base"],
"browbeat": ["(V) To intimidate with harsh words", "(V) To bully or pressure"],
"brunt": ["(N) The main force or impact", "(N) The worst part of something"],
"brusque": ["(Adj) Abrupt or blunt in manner", "(Adj) Curt to the point of rudeness"],
"buck": ["(V) To resist or oppose", "(N) A male deer"],
"buckskin": ["(N) Soft leather made from deer hide", "(N) Clothing made from such leather"],
"budge": ["(V) To move slightly", "(V) To change one’s opinion"],
"buffet": ["(V) To strike repeatedly", "(N) A meal where guests serve themselves"],
"bugle": ["(N) A simple brass instrument", "(V) To sound a bugle call"],
"bulbous": ["(Adj) Rounded and swollen", "(Adj) Bulging in shape"],
"bullionist": ["(N) A supporter of precious-metal currency", "(N) Someone who favors gold-based economics"],
"bullock": ["(N) A young bull", "(N) A castrated male bovine"],
"bulwark": ["(N) A defensive wall", "(N) A strong support or protection"],
"bumptious": ["(Adj) Annoyingly self-assertive", "(Adj) Pushy or conceited"],
"bungle": ["(V) To carry out a task clumsily", "(N) A poorly done job"],
"burgeon": ["(V) To grow or expand rapidly", "(V) To flourish or develop quickly"],
"burrow": ["(V) To dig a hole or tunnel", "(N) A small underground dwelling"],
"burrower": ["(N) An animal that digs tunnels or holes", "(N) A creature adapted for living underground"],
"bursary": ["(N) A scholarship or financial grant", "(N) A treasury or financial office"],
"bustle": ["(V) To move energetically or busily", "(N) Excited, noisy activity"],
"butcher": ["(N) A person who cuts and sells meat", "(V) To kill or prepare animals for food"],
"buttress": ["(N) A projecting support for a wall", "(V) To strengthen or reinforce"],
"buxom": ["(Adj) Plump and attractively full-figured", "(Adj) Healthy and lively in appearance"],
"bylaw": ["(N) A rule made by a local authority", "(N) A regulation governing internal operations"],
"byproduct": ["(N) A secondary result of a process", "(N) Something produced incidentally"],
"byway": ["(N) A minor road or path", "(N) A less-traveled route"],
"cabal": ["(N) A secret political faction", "(N) A small group plotting together"],
"cabin": ["(N) A small wooden shelter", "(N) A private room on a ship"],
"cable": ["(N) A thick rope or wire", "(V) To send a message by telegraph"],
"cache": ["(N) A hidden store of goods", "(V) To store away secretly"],
"cacophony": ["(N) A harsh, discordant mixture of sounds", "(N) Loud, jarring noise"],
"cactus": ["(N) A spiny desert plant", "(N) A succulent adapted to arid climates"],
"cadence": ["(N) A rhythmic flow of sounds", "(N) A sequence of musical chords"],
"cairn": ["(N) A pile of stones marking a place", "(N) A memorial made of stacked rocks"],
"cairnstone": ["(N) A stone used in a cairn", "(N) A marker rock placed for navigation"],
"calamity": ["(N) A disastrous event", "(N) Great misfortune or distress"],
"calcareous": ["(Adj) Containing calcium carbonate", "(Adj) Chalky or limestone-rich"],
"calcine": ["(V) To heat a substance until it decomposes", "(V) To reduce to powder by burning"],
"calibrate": ["(V) To adjust for accuracy", "(V) To standardize measuring equipment"],
"calligraphy": ["(N) Decorative handwriting", "(N) The art of beautiful lettering"],
"callous": ["(Adj) Emotionally insensitive", "(Adj) Hardened or thickened (skin)"],
"callow": ["(Adj) Inexperienced or immature", "(Adj) Lacking adult sophistication"],
"calumny": ["(N) False statements meant to harm", "(N) Slander or defamation"],
"camaraderie": ["(N) Mutual trust among companions", "(N) Warm friendship within a group"],
"cambium": ["(N) A plant tissue that produces new cells", "(N) A growth layer in stems and roots"],
"camelid": ["(N) A member of the camel family", "(N) Animals such as llamas or alpacas"],
"cameo": ["(N) A small carved relief", "(N) A brief appearance in a film"],
"canard": ["(N) A false or misleading story", "(N) A fabricated report"],
"canary": ["(N) A small yellow songbird", "(N) A bright yellow color"],
"candelabra": ["(N) A branched candleholder", "(N) A decorative lighting fixture"],
"candle": ["(N) A stick of wax with a wick", "(N) A source of soft light"],
"cane": ["(N) A walking stick", "(N) A tall grass used for sugar production"],
"canine": ["(Adj) Relating to dogs", "(N) A dog or dog-like animal"],
"canister": ["(N) A small metal container", "(N) A storage vessel for dry goods"],
"canker": ["(N) A fungal plant disease", "(V) To corrupt or infect morally"],
"canny": ["(Adj) Shrewd and careful", "(Adj) Showing good judgment"],
"canoe": ["(N) A narrow boat paddled by hand", "(V) To travel by canoe"],
"canon": ["(N) A general rule or principle", "(N) A collection of accepted works"],
"canopy": ["(N) A covering forming shelter", "(N) The upper layer of a forest"],
"canticle": ["(N) A hymn or chant", "(N) A biblical song of praise"],
"canto": ["(N) A major division of a long poem", "(N) A section of epic poetry"],
"canvas": ["(N) A heavy woven fabric", "(N) A surface for painting"],
"canyon": ["(N) A deep valley with steep sides", "(N) A gorge carved by a river"],
"capacious": ["(Adj) Spacious or roomy", "(Adj) Able to hold a great amount"],
"caparison": ["(V) To dress richly", "(N) Ornate coverings for a horse"],
"capacious": ["(Adj) Spacious or roomy", "(Adj) Able to hold a great amount"],
"capitulate": ["(V) To surrender or give in", "(V) To cease resisting"],
"caprice": ["(N) A sudden change of mood", "(N) An impulsive action"],
"capricious": ["(Adj) Unpredictable or impulsive", "(Adj) Prone to sudden changes"],
"capsize": ["(V) To overturn in water", "(V) To tip over accidentally"],
"capstone": ["(N) A finishing stone at the top of a structure", "(N) A crowning achievement"],
"carafe": ["(N) A glass container for serving drinks", "(N) A wide-mouthed decanter"],
"carapace": ["(N) A hard shell on an animal", "(N) A protective outer covering"],
"caraway": ["(N) An aromatic seed used in cooking", "(N) A plant producing such seeds"],
"caravan": ["(N) A group traveling together", "(N) A covered vehicle for living or travel"],
"caravel": ["(N) A small, fast sailing ship", "(N) A light vessel used in exploration"],
"caraway": ["(N) A spice seed used in bread and dishes", "(N) A plant of the parsley family"],
"carbonado": ["(N) A black diamond", "(N) Meat grilled over coals"],
"carcinogen": ["(N) A substance that causes cancer", "(N) A cancer-producing agent"],
"cardinal": ["(Adj) Of prime importance", "(N) A bright red songbird"],
"careen": ["(V) To tilt or lean dangerously", "(V) To rush forward uncontrollably"],
"caress": ["(V) To touch gently", "(N) A soft, affectionate stroke"],
"cargo": ["(N) Goods carried by a ship or vehicle", "(N) Freight transported commercially"],
"carouse": ["(V) To drink and celebrate noisily", "(N) A lively drinking party"],
"carp": ["(V) To complain constantly", "(N) A freshwater fish"],
"carpet": ["(N) A thick floor covering", "(V) To cover completely"],
"carrel": ["(N) A small study cubicle", "(N) A partitioned desk in a library"],
"carrot": ["(N) An orange root vegetable", "(N) A reward used as motivation"],
"cartilage": ["(N) A flexible connective tissue", "(N) A smooth tissue covering joints"],
"cartographer": ["(N) A mapmaker", "(N) Someone who creates charts or maps"],
"cascade": ["(N) A small waterfall", "(V) To flow or fall in stages"],
"cask": ["(N) A large barrel for liquids", "(V) To store in a cask"],
"castigate": ["(V) To criticize severely", "(V) To punish harshly"],
"castle": ["(N) A fortified building", "(N) A large stately residence"],
"casualty": ["(N) A person injured or killed", "(N) A victim of an accident or disaster"],
"cataclysm": ["(N) A violent upheaval", "(N) A sudden, massive change"],
"catalogue": ["(N) A systematic list of items", "(V) To record or classify"],
"catalyze": ["(V) To speed up a chemical reaction", "(V) To cause rapid change"],
"catapult": ["(N) A device for launching objects", "(V) To hurl or fling suddenly"],
"cataract": ["(N) A large waterfall", "(N) A clouding of the eye lens"],
"catarrh": ["(N) Excess mucus in the nose or throat", "(N) Inflammation of mucous membranes"],
"catastrophe": ["(N) A sudden disaster", "(N) A complete failure"],
"catechism": ["(N) A summary of religious doctrine", "(N) Instruction by question and answer"],
"cater": ["(V) To provide food and service", "(V) To supply what is needed"],
"catkin": ["(N) A slim, cylindrical flower cluster", "(N) A drooping inflorescence on trees"],
"cattle": ["(N) Domesticated bovine animals", "(N) Herd animals raised for meat or milk"],
"caudal": ["(Adj) Relating to the tail", "(Adj) Situated near the rear end"],
"cauldron": ["(N) A large metal pot", "(N) A situation of intense activity"],
"causal": ["(Adj) Relating to cause and effect", "(Adj) Involving a reason for something"],
"caustic": ["(Adj) Able to burn or corrode", "(Adj) Sarcastic in a biting way"],
"cauterize": ["(V) To burn tissue to stop bleeding", "(V) To seal a wound with heat"],
"cavalier": ["(Adj) Showing a lack of proper concern", "(N) A mounted soldier"],
"caveat": ["(N) A warning or caution", "(N) A condition attached to an agreement"],
"cavern": ["(N) A large cave", "(N) A hollow underground chamber"],
"cavil": ["(V) To raise petty objections", "(N) A trivial criticism"],
"cedar": ["(N) A fragrant evergreen tree", "(N) Wood from such a tree"],
"cedargrove": ["(N) A grove of cedar trees", "(N) A wooded area dominated by cedars"],
"cedarwood": ["(N) Wood from cedar trees", "(N) A fragrant timber used in furniture"],
"cede": ["(V) To give up territory or rights", "(V) To surrender formally"],
"celebrant": ["(N) A person performing a religious ceremony", "(N) Someone celebrating a special occasion"],
"celerity": ["(N) Swiftness of movement", "(N) Quickness in action"],
"celestial": ["(Adj) Relating to the sky or heavens", "(Adj) Divine or heavenly"],
"cellar": ["(N) A room below ground level", "(N) A storage space for wine or goods"],
"cement": ["(N) A binding construction material", "(V) To join firmly together"],
"censor": ["(V) To suppress unacceptable parts", "(N) An official who reviews content"],
"censure": ["(V) To express strong disapproval", "(N) A formal reprimand"],
"centaur": ["(N) A mythical half-man, half-horse creature", "(N) A symbol of dual nature"],
"centipede": ["(N) A many-legged arthropod", "(N) A fast-moving predatory insect"],
"ceramic": ["(Adj) Made of baked clay", "(N) A pottery object"],
"cerulean": ["(Adj) Deep sky blue", "(N) A vivid blue color"],
"cessation": ["(N) A stopping or ending", "(N) A temporary pause"],
"chafe": ["(V) To irritate by rubbing", "(V) To become annoyed or impatient"],
"chaff": ["(N) Husks separated from grain", "(N) Worthless or trivial matter"],
"chagrin": ["(N) Distress caused by disappointment", "(V) To embarrass or humiliate"],
"chain": ["(N) A series of linked metal rings", "(V) To fasten with a chain"],
"chair": ["(N) A seat with a back", "(V) To preside over a meeting"],
"chalice": ["(N) A ceremonial drinking cup", "(N) A goblet used in religious rites"],
"chalk": ["(N) A soft white limestone", "(V) To write or draw with chalk"],
"chamber": ["(N) A room or enclosed space", "(N) A legislative or judicial body"],
"chameleon": ["(N) A color-changing lizard", "(N) A person who adapts behavior easily"],
"champion": ["(N) A winner of a contest", "(V) To support or defend a cause"],
"chance": ["(N) The occurrence of events by accident", "(V) To risk or attempt"],
"chandelier": ["(N) A decorative hanging light fixture", "(N) A branched ceiling lamp"],
"changeover": ["(N) A switch from one system to another", "(N) A transition period"],
"channel": ["(N) A passage for water or communication", "(V) To direct or guide"],
"chant": ["(V) To sing or recite rhythmically", "(N) A repeated melodic phrase"],
"chapel": ["(N) A small place of worship", "(N) A room for religious services"],
"chaplet": ["(N) A wreath or garland", "(N) A string of prayer beads"],
"charade": ["(N) An absurd pretense", "(N) A game of acting out words"],
"charcoal": ["(N) A black carbon fuel", "(V) To draw with charcoal"],
"chariot": ["(N) A two-wheeled ancient vehicle", "(V) To ride in or drive a chariot"],
"charisma": ["(N) Compelling charm or influence", "(N) A magnetic personal quality"],
"charlatan": ["(N) A fraud pretending to have skills", "(N) A deceitful impostor"],
"chasm": ["(N) A deep fissure in the earth", "(N) A profound difference between viewpoints"],
"chaste": ["(Adj) Pure or modest", "(Adj) Abstaining from sexual activity"],
"chasten": ["(V) To discipline or correct", "(V) To subdue or moderate"],
"chateau": ["(N) A large French country house", "(N) A stately mansion"],
"chattel": ["(N) Personal property", "(N) A movable possession"],
"chatter": ["(V) To talk rapidly", "(N) Quick, trivial conversation"],
"chaw": ["(V) To chew roughly", "(N) A wad of chewing tobacco"],
"cheap": ["(Adj) Low in price", "(Adj) Of poor quality"],
"cheat": ["(V) To act dishonestly", "(N) A person who deceives"],
"check": ["(V) To examine or verify", "(N) A mark indicating correctness"],
"cheek": ["(N) The side of the face", "(N) Boldness or impudence"],
"cheer": ["(V) To shout encouragement", "(N) A joyful shout"],
"cheese": ["(N) A dairy product made from curds", "(N) A molded block of fermented milk"],
"cherish": ["(V) To hold dear", "(V) To care for lovingly"],
"cherry": ["(N) A small red stone fruit", "(N) A tree producing such fruit"],
"cherub": ["(N) A winged angelic being", "(N) A sweet-faced child"],
"chess": ["(N) A strategic board game", "(N) A contest of planning and foresight"],
"chest": ["(N) A large storage box", "(N) The front part of the torso"],
"chevron": ["(N) A V-shaped pattern", "(N) A military insignia"],
"chew": ["(V) To bite and grind with teeth", "(N) The act of chewing"],
"chic": ["(Adj) Stylish and fashionable", "(N) Elegant style"],
"chickadee": ["(N) A small North American songbird", "(N) A bird known for its 'chick-a-dee' call"],
"chicken": ["(N) A domesticated bird", "(N) A cowardly person"],
"chide": ["(V) To scold mildly", "(V) To express disapproval"],
"chief": ["(N) A leader or ruler", "(Adj) Most important"],
"chiffon": ["(N) A light, sheer fabric", "(N) A delicate textile used in dresses"],
"child": ["(N) A young human", "(N) A son or daughter"],
"chill": ["(N) A feeling of coldness", "(V) To make cold"],
"chime": ["(V) To make a ringing sound", "(N) A set of tuned bells"],
"chimera": ["(N) A mythical fire-breathing monster", "(N) An impossible or fanciful idea"],
"chimpanzee": ["(N) A great ape native to Africa", "(N) A highly intelligent primate"],
"chin": ["(N) The lower part of the face", "(V) To raise the chin defiantly"],
"china": ["(N) Fine porcelain dishes", "(N) A type of ceramic ware"],
"chisel": ["(N) A tool for cutting hard materials", "(V) To carve or shape with a chisel"],
"chivalry": ["(N) Medieval knightly conduct", "(N) Courteous behavior toward others"],
"chlorine": ["(N) A greenish-yellow gas used as a disinfectant", "(N) A chemical element used in water purification"],
"choleric": ["(Adj) Easily angered or irritable", "(Adj) Showing a quick temper"],
"chomp": ["(V) To chew vigorously", "(N) A loud biting or chewing sound"],
"choose": ["(V) To select from options", "(V) To decide on a course of action"],
"chop": ["(V) To cut into pieces", "(N) A thick slice of meat"],
"choral": ["(Adj) Related to a choir", "(Adj) Sung by a group of voices"],
"chord": ["(N) A combination of musical notes", "(N) A straight line connecting two points on a curve"],
"chore": ["(N) A routine task", "(N) An unpleasant but necessary duty"],
"chorus": ["(N) A group singing together", "(V) To say something in unison"],
"chortle": ["(V) To laugh in a gleeful way", "(N) A joyful, breathy laugh"],
"chowder": ["(N) A thick soup with seafood or vegetables", "(N) A creamy stew"],
"christen": ["(V) To name in a ceremony", "(V) To use something for the first time"],
"chromatic": ["(Adj) Relating to color", "(Adj) Using musical notes outside the main scale"],
"chronicle": ["(V) To record events in order", "(N) A factual written account"],
"chrysalis": ["(N) A protective insect pupa case", "(N) A transitional developmental stage"],
"chuckle": ["(V) To laugh quietly", "(N) A soft, restrained laugh"],
"churn": ["(V) To stir or agitate violently", "(N) A machine for making butter"],
"cider": ["(N) A drink made from fermented apples", "(N) A non-alcoholic apple beverage"],
"cinder": ["(N) A small piece of partly burned coal or wood", "(N) A fragment left after combustion"],
"cipher": ["(N) A secret code", "(V) To encode or calculate"],
"circuit": ["(N) A closed path for electricity", "(N) A regular route or series of events"],
"cirrus": ["(N) A high, wispy cloud", "(N) A delicate atmospheric formation"],
"cistern": ["(N) A tank for storing water", "(N) A reservoir for liquid collection"],
"citadel": ["(N) A fortress protecting a city", "(N) A stronghold or safe place"],
"citrine": ["(N) A yellow quartz gemstone", "(Adj) Lemon-colored"],
"civic": ["(Adj) Relating to a city or citizenship", "(Adj) Connected to public affairs"],
"civil": ["(Adj) Polite and courteous", "(Adj) Relating to citizens or government"],
"clad": ["(Adj) Dressed or covered", "(V) To provide with a protective layer"],
"claim": ["(V) To assert ownership or truth", "(N) A demand for something owed"],
"clamor": ["(N) A loud uproar", "(V) To shout noisily"],
"clamber": ["(V) To climb awkwardly", "(V) To scramble with effort"],
"clamp": ["(N) A device for holding things tightly", "(V) To fasten securely"],
"clan": ["(N) A group of related families", "(N) A close-knit community"],
"clangor": ["(N) A loud metallic ringing", "(N) A continuous clashing noise"],
"clank": ["(V) To make a sharp metallic sound", "(N) A loud metal-on-metal noise"],
"clap": ["(V) To strike hands together", "(N) A sharp, sudden sound"],
"clasp": ["(V) To grasp tightly", "(N) A fastener or buckle"],
"classic": ["(Adj) Of the highest quality", "(N) A work recognized as outstanding"],
"clatter": ["(V) To make a rattling noise", "(N) A series of loud, sharp sounds"],
"clause": ["(N) A grammatical unit with subject and verb", "(N) A section of a legal document"],
"claw": ["(N) A curved nail on an animal", "(V) To scratch or dig with claws"],
"clay": ["(N) A fine-grained natural soil", "(N) Material used for pottery"],
"cleanse": ["(V) To make clean or pure", "(V) To rid of impurities"],
"clear": ["(Adj) Easy to understand", "(V) To remove obstacles"],
"cleave": ["(V) To split or cut apart", "(V) To cling closely"],
"cleft": ["(N) A split or indentation", "(Adj) Divided or split"],
"clemency": ["(N) Mercy or leniency", "(N) Compassion shown in judgment"],
"clench": ["(V) To close tightly", "(V) To grip firmly"],
"clergy": ["(N) Religious officials", "(N) People authorized for spiritual duties"],
"cleric": ["(N) A member of the clergy", "(N) A religious leader"],
"clever": ["(Adj) Quick to understand", "(Adj) Skillful or ingenious"],
"click": ["(V) To make a short, sharp sound", "(N) A snapping noise"],
"client": ["(N) A person receiving services", "(N) A customer or patron"],
"cliff": ["(N) A steep rock face", "(N) A high, vertical drop"],
"climate": ["(N) Long-term weather patterns", "(N) A prevailing atmosphere or mood"],
"clinch": ["(V) To secure or settle decisively", "(V) To fasten firmly"],
"cling": ["(V) To hold tightly", "(V) To remain emotionally attached"],
"clinic": ["(N) A medical treatment facility", "(N) A session for instruction"],
"clink": ["(V) To make a light ringing sound", "(N) A metallic tinkle"],
"clip": ["(V) To cut or trim", "(N) A fastener or holder"],
"cloak": ["(N) A loose outer garment", "(V) To conceal or disguise"],
"clobber": ["(V) To strike heavily", "(V) To defeat decisively"],
"clock": ["(N) A device for measuring time", "(V) To record speed or time"],
"clod": ["(N) A lump of earth", "(N) A dull or stupid person"],
"clog": ["(V) To block or obstruct", "(N) A wooden shoe"],
"clone": ["(N) An identical genetic copy", "(V) To duplicate exactly"],
"close": ["(V) To shut or end", "(Adj) Near in distance"],
"closet": ["(N) A small storage room", "(V) To hide or seclude"],
"clot": ["(N) A thickened mass of blood", "(V) To coagulate"],
"clothe": ["(V) To dress or cover", "(V) To provide garments"],
"cloud": ["(N) A visible mass of water vapor", "(V) To obscure or darken"],
"clout": ["(N) Influence or power", "(V) To strike with force"],
"clover": ["(N) A small plant with three leaves", "(N) A symbol of luck"],
"cloverbud": ["(N) A young clover sprout", "(N) A newly formed clover leaf"],
"cloverleaf": ["(N) A road interchange shaped like a clover", "(N) A leaf with multiple lobes"],
"cloy": ["(V) To become overly sweet or sentimental", "(V) To cause disgust through excess"],
"club": ["(N) A group with shared interests", "(N) A heavy stick used as a weapon"],
"cluck": ["(V) To make a hen’s sound", "(N) A short, sharp clicking noise"],
"clue": ["(N) A piece of evidence", "(V) To inform or hint"],
"clump": ["(N) A cluster of things", "(V) To walk heavily"],
"clutch": ["(V) To grasp tightly", "(N) A mechanism for engaging power"],
"coagulate": ["(V) To thicken or clot", "(V) To change from liquid to solid"],
"coal": ["(N) A black combustible rock", "(V) To supply with coal"],
"coalesce": ["(V) To come together into one whole", "(V) To unite or merge"],
"coarse": ["(Adj) Rough in texture", "(Adj) Lacking refinement"],
"coast": ["(N) Land along the sea", "(V) To move effortlessly"],
"coax": ["(V) To persuade gently", "(V) To entice with soft words"],
"cob": ["(N) A male swan", "(N) A rounded loaf or lump"],
"cobble": ["(V) To mend roughly", "(N) A rounded stone used for paving"],
"cobblestone": ["(N) A stone used for paving streets", "(N) A rounded, naturally worn rock"],
"cobweb": ["(N) A spider’s web", "(N) Something dusty or neglected"],
"coda": ["(N) A concluding musical passage", "(N) A final section of a work"],
"coddle": ["(V) To treat with excessive care", "(V) To pamper or overprotect"],
"code": ["(N) A system of symbols or rules", "(V) To write instructions for a computer"],
"codify": ["(V) To arrange into a systematic code", "(V) To organize laws or rules"],
"coerce": ["(V) To force someone through pressure", "(V) To compel by threats"],
"coffer": ["(N) A strongbox for valuables", "(N) A recessed panel in a ceiling"],
"cogent": ["(Adj) Clear and convincing", "(Adj) Logically compelling"],
"cognate": ["(Adj) Related by origin", "(N) A word with a common root"],
"cognition": ["(N) The mental process of knowing", "(N) Perception and reasoning"],
"cohabit": ["(V) To live together", "(V) To share a residence without marriage"],
"cohere": ["(V) To stick together", "(V) To be logically consistent"],
"cohort": ["(N) A group of people with a shared characteristic", "(N) A companion or associate"],
"coil": ["(N) A looped series of rings", "(V) To wind into loops"],
"coin": ["(N) A piece of stamped metal currency", "(V) To invent a new word or phrase"],
"coincide": ["(V) To occur at the same time", "(V) To match exactly"],
"cold": ["(Adj) Low in temperature", "(N) A common viral illness"],
"collaborate": ["(V) To work together", "(V) To cooperate on a project"],
"collage": ["(N) An artwork made from assembled materials", "(N) A mixture of various elements"],
"collapse": ["(V) To fall down suddenly", "(N) A breakdown or failure"],
"collar": ["(N) A band around the neck", "(V) To seize or apprehend"],
"collate": ["(V) To gather and arrange in order", "(V) To compare texts critically"],
"colleague": ["(N) A coworker", "(N) A professional associate"],
"collect": ["(V) To gather together", "(V) To receive payments"],
"colloquial": ["(Adj) Informal or conversational", "(Adj) Used in everyday speech"],
"colon": ["(N) A punctuation mark", "(N) A part of the large intestine"],
"colony": ["(N) A settlement ruled by another country", "(N) A group of organisms living together"],
"color": ["(N) A visual hue", "(V) To apply pigment"],
"colossal": ["(Adj) Extremely large", "(Adj) Gigantic in scale"],
"colt": ["(N) A young male horse", "(N) A youthful or inexperienced person"],
"column": ["(N) A vertical support pillar", "(N) A section of printed text"],
"comb": ["(N) A toothed grooming tool", "(V) To search thoroughly"],
"combat": ["(N) Fighting or conflict", "(V) To oppose or fight against"],
"combine": ["(V) To join together", "(N) A harvesting machine"],
"come": ["(V) To move toward a place", "(V) To arrive or occur"],
"comely": ["(Adj) Attractive or pleasing", "(Adj) Fair in appearance"],
"comet": ["(N) A celestial body with a glowing tail", "(N) A small icy object orbiting the sun"],
"comfort": ["(N) A state of physical ease", "(V) To soothe or console"],
"comic": ["(Adj) Funny or humorous", "(N) A comedian or comic book"],
"commemorate": ["(V) To honor the memory of", "(V) To mark an event with ceremony"],
"commence": ["(V) To begin or start", "(V) To initiate formally"],
"commend": ["(V) To praise formally", "(V) To recommend as worthy"],
"commensurate": ["(Adj) Corresponding in size or degree", "(Adj) Proportionate or equal"],
"commingle": ["(V) To mix together", "(V) To blend or combine"],
"commiserate": ["(V) To express sympathy", "(V) To share in someone’s sorrow"],
"commit": ["(V) To carry out or perform", "(V) To pledge or bind to a course"],
"commodity": ["(N) A basic good for trade", "(N) Something useful or valuable"],
"common": ["(Adj) Ordinary or widespread", "(N) Shared land or resource"],
"commotion": ["(N) A noisy disturbance", "(N) Confused or excited movement"],
"commute": ["(V) To travel regularly between home and work", "(V) To reduce a punishment"],
"compact": ["(Adj) Small and efficiently arranged", "(N) A formal agreement"],
"companion": ["(N) A person who accompanies another", "(N) A close friend"],
"company": ["(N) A business organization", "(N) Companionship or guests"],
"compare": ["(V) To examine similarities and differences", "(V) To evaluate relative qualities"],
"compass": ["(N) A navigational instrument", "(N) A tool for drawing circles"],
"compel": ["(V) To force or drive someone to act", "(V) To require by necessity"],
"compendium": ["(N) A concise collection of information", "(N) A summary of key facts"],
"compensate": ["(V) To make up for loss or damage", "(V) To pay for services rendered"],
"compete": ["(V) To strive against others", "(V) To take part in a contest"],
"compile": ["(V) To gather information into a single source", "(V) To assemble from various materials"],
"complain": ["(V) To express dissatisfaction", "(V) To protest or object"],
"complement": ["(N) Something that completes another", "(V) To enhance or improve by adding"],
"complete": ["(Adj) Finished or whole", "(V) To bring to an end"],
"complex": ["(Adj) Complicated or intricate", "(N) A group of related buildings"],
"complicate": ["(V) To make more difficult", "(V) To introduce confusion"],
"compliment": ["(N) A polite expression of praise", "(V) To express admiration"],
"comply": ["(V) To act in accordance with rules", "(V) To obey a request"],
"compose": ["(V) To create or write", "(V) To calm or settle oneself"],
"compost": ["(N) Decayed organic matter", "(V) To convert waste into fertilizer"],
"compound": ["(N) A mixture of elements", "(V) To combine or intensify"],
"comprehend": ["(V) To understand fully", "(V) To grasp the meaning of"],
"compress": ["(V) To press together tightly", "(N) A cloth applied for healing"],
"comprise": ["(V) To consist of", "(V) To include as parts"],
"compromise": ["(N) A mutual agreement", "(V) To settle differences by concession"],
"compute": ["(V) To calculate or reckon", "(V) To determine by mathematics"],
"concede": ["(V) To admit as true", "(V) To yield or surrender"],
"conceal": ["(V) To hide from view", "(V) To keep secret"],
"concentrate": ["(V) To focus attention", "(N) A substance made stronger by removal of liquid"],
"concept": ["(N) An abstract idea", "(N) A general notion or plan"],
"concern": ["(N) A matter of interest or worry", "(V) To affect or involve"],
"concert": ["(N) A musical performance", "(V) To plan or act together"],
"conch": ["(N) A large spiral shell", "(N) A tropical marine mollusk"],
"conciliate": ["(V) To win over or soothe", "(V) To reconcile differences"],
"concise": ["(Adj) Brief and to the point", "(Adj) Expressing much in few words"],
"conclave": ["(N) A private meeting", "(N) A gathering for decision-making"],
"conclude": ["(V) To bring to an end", "(V) To reach a judgment"],
"concoct": ["(V) To prepare by mixing ingredients", "(V) To devise or invent"],
"concomitant": ["(Adj) Occurring together", "(N) Something that accompanies another"],
"concord": ["(N) Agreement or harmony", "(N) A peaceful relationship"],
"concourse": ["(N) A large open area", "(N) A gathering or crowd"],
"concrete": ["(N) A building material of cement and gravel", "(Adj) Real or tangible"],
"concur": ["(V) To agree or share the same opinion", "(V) To happen at the same time"],
"concussion": ["(N) A brain injury caused by impact", "(N) A violent shaking or shock"],
"condemn": ["(V) To express strong disapproval", "(V) To sentence someone to punishment"],
"condense": ["(V) To make something more compact", "(V) To change from gas to liquid"],
"condiment": ["(N) A substance added to food for flavor", "(N) A seasoning such as mustard or ketchup"],
"condition": ["(N) A state of being", "(V) To train or prepare for use"],
"condone": ["(V) To accept or allow behavior considered wrong", "(V) To overlook or forgive an offense"],
"conduce": ["(V) To contribute to a result", "(V) To lead or tend toward a particular outcome"],
"conduct": ["(N) Behavior or manner", "(V) To lead or guide"],
"conduit": ["(N) A channel for conveying fluids or information", "(N) A pipe or tube for electrical wiring"],
"cone": ["(N) A three-dimensional geometric shape", "(N) A seed-bearing structure of conifers"],
"confabulate": ["(V) To chat informally", "(V) To fabricate imaginary experiences"],
"confection": ["(N) A sweet food item", "(N) Something delicately made"],
"confederate": ["(N) An ally or partner", "(V) To unite in a league"],
"confer": ["(V) To discuss or consult", "(V) To grant or bestow"],
"confess": ["(V) To admit wrongdoing", "(V) To acknowledge something openly"],
"confide": ["(V) To share a secret with trust", "(V) To entrust something to someone"],
"configure": ["(V) To arrange or set up", "(V) To shape according to a plan"],
"confine": ["(V) To restrict within limits", "(N) A boundary or limit"],
"confirm": ["(V) To establish truth or accuracy", "(V) To approve formally"],
"confiscate": ["(V) To seize by authority", "(V) To take away as a penalty"],
"conflagrate": ["(V) To catch fire or set ablaze", "(V) To burn intensely"],
"conflate": ["(V) To combine two things into one", "(V) To confuse separate ideas"],
"conflict": ["(N) A struggle or clash", "(V) To be incompatible or opposed"],
"confluence": ["(N) The meeting of two rivers", "(N) A coming together of ideas or events"],
"conform": ["(V) To comply with rules or standards", "(V) To behave in a socially acceptable way"],
"confound": ["(V) To confuse or perplex", "(V) To prove something wrong"],
"confront": ["(V) To face something challenging", "(V) To challenge someone directly"],
"confuse": ["(V) To make unclear or uncertain", "(V) To mix up mentally"],
"congeal": ["(V) To solidify from cooling", "(V) To thicken or clot"],
"congenial": ["(Adj) Pleasant and agreeable", "(Adj) Suited to one’s tastes"],
"congest": ["(V) To overcrowd or block", "(V) To fill to excess"],
"conglomerate": ["(N) A large corporation made of merged companies", "(V) To gather into a mass"],
"congruent": ["(Adj) In agreement or harmony", "(Adj) Identical in form or shape"],
"conifer": ["(N) A cone-bearing tree", "(N) A gymnosperm such as pine or spruce"],
"conjecture": ["(N) A guess based on incomplete information", "(V) To speculate or infer"],
"conjoin": ["(V) To join together", "(V) To unite or combine"],
"conjugal": ["(Adj) Relating to marriage", "(Adj) Pertaining to the relationship between spouses"],
"conjure": ["(V) To summon by magic", "(V) To call to mind vividly"],
"connect": ["(V) To join or link together", "(V) To establish a relationship"],
"connive": ["(V) To secretly allow wrongdoing", "(V) To plot or scheme"],
"connoisseur": ["(N) An expert judge of taste", "(N) Someone with refined appreciation"],
"connotation": ["(N) An implied meaning", "(N) A secondary association of a word"],
"conquer": ["(V) To defeat or overcome", "(V) To gain control through effort"],
"conscript": ["(V) To enlist by force", "(N) A person drafted into service"],
"consecrate": ["(V) To make sacred", "(V) To dedicate formally to a purpose"],
"consent": ["(N) Permission or approval", "(V) To agree willingly"],
"consequence": ["(N) A result or effect", "(N) Importance or significance"],
"conserve": ["(V) To protect from harm or waste", "(V) To preserve resources"],
"consider": ["(V) To think carefully about", "(V) To regard or judge"],
"consign": ["(V) To deliver to another’s care", "(V) To assign to an undesirable fate"],
"consist": ["(V) To be composed of", "(V) To exist or reside in"],
"console": ["(V) To comfort someone in distress", "(N) A control panel or cabinet"],
"consolidate": ["(V) To combine into a stronger whole", "(V) To reinforce or strengthen"],
"consonant": ["(N) A speech sound not a vowel", "(Adj) In agreement or harmony"],
"consort": ["(V) To associate with", "(N) A spouse or companion"],
"conspicuous": ["(Adj) Easily seen or noticed", "(Adj) Attracting attention"],
"conspire": ["(V) To plan secretly", "(V) To work together toward a harmful goal"],
"constellate": ["(V) To cluster together", "(V) To form a group or pattern"],
"consternate": ["(V) To fill with alarm or dismay", "(V) To bewilder or terrify"],
"constituent": ["(N) A component part", "(N) A voter represented by an official"],
"constrain": ["(V) To restrict or limit", "(V) To compel by force"],
"constrict": ["(V) To tighten or narrow", "(V) To limit freedom or movement"],
"construe": ["(V) To interpret or explain", "(V) To analyze the meaning of words"],
"consul": ["(N) A government representative abroad", "(N) An official appointed to assist citizens"],
"consult": ["(V) To seek advice", "(V) To refer to a source of information"],
"consume": ["(V) To eat or drink", "(V) To use up resources"],
"consummate": ["(Adj) Perfect or complete", "(V) To bring to fulfillment"],
"contact": ["(N) Communication or connection", "(V) To get in touch with"],
"contain": ["(V) To hold within limits", "(V) To control or restrain"],
"contaminate": ["(V) To pollute or make impure", "(V) To infect with harmful substances"],
"contemplate": ["(V) To think deeply about", "(V) To consider thoughtfully"],
"contend": ["(V) To struggle or compete", "(V) To assert a position"],
"content": ["(N) The substance within something", "(Adj) Satisfied or at ease"],
"contest": ["(N) A competition", "(V) To challenge or dispute"],
"context": ["(N) Surrounding circumstances", "(N) The setting that gives meaning"],
"contiguous": ["(Adj) Sharing a common border", "(Adj) Touching or adjacent"],
"continent": ["(N) A large landmass", "(Adj) Exercising self-restraint"],
"contingent": ["(Adj) Dependent on conditions", "(N) A group forming part of a larger body"],
"continual": ["(Adj) Repeated frequently", "(Adj) Occurring regularly"],
"continue": ["(V) To persist or carry on", "(V) To resume after interruption"],
"contort": ["(V) To twist violently", "(V) To distort out of shape"],
"contour": ["(N) An outline or shape", "(V) To mold or shape"],
"contraband": ["(N) Illegal goods", "(Adj) Prohibited from import or export"],
"contract": ["(N) A binding agreement", "(V) To shrink or draw together"],
"contradict": ["(V) To assert the opposite", "(V) To deny the truth of something"],
"contrary": ["(Adj) Opposite in nature", "(N) A stubborn or opposing person"],
"contrast": ["(N) A striking difference", "(V) To compare differences"],
"contravene": ["(V) To violate a rule or law", "(V) To oppose or contradict"],
"contribute": ["(V) To give or supply", "(V) To help bring about"],
"contrite": ["(Adj) Deeply sorry for wrongdoing", "(Adj) Showing sincere remorse"],
"contrive": ["(V) To devise cleverly", "(V) To plan with ingenuity"],
"control": ["(N) Power to direct or manage", "(V) To regulate or command"],
"controvert": ["(V) To dispute or oppose", "(V) To argue against"],
"contumely": ["(N) Insolent or insulting language", "(N) Contemptuous treatment"],
"conundrum": ["(N) A difficult puzzle or problem", "(N) A riddle with a tricky answer"],
"convalesce": ["(V) To recover health after illness", "(V) To regain strength"],
"convene": ["(V) To gather for a meeting", "(V) To assemble formally"],
"convenience": ["(N) Ease of use", "(N) Something that adds comfort"],
"converge": ["(V) To come together from different directions", "(V) To meet at a point"],
"converse": ["(V) To talk informally", "(N) The opposite or reverse"],
"convert": ["(V) To change form or belief", "(N) A person who adopts new views"],
"convey": ["(V) To transport or carry", "(V) To communicate clearly"],
"convict": ["(N) A person found guilty of a crime", "(V) To declare someone guilty"],
"convince": ["(V) To persuade with argument", "(V) To cause belief or certainty"],
"convivial": ["(Adj) Friendly and lively", "(Adj) Enjoying feasting and company"],
"convoy": ["(N) A group traveling together for protection", "(V) To escort in a group"],
"convulse": ["(V) To shake violently", "(V) To cause upheaval"],
"coo": ["(V) To make a soft murmuring sound", "(N) A gentle, murmured utterance"],
"cook": ["(V) To prepare food by heating", "(N) A person who prepares meals"],
"cool": ["(Adj) Moderately cold", "(V) To lower temperature"],
"coop": ["(N) An enclosure for poultry", "(V) To confine or restrict"],
"cooperate": ["(V) To work together toward a goal", "(V) To act jointly"],
"coordinate": ["(V) To organize activities", "(N) A point defined by numbers"],
"copious": ["(Adj) Abundant in supply", "(Adj) Large in quantity"],
"copper": ["(N) A reddish-brown metal", "(N) A police officer (informal)"],
"coral": ["(N) A hard marine organism", "(N) A pinkish-orange color"],
"corbel": ["(N) A projecting stone support", "(V) To support with a bracket"],
"cordial": ["(Adj) Warm and friendly", "(N) A sweet fruit-flavored drink"],
"cordon": ["(N) A line of guards or police", "(V) To block off with a barrier"],
"core": ["(N) The central part of something", "(V) To remove the center"],
"corral": ["(V) To gather or round up", "(N) An enclosure for livestock"],
"correct": ["(Adj) Free from error", "(V) To make right or accurate"],
"correlate": ["(V) To show a relationship between things", "(N) Something connected to another"],
"correspond": ["(V) To communicate by letters", "(V) To match or agree"],
"corrode": ["(V) To wear away gradually", "(V) To destroy by chemical action"],
"corroborate": ["(V) To confirm with evidence", "(V) To support a statement"],
"corrupt": ["(Adj) Immoral or dishonest", "(V) To degrade or spoil"],
"corsair": ["(N) A pirate or privateer", "(N) A fast, lightly armed ship"],
"cortex": ["(N) The outer layer of an organ", "(N) The brain’s outer surface"],
"cosmic": ["(Adj) Relating to the universe", "(Adj) Vast or immense"],
"cosset": ["(V) To pamper excessively", "(V) To treat with indulgent care"],
"costume": ["(N) Clothing worn for a role", "(V) To dress in special attire"],
"cot": ["(N) A small portable bed", "(N) A baby’s crib"],
"cottage": ["(N) A small rural house", "(N) A cozy dwelling"],
"cottagecore": ["(N) An aesthetic idealizing rural life", "(Adj) Relating to pastoral simplicity"],
"cotton": ["(N) A soft white fiber", "(V) To begin to understand (informal)"],
"cottonseed": ["(N) The seed of the cotton plant", "(N) A source of oil and meal"],
"cottonwood": ["(N) A fast-growing poplar tree", "(N) A tree with fluffy seeds"],
"couch": ["(N) A long upholstered seat", "(V) To express in specific terms"],
"cougar": ["(N) A large wild cat", "(N) An older woman pursuing younger men (informal)"],
"cough": ["(V) To expel air suddenly from the lungs", "(N) A sudden hacking sound"],
"could": ["(V) Used to indicate possibility", "(V) Used to make polite requests"],
"council": ["(N) A group convened for decision-making", "(N) An advisory or legislative body"],
"counsel": ["(N) Advice or guidance", "(V) To give professional advice"],
"count": ["(V) To determine the total number", "(N) A nobleman in some European countries"],
"counter": ["(N) A flat surface for work or service", "(V) To oppose or respond to"],
"counteract": ["(V) To neutralize or offset", "(V) To act against something"],
"counterfeit": ["(Adj) Fake or fraudulent", "(V) To imitate illegally"],
"countervail": ["(V) To offset or counterbalance", "(V) To oppose with equal force"],
"country": ["(N) A nation or territory", "(N) Rural land"],
"coup": ["(N) A sudden takeover of power", "(N) A notable or successful move"],
"couple": ["(N) Two individuals together", "(V) To join or connect"],
"courage": ["(N) The ability to face danger", "(N) Strength in the face of fear"],
"course": ["(N) A path or direction", "(N) A series of lessons"],
"court": ["(N) A place where legal cases are heard", "(V) To seek affection or favor"],
"courteous": ["(Adj) Polite and respectful", "(Adj) Showing good manners"],
"cousin": ["(N) A child of one’s aunt or uncle", "(N) A distant relative"],
"covet": ["(V) To desire wrongfully", "(V) To long for something belonging to another"],
"cow": ["(N) A female bovine", "(V) To intimidate or frighten"],
"cower": ["(V) To crouch in fear", "(V) To shrink away timidly"],
"cowl": ["(N) A hooded garment", "(N) A protective covering"],
"coy": ["(Adj) Shy or modest", "(Adj) Pretending reluctance"],
"coyote": ["(N) A wild canine of North America", "(N) A person who smuggles migrants (informal)"],
"cozy": ["(Adj) Warm and comfortable", "(N) A cover to keep a teapot warm"],
"crab": ["(N) A crustacean with claws", "(V) To complain irritably"],
"crack": ["(V) To break with a sharp sound", "(N) A narrow opening"],
"crackle": ["(V) To make a series of small popping sounds", "(N) A crisp, snapping noise"],
"cradle": ["(N) A baby’s bed", "(V) To hold gently"],
"craft": ["(N) A skill or trade", "(V) To make with skill"],
"crag": ["(N) A steep, rugged rock", "(N) A cliff or rocky outcrop"],
"cram": ["(V) To stuff tightly", "(V) To study intensively"],
"crane": ["(N) A tall wading bird", "(N) A machine for lifting heavy objects"],
"cranium": ["(N) The skull enclosing the brain", "(N) The upper part of the skull"],
"crank": ["(N) A handle that turns a mechanism", "(N) An eccentric person"],
"cranny": ["(N) A small narrow opening", "(N) A hidden nook"],
"crash": ["(V) To collide violently", "(N) A sudden loud noise"],
"crate": ["(N) A large shipping box", "(V) To pack in a crate"],
"crater": ["(N) A bowl-shaped depression, especially from impact or eruption", "(N) A hollow formed by explosion or collapse"],
"cravat": ["(N) A neckband or tie", "(N) A decorative cloth worn around the neck"],
"crave": ["(V) To desire intensely", "(V) To long for something strongly"],
"craven": ["(Adj) Cowardly or lacking courage", "(N) A person who is extremely timid"],
"crawl": ["(V) To move slowly on hands and knees", "(N) A slow, dragging movement"],
"crayon": ["(N) A colored drawing stick", "(V) To draw or color with crayons"],
"craze": ["(N) A widespread enthusiasm or trend", "(V) To develop fine cracks on a surface"],
"crazy": ["(Adj) Mentally unsound or wild", "(Adj) Extremely enthusiastic or passionate (informal)"],
"creak": ["(V) To make a harsh, squeaking sound", "(N) A long, rasping noise"],
"cream": ["(N) The thick fatty part of milk", "(V) To beat into a smooth consistency"],
"crease": ["(N) A line made by folding", "(V) To make a wrinkle or fold"],
"create": ["(V) To bring into existence", "(V) To produce or design"],
"credence": ["(N) Belief in the truth of something", "(N) Acceptance as valid"],
"credible": ["(Adj) Believable or trustworthy", "(Adj) Convincing in appearance"],
"credit": ["(N) Recognition or praise", "(V) To attribute or assign"],
"credo": ["(N) A statement of beliefs", "(N) A guiding principle or philosophy"],
"creed": ["(N) A formal statement of faith", "(N) A system of guiding beliefs"],
"creek": ["(N) A small stream", "(N) A narrow channel of water"],
"creep": ["(V) To move slowly and quietly", "(N) A person who behaves disturbingly"],
"cremate": ["(V) To burn a body to ashes", "(V) To reduce to cinders by fire"],
"creole": ["(N) A person of mixed European and African descent", "(N) A language formed from blending tongues"],
"crepe": ["(N) A thin pancake", "(N) A light, crinkled fabric"],
"crescendo": ["(N) A gradual increase in loudness", "(V) To grow louder or more intense"],
"cress": ["(N) A peppery leafy herb", "(N) A fast-growing edible plant"],
"crest": ["(N) The top of a hill or wave", "(V) To reach the highest point"],
"crevice": ["(N) A narrow crack or opening", "(N) A deep fissure in rock"],
"crew": ["(N) A group working together", "(V) To serve as part of a team"],
"crib": ["(N) A baby’s bed with bars", "(V) To copy someone’s work (informal)"],
"cricket": ["(N) A chirping insect", "(N) A bat-and-ball sport"],
"cried": ["(V) Past tense of cry", "(V) To weep or shout loudly"],
"crime": ["(N) An act against the law", "(N) A wrongdoing or offense"],
"crimp": ["(V) To press into folds", "(N) A small bend or curl"],
"crimson": ["(Adj) Deep red in color", "(N) A rich, dark red hue"],
"cringe": ["(V) To recoil in embarrassment or fear", "(N) A shrinking reaction"],
"crinkle": ["(V) To form small wrinkles", "(N) A slight fold or crease"],
"crisp": ["(Adj) Firm and fresh", "(Adj) Clear and sharp in style"],
"criteria": ["(N) Standards for judgment", "(N) Rules for evaluation"],
"critic": ["(N) A person who judges artistic work", "(N) Someone who expresses disapproval"],
"critique": ["(N) A detailed analysis", "(V) To evaluate or review"],
"croak": ["(V) To make a deep, hoarse sound", "(V) To die (slang)"],
"crochet": ["(V) To make fabric with a hooked needle", "(N) Needlework made by looping yarn"],
"crock": ["(N) A clay pot or jar", "(N) Nonsense or falsehood (informal)"],
"crocus": ["(N) A small spring-blooming flower", "(N) A plant with colorful petals"],
"croissant": ["(N) A flaky crescent-shaped pastry", "(N) A buttery French bread roll"],
"crone": ["(N) An old woman, often depicted as ugly", "(N) A hag in folklore"],
"crook": ["(N) A criminal or swindler", "(N) A curved tool or staff"],
"croon": ["(V) To sing softly and smoothly", "(N) A gentle, melodic song"],
"crop": ["(N) A cultivated plant harvest", "(V) To cut short or trim"],
"cross": ["(N) A symbol of intersecting lines", "(V) To go from one side to another"],
"crotchet": ["(N) A quarter note in music", "(N) An odd or stubborn notion"],
"crouch": ["(V) To bend low with limbs close", "(N) A squatting posture"],
"crow": ["(N) A black bird known for cawing", "(V) To boast loudly"],
"crowd": ["(N) A large group of people", "(V) To press closely together"],
"crown": ["(N) A royal headpiece", "(V) To declare someone a champion"],
"crucial": ["(Adj) Extremely important", "(Adj) Decisive or critical"],
"crude": ["(Adj) In a raw or unrefined state", "(Adj) Lacking tact or polish"],
"cruel": ["(Adj) Willfully causing pain", "(Adj) Harsh or severe"],
"cruise": ["(V) To travel smoothly at a steady speed", "(N) A pleasure voyage"],
"crumb": ["(N) A small fragment of bread", "(V) To break into tiny pieces"],
"crumble": ["(V) To fall apart into small pieces", "(N) A baked dessert with a crumb topping"],
"crunch": ["(V) To crush with a crackling sound", "(N) A critical moment or shortage"],
"crusade": ["(N) A vigorous campaign for a cause", "(V) To fight passionately for something"],
"crush": ["(V) To press or squeeze with force", "(N) A strong but temporary infatuation"],
"crust": ["(N) The hard outer layer of bread or earth", "(V) To form a hardened surface"],
"crux": ["(N) The central or most important point", "(N) A difficult or puzzling problem"],
"cry": ["(V) To shed tears", "(N) A loud call or shout"],
"crypt": ["(N) An underground burial chamber", "(N) A hidden or secret vault"],
"cryptic": ["(Adj) Mysterious or obscure", "(Adj) Having a hidden meaning"],
"crystal": ["(N) A clear, transparent mineral", "(Adj) Extremely clear or sparkling"],
"cub": ["(N) A young carnivorous mammal", "(N) A novice or beginner"],
"cubby": ["(N) A small storage compartment", "(N) A cozy nook or recess"],
"cubbyhole": ["(N) A tiny enclosed space", "(N) A small compartment for storage"],
"cube": ["(N) A solid with six equal square faces", "(V) To cut into small square pieces"],
"cuckoo": ["(N) A bird known for laying eggs in other nests", "(Adj) Silly or crazy (informal)"],
"cucumber": ["(N) A long green vegetable", "(N) A plant producing such fruit"],
"cudgel": ["(N) A short, thick club", "(V) To beat with a heavy stick"],
"cuff": ["(N) The end of a sleeve", "(V) To strike lightly"],
"cull": ["(V) To select or gather", "(V) To remove inferior items"],
"culminate": ["(V) To reach the highest point", "(V) To conclude or finish"],
"culpable": ["(Adj) Deserving blame", "(Adj) Guilty of wrongdoing"],
"cultivate": ["(V) To prepare land for crops", "(V) To develop a skill or relationship"],
"culture": ["(N) The customs of a group", "(N) Artistic or intellectual expression"],
"cumbersome": ["(Adj) Large and difficult to carry", "(Adj) Complicated or unwieldy"],
"cumin": ["(N) A spice made from dried seeds", "(N) A plant producing aromatic seeds"],
"cunning": ["(Adj) Clever in a deceptive way", "(N) Skill in achieving goals by trickery"],
"cup": ["(N) A small drinking vessel", "(V) To shape hands like a bowl"],
"cupboard": ["(N) A cabinet for storage", "(N) A closet with shelves"],
"curb": ["(V) To restrain or control", "(N) A raised edge along a street"],
"curd": ["(N) The thick part of milk that forms cheese", "(N) A dairy product separated from whey"],
"cure": ["(V) To heal or restore health", "(N) A remedy or solution"],
"curio": ["(N) A rare or unusual object", "(N) A collectible item"],
"curious": ["(Adj) Eager to know or learn", "(Adj) Strange or unusual"],
"curl": ["(V) To form into a spiral shape", "(N) A ringlet of hair"],
"currant": ["(N) A small dried grape", "(N) A berry-producing shrub"],
"current": ["(Adj) Happening now", "(N) A flow of water, air, or electricity"],
"curry": ["(N) A spiced dish", "(V) To groom a horse with a comb"],
"curse": ["(N) A spoken wish for harm", "(V) To swear or speak angrily"],
"curtail": ["(V) To cut short or reduce", "(V) To limit or restrict"],
"curve": ["(N) A smoothly bending line", "(V) To bend without angles"],
"cushion": ["(N) A soft padded support", "(V) To soften the impact of something"],
"custard": ["(N) A sweet, creamy dessert", "(N) A mixture of milk, eggs, and sugar"],
"custom": ["(N) A traditional practice", "(Adj) Made to order"],
"cut": ["(V) To divide with a sharp tool", "(N) A reduction or wound"],
"cutlass": ["(N) A short, curved sword", "(N) A naval weapon used in boarding actions"],
"cutlet": ["(N) A small slice of meat", "(N) A breaded and fried meat portion"],
"cuttlefish": ["(N) A marine mollusk with ink sacs", "(N) A cephalopod related to squid"],
"cycle": ["(N) A repeating series of events", "(V) To ride a bicycle"],
"cypress": ["(N) A coniferous tree with scale-like leaves", "(N) Wood from such a tree"],
"czar": ["(N) A Russian emperor", "(N) A person with great authority"],
"dabble": ["(V) To take part superficially", "(V) To splash or play in water"],
"dachshund": ["(N) A small long-bodied dog breed", "(N) A hound with short legs"],
"daffodil": ["(N) A yellow spring flower", "(N) A plant with a trumpet-shaped bloom"],
"daffodilwood": ["(N) Wood from trees associated with daffodils (poetic)", "(N) A fanciful term for springtime timber"],
"daffy": ["(Adj) Silly or foolish", "(Adj) Eccentric in a harmless way"],
"daft": ["(Adj) Absurd or ridiculous", "(Adj) Slightly crazy (informal)"],
"dagger": ["(N) A short pointed knife", "(N) A symbol indicating danger or death"],
"daily": ["(Adj) Happening every day", "(N) A newspaper published each day"],
"dainty": ["(Adj) Delicately small and pretty", "(N) A small, tasty treat"],
"dairy": ["(N) A place where milk is processed", "(Adj) Made from milk"],
"dais": ["(N) A raised platform", "(N) A stage for speakers or honored guests"],
"daisy": ["(N) A common white-petaled flower", "(N) A plant of the aster family"],
"dale": ["(N) A valley", "(N) A broad, open area of low land"],
"dalliance": ["(N) A brief romantic involvement", "(N) A period of playful behavior"],
"dam": ["(N) A barrier built to hold back water", "(V) To block or obstruct"],
"damage": ["(N) Harm or injury", "(V) To cause loss or destruction"],
"dampen": ["(V) To make slightly wet", "(V) To reduce enthusiasm"],
"damper": ["(N) A device that reduces vibration or noise", "(N) A mechanism controlling airflow"],
"damsel": ["(N) A young unmarried woman", "(N) A maiden in old literature"],
"dance": ["(V) To move rhythmically to music", "(N) A social event with dancing"],
"dandelion": ["(N) A yellow-flowered weed", "(N) A plant with fluffy seed heads"],
"dander": ["(N) Loose skin flakes from animals", "(N) Anger or irritation (informal)"],
"dandle": ["(V) To bounce a child playfully", "(V) To pamper or fondle"],
"dank": ["(Adj) Unpleasantly damp", "(Adj) Chilly and musty"],
"dapper": ["(Adj) Neat and stylish in appearance", "(Adj) Trim and well-groomed"],
"dare": ["(V) To challenge boldly", "(N) A test of courage"],
"dark": ["(Adj) Without light", "(N) The absence of illumination"],
"darken": ["(V) To make darker", "(V) To become gloomy or somber"],
"darling": ["(N) A beloved person", "(Adj) Charming or endearing"],
"darn": ["(V) To mend by weaving thread", "(N) A mild exclamation"],
"dart": ["(N) A small pointed missile", "(V) To move suddenly and quickly"],
"dash": ["(V) To run or move quickly", "(N) A small amount added for flavor"],
"data": ["(N) Facts or information", "(N) Numerical or recorded details"],
"date": ["(N) A specific day of the month", "(N) A romantic meeting"],
"daub": ["(V) To smear or coat crudely", "(N) A patch of poorly applied paint"],
"dauber": ["(N) A person who paints unskillfully", "(N) A tool for applying paint or ink"],
"daughter": ["(N) A female child", "(N) A descendant in a family line"],
"daunt": ["(V) To intimidate or discourage", "(V) To lessen someone’s confidence"],
"dawdle": ["(V) To waste time by moving slowly", "(V) To linger without purpose"],
"dawn": ["(N) The first appearance of light", "(V) To begin to be understood"],
"daybreak": ["(N) The time when daylight first appears", "(N) Early morning twilight"],
"daydream": ["(V) To indulge in pleasant thoughts", "(N) A fantasy occurring while awake"],
"daylight": ["(N) Natural light from the sun", "(N) The period between sunrise and sunset"],
"daylily": ["(N) A flowering plant with blooms lasting one day", "(N) A hardy garden perennial"],
"daytime": ["(N) The period of the day when it is light", "(N) The hours between morning and evening"],
"daze": ["(V) To stun or confuse", "(N) A state of bewilderment"],
"dazzle": ["(V) To impress deeply", "(V) To blind temporarily with bright light"],
"deacon": ["(N) A church officer", "(N) A ministerial assistant"],
"dead": ["(Adj) No longer alive", "(N) A period of complete inactivity"],
"deaden": ["(V) To make less intense", "(V) To muffle or reduce sound"],
"deadline": ["(N) The latest time for completion", "(N) A fixed due date"],
"deadlock": ["(N) A standstill between opposing sides", "(V) To bring to a halt"],
"deaf": ["(Adj) Unable to hear", "(Adj) Unwilling to listen"],
"deal": ["(V) To distribute or give out", "(N) An agreement or arrangement"],
"dealer": ["(N) A person who buys and sells goods", "(N) The one who distributes cards in a game"],
"dean": ["(N) The head of a college or department", "(N) A senior official in a church"],
"dear": ["(Adj) Loved or cherished", "(N) A term of affection"],
"dearth": ["(N) A scarcity or lack", "(N) An insufficient supply"],
"death": ["(N) The end of life", "(N) The permanent cessation of vital functions"],
"debacle": ["(N) A sudden and disastrous failure", "(N) A complete collapse"],
"debase": ["(V) To reduce in quality or value", "(V) To lower in moral character"],
"debatable": ["(Adj) Open to question or dispute", "(Adj) Not certain or settled"],
"debate": ["(N) A formal discussion", "(V) To argue opposing viewpoints"],
"debauch": ["(V) To corrupt morally", "(V) To indulge in excessive pleasures"],
"debilitate": ["(V) To weaken severely", "(V) To impair strength or vitality"],
"debility": ["(N) Physical weakness", "(N) A state of frailty or feebleness"],
"debit": ["(N) An entry recording an amount owed", "(V) To charge to an account"],
"debonair": ["(Adj) Confident, stylish, and charming", "(Adj) Suave in manner"],
"debrief": ["(V) To question after a mission", "(V) To gather information from someone’s experience"],
"debris": ["(N) Scattered fragments of something broken", "(N) Rubble or remains"],
"debt": ["(N) Something owed", "(N) A financial obligation"],
"debunk": ["(V) To expose as false", "(V) To disprove exaggerated claims"],
"debut": ["(N) A first public appearance", "(V) To appear for the first time"],
"decade": ["(N) A period of ten years", "(N) A ten-year span in history"],
"decadent": ["(Adj) Luxuriously self-indulgent", "(Adj) Morally declining or corrupt"],
"decamp": ["(V) To depart suddenly", "(V) To leave a place quickly and secretly"],
"decant": ["(V) To pour off liquid gently", "(V) To transfer wine to separate sediment"],
"decay": ["(V) To rot or decompose", "(N) A gradual decline in strength"],
"deceit": ["(N) The act of deceiving", "(N) A dishonest trick or lie"],
"deceive": ["(V) To mislead or trick", "(V) To cause someone to believe something untrue"],
"december": ["(N) The twelfth month of the year", "(N) The final period of a calendar cycle"],
"decency": ["(N) Behavior conforming to moral standards", "(N) Modesty or propriety"],
"decent": ["(Adj) Respectable and proper", "(Adj) Fairly good or adequate"],
"decentralize": ["(V) To distribute power away from a central authority", "(V) To reorganize into smaller units"],
"deception": ["(N) The act of deceiving", "(N) A false impression or trick"],
"decibel": ["(N) A unit for measuring sound intensity", "(N) A logarithmic scale of loudness"],
"decide": ["(V) To make a choice", "(V) To settle a question or dispute"],
"decimal": ["(Adj) Based on the number ten", "(N) A fraction written with a point"],
"decimate": ["(V) To destroy a large portion of", "(V) To drastically reduce in number"],
"decipher": ["(V) To interpret or decode", "(V) To make sense of unclear writing"],
"decision": ["(N) A choice made after consideration", "(N) A conclusion reached"],
"deck": ["(N) A platform or floor on a ship", "(V) To decorate or adorn"],
"declaim": ["(V) To speak loudly and theatrically", "(V) To deliver a formal speech"],
"declare": ["(V) To announce formally", "(V) To state clearly and openly"],
"decline": ["(V) To decrease or diminish", "(V) To politely refuse"],
"decode": ["(V) To convert into understandable form", "(V) To decipher a coded message"],
"decompose": ["(V) To break down into simpler parts", "(V) To rot or decay"],
"decorate": ["(V) To make something look more attractive", "(V) To award a medal to someone"],
"decorous": ["(Adj) Proper and polite", "(Adj) Marked by good taste"],
"decoy": ["(N) A lure used to attract animals", "(V) To entice into a trap"],
"decrease": ["(V) To become smaller", "(N) A reduction in amount"],
"decree": ["(N) An official order", "(V) To command formally"],
"dedicate": ["(V) To devote to a purpose", "(V) To inscribe a work to someone"],
"deduce": ["(V) To infer from evidence", "(V) To reach a logical conclusion"],
"deduct": ["(V) To subtract from a total", "(V) To take away an amount"],
"deed": ["(N) An action or accomplishment", "(N) A legal document transferring property"],
"deem": ["(V) To judge or consider", "(V) To regard in a particular way"],
"deep": ["(Adj) Extending far down or in", "(N) A vast or profound area"],
"deepen": ["(V) To make deeper", "(V) To intensify or strengthen"],
"deer": ["(N) A hoofed grazing animal", "(N) A member of the Cervidae family"],
"deface": ["(V) To damage the surface of", "(V) To spoil the appearance of"],
"defame": ["(V) To harm someone’s reputation", "(V) To spread damaging statements"],
"default": ["(N) Failure to fulfill an obligation", "(V) To revert to a standard setting"],
"defeat": ["(V) To win a victory over", "(N) A loss or failure"],
"defect": ["(N) An imperfection or flaw", "(V) To abandon allegiance"],
"defend": ["(V) To protect from harm", "(V) To justify or support"],
"defense": ["(N) Protection from attack", "(N) The act of resisting an opponent"],
"defer": ["(V) To postpone or delay", "(V) To yield respectfully to another"],
"deference": ["(N) Respectful submission", "(N) Courteous regard for others"],
"defiance": ["(N) Open resistance", "(N) Bold disobedience"],
"defiant": ["(Adj) Boldly resistant", "(Adj) Showing open disobedience"],
"deficiency": ["(N) A lack or shortage", "(N) A failing or weakness"],
"deficit": ["(N) An amount by which something is less than required", "(N) A financial shortfall"],
"define": ["(V) To state the meaning of a word", "(V) To outline clearly"],
"definite": ["(Adj) Clearly stated or decided", "(Adj) Precise and exact"],
"definition": ["(N) A statement of meaning", "(N) The clarity of an image or sound"],
"deflate": ["(V) To release air or gas", "(V) To reduce confidence or pride"],
"deflect": ["(V) To cause to change direction", "(V) To ward off or turn aside"],
"defog": ["(V) To remove condensation", "(V) To clear a foggy surface"],
"deforest": ["(V) To clear trees from an area", "(V) To remove forest cover"],
"deform": ["(V) To distort the shape of", "(V) To spoil the appearance of"],
"defraud": ["(V) To cheat someone of money", "(V) To obtain by deception"],
"defray": ["(V) To pay the cost of", "(V) To cover expenses"],
"defrost": ["(V) To thaw or remove ice", "(V) To warm up frozen material"],
"deft": ["(Adj) Skillful and quick", "(Adj) Demonstrating nimble ability"],
"defunct": ["(Adj) No longer existing or functioning", "(Adj) Dead or obsolete"],
"defuse": ["(V) To remove the fuse from a bomb", "(V) To reduce tension or danger"],
"defy": ["(V) To resist boldly", "(V) To challenge authority"],
"degenerate": ["(V) To decline in quality", "(Adj) Morally corrupt or degraded"],
"degrade": ["(V) To treat with disrespect", "(V) To reduce in rank or quality"],
"degree": ["(N) A unit of measurement", "(N) A level of academic achievement"],
"dehydrate": ["(V) To remove water from", "(V) To lose moisture"],
"deify": ["(V) To worship as a god", "(V) To idealize excessively"],
"deign": ["(V) To do something considered beneath one’s dignity", "(V) To condescend reluctantly"],
"deity": ["(N) A god or goddess", "(N) A divine being"],
"deject": ["(V) To make sad or dispirited", "(V) To lower someone’s spirits"],
"delay": ["(V) To postpone or slow down", "(N) A period of waiting"],
"delegate": ["(N) A representative or envoy", "(V) To assign responsibility"],
"delete": ["(V) To remove or erase", "(V) To strike out text"],
"deli": ["(N) A store selling prepared foods", "(N) A section of a grocery with meats and cheeses"],
"deliberate": ["(Adj) Done intentionally", "(V) To consider carefully"],
"delicacy": ["(N) A rare or expensive food", "(N) Fineness or fragility"],
"delicate": ["(Adj) Easily broken or damaged", "(Adj) Fine and subtle in quality"],
"delight": ["(N) Great pleasure", "(V) To please greatly"],
"delimit": ["(V) To set boundaries", "(V) To define limits clearly"],
"delinquent": ["(Adj) Neglectful of duty", "(N) A young offender"],
"delineate": ["(V) To describe precisely", "(V) To outline or depict"],
"delirious": ["(Adj) In a disturbed mental state", "(Adj) Wildly excited"],
"deliver": ["(V) To bring or hand over", "(V) To give a speech or performance"],
"delta": ["(N) A triangular river mouth", "(N) The fourth letter of the Greek alphabet"],
"delude": ["(V) To mislead or deceive", "(V) To cause false belief"],
"deluge": ["(N) A severe flood", "(V) To overwhelm with a large amount"],
"delusion": ["(N) A false belief", "(N) A mistaken conviction despite evidence"],
"delve": ["(V) To dig or search deeply", "(V) To investigate thoroughly"],
"demagogue": ["(N) A leader who gains power by appealing to emotions", "(N) A manipulative political agitator"],
"demean": ["(V) To lower in dignity", "(V) To degrade or humiliate"],
"demeanor": ["(N) Outward behavior", "(N) Conduct or manner"],
"demented": ["(Adj) Mentally ill or insane", "(Adj) Behaving irrationally"],
"dementia": ["(N) A decline in cognitive ability", "(N) A disorder affecting memory and reasoning"],
"demerit": ["(N) A mark against someone for misconduct", "(N) A fault or weakness"],
"demise": ["(N) Death or end", "(N) The transfer of property by will"],
"demolish": ["(V) To destroy completely", "(V) To tear down"],
"demonstrate": ["(V) To show clearly", "(V) To protest publicly"],
"demote": ["(V) To reduce in rank", "(V) To assign to a lower position"],
"demur": ["(V) To raise objections", "(N) A hesitation or protest"],
"den": ["(N) A wild animal’s lair", "(N) A small, cozy room"],
"denote": ["(V) To indicate or signify", "(V) To be a name for something"],
"denounce": ["(V) To publicly condemn", "(V) To accuse formally"],
"dense": ["(Adj) Thick or crowded", "(Adj) Difficult to understand"],
"density": ["(N) The degree of compactness", "(N) Mass per unit volume"],
"dent": ["(N) A small hollow caused by pressure", "(V) To make a slight depression"],
"dentist": ["(N) A doctor specializing in teeth", "(N) A practitioner of dental medicine"],
"deny": ["(V) To refuse to admit truth", "(V) To withhold something requested"],
"depart": ["(V) To leave or go away", "(V) To deviate from a standard"],
"department": ["(N) A division of an organization", "(N) A specialized area of activity"],
"departure": ["(N) The act of leaving", "(N) A deviation from the norm"],
"depend": ["(V) To rely on", "(V) To be determined by circumstances"],
"depict": ["(V) To represent visually", "(V) To describe in words"],
"deplete": ["(V) To use up resources", "(V) To reduce significantly"],
"deplore": ["(V) To express strong disapproval", "(V) To regret deeply"],
"deploy": ["(V) To position strategically", "(V) To spread out for action"],
"deport": ["(V) To expel from a country", "(V) To behave in a particular manner"],
"depose": ["(V) To remove from office", "(V) To give sworn testimony"],
"deposit": ["(N) Money placed in a bank", "(V) To put down or store"],
"depot": ["(N) A storage place or warehouse", "(N) A station for transport"],
"deprave": ["(V) To corrupt morally", "(V) To lead into wickedness"],
"deprecate": ["(V) To express disapproval of", "(V) To belittle or downplay"],
"depress": ["(V) To make sad or gloomy", "(V) To press down physically"],
"deprive": ["(V) To take something away", "(V) To deny possession or use"],
"depth": ["(N) The distance downward or inward", "(N) Intensity or complexity"],
"deputy": ["(N) A second-in-command", "(N) A representative with authority"],
"derail": ["(V) To cause a train to leave the tracks", "(V) To obstruct progress"],
"derange": ["(V) To disturb the order of", "(V) To make insane"],
"derelict": ["(Adj) Abandoned or neglected", "(N) A homeless or neglected person"],
"derive": ["(V) To obtain from a source", "(V) To originate from"],
"derogatory": ["(Adj) Expressing low opinion", "(Adj) Disparaging or insulting"],
"descend": ["(V) To move downward", "(V) To originate from an ancestor"],
"describe": ["(V) To give an account of", "(V) To explain in detail"],
"description": ["(N) A spoken or written account", "(N) A detailed portrayal"],
"descry": ["(V) To catch sight of", "(V) To detect from afar"],
"desert": ["(N) A dry, barren region", "(V) To abandon or leave behind"],
"deserve": ["(V) To be worthy of", "(V) To merit or earn"],
"design": ["(V) To plan or create", "(N) A decorative or functional pattern"],
"desire": ["(N) A strong feeling of wanting", "(V) To long for or wish"],
"desk": ["(N) A piece of furniture for writing", "(N) A workstation or office table"],
"desolate": ["(Adj) Empty and bleak", "(V) To make a place barren"],
"despair": ["(N) Complete loss of hope", "(V) To lose all hope"],
"despatch": ["(V) To send off quickly", "(N) A message sent with urgency"],
"desperado": ["(N) A bold outlaw", "(N) A reckless criminal"],
"desperate": ["(Adj) Feeling hopeless", "(Adj) Involving extreme measures"],
"despise": ["(V) To feel deep contempt for", "(V) To regard with disgust"],
"despite": ["(Prep) In spite of", "(N) Contempt or disdain"],
"despoil": ["(V) To plunder or rob", "(V) To strip of possessions"],
"despond": ["(V) To lose confidence or hope", "(V) To become dejected"],
"despot": ["(N) A ruler with absolute power", "(N) A tyrannical leader"],
"destiny": ["(N) A predetermined course of events", "(N) Fate or inevitable outcome"],
"destroy": ["(V) To ruin completely", "(V) To demolish or annihilate"],
"detach": ["(V) To separate from something", "(V) To disengage or remove"],
"detail": ["(N) A small part of something", "(V) To describe thoroughly"],
"detain": ["(V) To keep in custody", "(V) To delay or hold back"],
"detect": ["(V) To discover or identify", "(V) To notice something hidden"],
"detention": ["(N) The act of holding someone", "(N) Punishment requiring students to stay after school"],
"deter": ["(V) To discourage from acting", "(V) To prevent through fear or doubt"],
"detergent": ["(N) A cleaning agent", "(Adj) Having cleansing power"],
"determine": ["(V) To decide or conclude", "(V) To establish firmly"],
"detest": ["(V) To hate intensely", "(V) To feel strong aversion toward"],
"detonate": ["(V) To explode violently", "(V) To trigger an explosion"],
"detour": ["(N) A longer route taken to avoid something", "(V) To take an alternate path"],
"detox": ["(V) To remove toxins from the body", "(N) A cleansing process"],
"deuce": ["(N) The number two in cards or dice", "(N) A tied score in tennis"],
"devastate": ["(V) To cause great destruction", "(V) To overwhelm with grief"],
"develop": ["(V) To grow or expand", "(V) To create or improve"],
"deviate": ["(V) To depart from a path", "(V) To differ from expectations"],
"device": ["(N) A tool or instrument", "(N) A machine designed for a specific purpose"],
"devil": ["(N) An evil supernatural being", "(V) To season food with spices (culinary)"],
"devise": ["(V) To plan or invent", "(V) To think up through careful thought"],
"devoid": ["(Adj) Completely lacking", "(Adj) Empty or without content"],
"devote": ["(V) To give time or effort to something", "(V) To dedicate oneself fully"],
"devour": ["(V) To eat greedily", "(V) To consume eagerly or destructively"],
"devout": ["(Adj) Deeply religious", "(Adj) Sincere and earnest in devotion"],
"dew": ["(N) Moisture condensed on cool surfaces", "(N) Tiny droplets formed overnight"],
"dewdrop": ["(N) A small drop of dew", "(N) A bead of moisture on plants"],
"dexterity": ["(N) Skill in using hands or body", "(N) Mental agility or cleverness"],
"dexterous": ["(Adj) Skillful with hands", "(Adj) Demonstrating agility or precision"],
"diadem": ["(N) A jeweled crown or headband", "(N) A symbol of royal authority"],
"diagnose": ["(V) To identify a condition or problem", "(V) To determine the cause of something"],
"diagram": ["(N) A simplified drawing showing structure", "(V) To represent with a diagram"],
"dial": ["(N) A face of a clock or instrument", "(V) To call a number on a phone"],
"dialogue": ["(N) A conversation between two or more people", "(N) An exchange of ideas"],
"diameter": ["(N) A straight line through a circle’s center", "(N) The width of a circular object"],
"diamond": ["(N) A precious gemstone", "(N) A shape with four equal sides at angles"],
"diaphanous": ["(Adj) Light and translucent", "(Adj) Delicate and sheer"],
"diary": ["(N) A daily written record", "(N) A journal of personal experiences"],
"dibble": ["(N) A pointed gardening tool", "(V) To make holes in soil for planting"],
"dice": ["(N) Small cubes used in games", "(V) To cut into small cubes"],
"dictate": ["(V) To speak for transcription", "(V) To command or order"],
"dictator": ["(N) A ruler with absolute power", "(N) A person who imposes their will on others"],
"diction": ["(N) Word choice in speech or writing", "(N) Clarity of pronunciation"],
"dictionary": ["(N) A reference book of words and meanings", "(N) A list of terms with definitions"],
"didactic": ["(Adj) Intended to teach", "(Adj) Moralizing or instructive"],
"die": ["(V) To cease living", "(N) A tool for shaping or cutting material"],
"diet": ["(N) The food one regularly eats", "(V) To restrict food intake"],
"differ": ["(V) To be unlike", "(V) To disagree in opinion"],
"different": ["(Adj) Not the same", "(Adj) Distinct or separate"],
"diffident": ["(Adj) Shy or lacking confidence", "(Adj) Reserved in manner"],
"diffuse": ["(V) To spread widely", "(Adj) Not concentrated or focused"],
"dig": ["(V) To break up soil", "(N) A sarcastic remark (informal)"],
"digestion": ["(N) The process of breaking down food", "(N) The ability to understand ideas"],
"digit": ["(N) A numeral from 0 to 9", "(N) A finger or toe"],
"dignify": ["(V) To make something seem worthy", "(V) To honor or elevate"],
"dignity": ["(N) A sense of self-respect", "(N) Worthiness or nobility"],
"dilate": ["(V) To widen or expand", "(V) To speak or write at length"],
"diligent": ["(Adj) Hard-working and careful", "(Adj) Showing steady effort"],
"dill": ["(N) An aromatic herb", "(N) The seeds or leaves used in cooking"],
"dilute": ["(V) To make weaker by adding liquid", "(V) To reduce intensity"],
"dim": ["(Adj) Not bright or clear", "(V) To make less intense"],
"dime": ["(N) A U.S. coin worth ten cents", "(N) A small amount of money (informal)"],
"dimension": ["(N) A measurable extent", "(N) An aspect or feature"],
"diminish": ["(V) To make smaller", "(V) To lessen in importance"],
"dimple": ["(N) A small indentation in the skin", "(V) To form small hollows"],
"din": ["(N) A loud, continuous noise", "(V) To make a persistent clamor"],
"dine": ["(V) To eat dinner", "(V) To have a formal meal"],
"dinghy": ["(N) A small boat", "(N) A lightweight rowboat or sailboat"],
"dingy": ["(Adj) Dirty or discolored", "(Adj) Shabby or dull"],
"dinner": ["(N) The main meal of the day", "(N) A formal evening meal"],
"diode": ["(N) An electronic component allowing one-way current", "(N) A semiconductor device"],
"diorama": ["(N) A miniature 3D scene", "(N) A model depicting a landscape or event"],
"dioxide": ["(N) A compound with two oxygen atoms", "(N) A gas such as carbon dioxide"],
"diploma": ["(N) A certificate of graduation", "(N) A document conferring academic achievement"],
"diplomat": ["(N) A representative managing international relations", "(N) A tactful negotiator"],
"dire": ["(Adj) Extremely serious or urgent", "(Adj) Warning of disaster"],
"direct": ["(V) To guide or manage", "(Adj) Straightforward or immediate"],
"direction": ["(N) A course or path", "(N) Instructions for action"],
"dirge": ["(N) A mournful song", "(N) A funeral lament"],
"dirt": ["(N) Loose soil or earth", "(N) Gossip or scandal (informal)"],
"disable": ["(V) To make unable to function", "(V) To incapacitate"],
"disagree": ["(V) To have different opinions", "(V) To conflict or be inconsistent"],
"disallow": ["(V) To refuse permission", "(V) To reject as invalid"],
"disappear": ["(V) To cease to be visible", "(V) To vanish or fade away"],
"disarm": ["(V) To remove weapons", "(V) To reduce hostility"],
"disarray": ["(N) A state of disorder", "(V) To throw into confusion"],
"disaster": ["(N) A sudden catastrophe", "(N) A complete failure"],
"disband": ["(V) To break up an organization", "(V) To dissolve a group"],
"disburse": ["(V) To pay out money", "(V) To distribute funds"],
"discard": ["(V) To throw away", "(N) Something cast aside"],
"discern": ["(V) To perceive clearly", "(V) To distinguish with effort"],
"discharge": ["(V) To release or dismiss", "(N) A flow or outpouring"],
"discipline": ["(N) Training to develop self-control", "(V) To punish or correct"],
"disclaim": ["(V) To deny responsibility", "(V) To renounce a claim"],
"disclose": ["(V) To reveal or make known", "(V) To uncover information"],
"discolor": ["(V) To change color", "(V) To stain or fade"],
"discomfit": ["(V) To make uneasy or embarrassed", "(V) To frustrate plans"],
"disconnect": ["(V) To detach or separate", "(N) A lack of connection"],
"discontent": ["(N) Dissatisfaction", "(Adj) Unhappy or restless"],
"discord": ["(N) Lack of harmony", "(N) Disagreement or conflict"],
"discount": ["(N) A reduction in price", "(V) To disregard or minimize"],
"discourage": ["(V) To deter or dissuade", "(V) To deprive of confidence"],
"discover": ["(V) To find unexpectedly", "(V) To learn something new"],
"discredit": ["(V) To harm someone’s reputation", "(N) Loss of trust or respect"],
"discreet": ["(Adj) Careful in speech or action", "(Adj) Tactful and prudent"],
"discrete": ["(Adj) Separate and distinct", "(Adj) Individually different"],
"discriminate": ["(V) To distinguish differences", "(V) To treat unfairly based on prejudice"],
"discuss": ["(V) To talk about in detail", "(V) To consider from various angles"],
"disdain": ["(N) Contempt or scorn", "(V) To regard as unworthy"],
"disembark": ["(V) To leave a ship or vehicle", "(V) To go ashore"],
"disengage": ["(V) To release from attachment", "(V) To withdraw involvement"],
"disfigure": ["(V) To spoil the appearance of", "(V) To mar or deform"],
"disgorge": ["(V) To vomit or eject forcefully", "(V) To release contents"],
"disgrace": ["(N) Loss of honor", "(V) To bring shame upon"],
"disguise": ["(V) To conceal identity", "(N) A costume or mask"],
"disgust": ["(N) Strong aversion", "(V) To sicken or offend"],
"dish": ["(N) A shallow container for food", "(V) To gossip or criticize (informal)"],
"dishearten": ["(V) To discourage deeply", "(V) To lower morale"],
"dishonor": ["(N) Loss of respect", "(V) To bring shame upon"],
"disillusion": ["(V) To free from false beliefs", "(N) A loss of idealism"],
"disinfect": ["(V) To clean of harmful microbes", "(V) To sterilize"],
"disinherit": ["(V) To deprive of inheritance", "(V) To exclude from succession"],
"disintegrate": ["(V) To break into pieces", "(V) To decay or fall apart"],
"disinter": ["(V) To dig up a buried body", "(V) To bring to light"],
"disjoint": ["(V) To separate at the joints", "(Adj) Lacking coherence"],
"disk": ["(N) A flat, circular object", "(N) A computer storage medium"],
"dislike": ["(V) To feel aversion toward", "(N) A feeling of distaste"],
"dislocate": ["(V) To put out of place", "(V) To disrupt normal arrangement"],
"dislodge": ["(V) To force out of position", "(V) To remove from a place"],
"dismal": ["(Adj) Depressingly gloomy", "(Adj) Poor in quality"],
"dismantle": ["(V) To take apart", "(V) To strip of equipment"],
"dismay": ["(N) Sudden disappointment", "(V) To alarm or upset"],
"dismiss": ["(V) To send away", "(V) To reject or disregard"],
"dismount": ["(V) To get off a horse or bicycle", "(V) To remove from support"],
"disobey": ["(V) To fail to follow rules", "(V) To defy authority"],
"disorder": ["(N) A state of confusion", "(N) A medical abnormality"],
"disown": ["(V) To refuse to acknowledge", "(V) To deny responsibility for"],
"disparage": ["(V) To belittle or criticize", "(V) To speak of as unimportant"],
"disparate": ["(Adj) Fundamentally different", "(Adj) Not allowing comparison"],
"disparity": ["(N) A great difference", "(N) Inequality or imbalance"],
"dispatch": ["(V) To send off quickly", "(N) A message or report"],
"dispel": ["(V) To drive away", "(V) To eliminate doubts or fears"],
"dispense": ["(V) To distribute or give out", "(V) To exempt from a rule"],
"disperse": ["(V) To scatter in different directions", "(V) To distribute widely"],
"displace": ["(V) To move from usual position", "(V) To force out of place"],
"display": ["(V) To show or exhibit", "(N) A visual presentation"],
"displease": ["(V) To cause dissatisfaction", "(V) To offend or annoy"],
"disport": ["(V) To amuse oneself", "(V) To frolic or play"],
"dispose": ["(V) To get rid of", "(V) To incline or persuade"],
"dispute": ["(N) A disagreement", "(V) To argue or contest"],
"disquiet": ["(N) A feeling of anxiety", "(V) To make uneasy"],
"disregard": ["(V) To ignore or pay no attention", "(N) Lack of consideration"],
"disrobe": ["(V) To remove clothing", "(V) To undress completely"],
"disrupt": ["(V) To interrupt or disturb", "(V) To cause disorder"],
"dissatisfy": ["(V) To fail to please", "(V) To leave someone unfulfilled"],
"dissect": ["(V) To cut apart for study", "(V) To analyze in detail"],
"dissemble": ["(V) To conceal true motives", "(V) To disguise feelings"],
"disseminate": ["(V) To spread widely", "(V) To distribute information"],
"dissent": ["(N) Disagreement with authority", "(V) To hold a differing opinion"],
"dissertation": ["(N) A long academic paper", "(N) A formal written argument"],
"disservice": ["(N) A harmful action", "(N) Something that damages reputation"],
"dissident": ["(N) A person who opposes authority", "(Adj) Disagreeing with official policy"],
"dissimilar": ["(Adj) Not alike", "(Adj) Different in nature"],
"dissipate": ["(V) To scatter or disperse", "(V) To waste foolishly"],
"dissolve": ["(V) To melt into liquid", "(V) To end or terminate"],
"dissonance": ["(N) Lack of harmony", "(N) Conflict between ideas"],
"dissuade": ["(V) To persuade not to do something", "(V) To discourage through reasoning"],
"distance": ["(N) The space between two points", "(V) To create emotional separation"],
"distend": ["(V) To swell or expand", "(V) To stretch outward"],
"distinct": ["(Adj) Clearly different", "(Adj) Easily recognizable"],
"distinguish": ["(V) To tell apart", "(V) To recognize as different"],
"distort": ["(V) To twist out of shape", "(V) To misrepresent facts"],
"distract": ["(V) To divert attention", "(V) To disturb concentration"],
"distress": ["(N) Extreme anxiety or pain", "(V) To cause suffering"],
"distribute": ["(V) To hand out or deliver", "(V) To spread over an area"],
"distrust": ["(N) Lack of trust", "(V) To doubt someone’s honesty"],
"disturb": ["(V) To interrupt or bother", "(V) To upset normal function"],
"ditch": ["(N) A narrow trench", "(V) To abandon or discard"],
"dither": ["(V) To hesitate nervously", "(N) A state of indecision"],
"ditto": ["(N) The same thing again", "(V) To repeat exactly"],
"ditty": ["(N) A short, simple song", "(N) A light, catchy tune"],
"diverge": ["(V) To move apart", "(V) To differ in opinion"],
"diverse": ["(Adj) Showing variety", "(Adj) Composed of different elements"],
"divert": ["(V) To change direction", "(V) To entertain or amuse"],
"divide": ["(V) To separate into parts", "(N) A boundary or separation"],
"divine": ["(Adj) Heavenly or godlike", "(V) To foresee or predict"],
"division": ["(N) The act of separating", "(N) A mathematical operation"],
"divorce": ["(N) Legal dissolution of marriage", "(V) To separate completely"],
"dizzy": ["(Adj) Feeling unsteady", "(Adj) Causing a sensation of spinning"],
"do": ["(V) To perform an action", "(V) To accomplish or complete"],
"docile": ["(Adj) Easily managed or taught", "(Adj) Gentle and obedient"],
"doctor": ["(N) A medical professional", "(V) To alter or tamper with"],
"doctrine": ["(N) A set of beliefs", "(N) A principle taught by a group"],
"document": ["(N) A written record", "(V) To record information"],
"dodge": ["(V) To avoid by quick movement", "(N) A clever trick or evasion"],
"doe": ["(N) A female deer", "(N) A female of certain mammals"],
"dog": ["(N) A domesticated canine", "(V) To follow persistently"],
"dogged": ["(Adj) Stubbornly persistent", "(Adj) Determined despite difficulty"],
"dogma": ["(N) A principle held as unquestionable", "(N) A doctrine taught as true"],
"doily": ["(N) A decorative lace mat", "(N) A small ornamental covering"],
"dole": ["(N) Money given as charity", "(V) To distribute sparingly"],
"doll": ["(N) A child’s toy figure", "(V) To dress up attractively"],
"dollar": ["(N) A unit of currency", "(N) A basic monetary measure in several countries"],
"dollop": ["(N) A small lump or portion", "(V) To add casually in small amounts"],
"dolly": ["(N) A small platform on wheels", "(V) To move something using a dolly"],
"dolphin": ["(N) A highly intelligent marine mammal", "(N) A fast-swimming aquatic creature"],
"domain": ["(N) An area of control or knowledge", "(N) A territory governed by a ruler"],
"dome": ["(N) A rounded roof structure", "(N) A large, curved enclosure"],
"domestic": ["(Adj) Relating to the home", "(Adj) Tame or not wild"],
"domicile": ["(N) A place of residence", "(V) To establish a home"],
"dominant": ["(Adj) Most powerful or influential", "(N) A dominant genetic trait"],
"dominate": ["(V) To control or rule over", "(V) To be the most prominent"],
"don": ["(V) To put on clothing", "(N) A university teacher or leader"],
"donate": ["(V) To give as a gift or contribution", "(V) To provide without expecting return"],
"donkey": ["(N) A domesticated hoofed animal", "(N) A stubborn person (informal)"],
"donor": ["(N) A person who gives something", "(N) One who contributes money or organs"],
"doom": ["(N) Fate, often unpleasant", "(V) To condemn to a negative outcome"],
"door": ["(N) A hinged barrier for entry", "(N) An opportunity or access point"],
"dope": ["(N) Information or news (slang)", "(V) To administer drugs"],
"dormant": ["(Adj) Inactive but capable of awakening", "(Adj) Temporarily quiet or still"],
"dorsal": ["(Adj) Relating to the back of an organism", "(Adj) Positioned on the upper side"],
"dosage": ["(N) The amount of medicine to be taken", "(N) A prescribed quantity of a substance"],
"dose": ["(N) A measured amount of medicine", "(V) To administer a dose"],
"dote": ["(V) To show excessive love", "(V) To be overly fond of someone"],
"dotted": ["(Adj) Marked with dots", "(Adj) Spotted or speckled"],
"double": ["(Adj) Twice as much", "(V) To duplicate or fold over"],
"doubt": ["(N) A feeling of uncertainty", "(V) To question the truth of something"],
"dough": ["(N) A mixture of flour and liquid", "(N) Money (slang)"],
"douse": ["(V) To drench with liquid", "(V) To extinguish a flame"],
"dove": ["(N) A gentle bird symbolizing peace", "(N) A person favoring peaceful policies"],
"dovetail": ["(V) To fit together harmoniously", "(N) A joint used in carpentry"],
"down": ["(Adv) Toward a lower place", "(N) Soft fluffy feathers"],
"downcast": ["(Adj) Sad or discouraged", "(Adj) Directed downward"],
"downpour": ["(N) A heavy rainstorm", "(N) A sudden, intense rainfall"],
"downtown": ["(N) The central business district", "(Adj) Located in the city center"],
"dowry": ["(N) Property a bride brings to marriage", "(N) A gift given at a wedding"],
"doyle": ["(N) A surname", "(N) A reference to works by Arthur Conan Doyle"],
"doze": ["(V) To sleep lightly", "(N) A short nap"],
"drab": ["(Adj) Dull and lacking color", "(N) A dull, grayish color"],
"draft": ["(N) A preliminary version of writing", "(V) To prepare a first version"],
"drag": ["(V) To pull with effort", "(N) Something tedious or boring"],
"dragon": ["(N) A mythical fire-breathing creature", "(N) A fierce or intimidating person"],
"drain": ["(V) To remove liquid", "(N) A pipe that carries away water"],
"drake": ["(N) A male duck", "(N) A dragon in some folklore"],
"dram": ["(N) A small drink of liquor", "(N) A unit of weight"],
"drama": ["(N) A serious play or story", "(N) Emotional or intense events"],
"drastic": ["(Adj) Extreme or severe", "(Adj) Having a strong effect"],
"draw": ["(V) To pull or sketch", "(N) A tie in a contest"],
"drawer": ["(N) A sliding storage compartment", "(N) A person who draws"],
"dread": ["(N) Great fear", "(V) To anticipate with anxiety"],
"dream": ["(N) Thoughts during sleep", "(V) To imagine or aspire"],
"dredge": ["(V) To scoop from the bottom of water", "(V) To coat food in flour"],
"dress": ["(N) A garment for women", "(V) To put on clothes"],
"dresser": ["(N) A piece of furniture with drawers", "(N) A person who assists with costumes"],
"drew": ["(V) Past tense of draw", "(V) Pulled or sketched"],
"dribble": ["(V) To let liquid fall in drops", "(V) To move a ball skillfully"],
"dried": ["(Adj) Without moisture", "(V) Past tense of dry"],
"drift": ["(V) To move slowly without direction", "(N) A pile formed by wind or water"],
"drill": ["(N) A tool for making holes", "(V) To practice repeatedly"],
"drink": ["(V) To swallow liquid", "(N) A beverage"],
"drip": ["(V) To fall in drops", "(N) A small drop of liquid"],
"drive": ["(V) To operate a vehicle", "(N) Motivation or energy"],
"drizzle": ["(N) Light rain", "(V) To pour in a thin stream"],
"droll": ["(Adj) Amusing in an odd way", "(N) A comical person"],
"drone": ["(N) A continuous low sound", "(V) To speak monotonously"],
"droop": ["(V) To hang downward", "(V) To lose spirit or strength"],
"drop": ["(N) A small amount of liquid", "(V) To let fall"],
"drought": ["(N) A prolonged lack of rain", "(N) A severe water shortage"],
"drove": ["(N) A herd or flock", "(V) Past tense of drive"],
"drown": ["(V) To die by submersion", "(V) To overwhelm with liquid"],
"drowse": ["(V) To be half-asleep", "(N) A light sleep"],
"drudge": ["(N) A person who does dull work", "(V) To do tedious labor"],
"drug": ["(N) A chemical used as medicine", "(V) To administer a drug"],
"drum": ["(N) A percussion instrument", "(V) To beat rhythmically"],
"drunk": ["(Adj) Intoxicated by alcohol", "(N) A person who is intoxicated"],
"dry": ["(Adj) Free from moisture", "(V) To remove liquid"],
"dual": ["(Adj) Having two parts", "(Adj) Double in nature"],
"dub": ["(V) To give a title or name", "(V) To add sound to film"],
"duck": ["(N) A waterfowl bird", "(V) To lower the head quickly"],
"duct": ["(N) A tube for air or liquid", "(V) To channel through a duct"],
"dude": ["(N) A man or guy (informal)", "(N) A stylish or refined man (old use)"],
"duel": ["(N) A formal fight between two people", "(V) To fight in a duel"],
"duet": ["(N) A performance by two people", "(N) A musical composition for two"],
"duff": ["(N) A pudding-like dessert", "(Adj) Useless or worthless (slang)"],
"dug": ["(V) Past tense of dig", "(N) A teat of a female mammal"],
"duke": ["(N) A nobleman of high rank", "(V) To fight (slang: duke it out)"],
"dull": ["(Adj) Not sharp or bright", "(V) To make less intense"],
"duly": ["(Adv) In a proper manner", "(Adv) At the expected time"],
"dumb": ["(Adj) Unable to speak", "(Adj) Foolish or stupid (informal)"],
"dummy": ["(N) A model or replica", "(N) A person acting as a stand-in"],
"dump": ["(V) To drop or dispose of", "(N) A place for waste"],
"dune": ["(N) A hill of sand", "(N) A ridge formed by wind"],
"dung": ["(N) Animal excrement", "(V) To fertilize with manure"],
"dungeon": ["(N) A dark underground prison", "(N) A strong, confining cell"],
"dunk": ["(V) To dip into liquid", "(N) A basketball shot pushing the ball downward"],
"dupe": ["(V) To deceive or trick", "(N) A person easily fooled"],
"duplicate": ["(V) To make an exact copy", "(N) A replica or double"],
"durable": ["(Adj) Able to withstand wear", "(Adj) Long-lasting or sturdy"],
"duration": ["(N) The length of time something lasts", "(N) A period of continued existence"],
"duress": ["(N) Threats used to force action", "(N) Coercion or pressure"],
"dusk": ["(N) The time just after sunset", "(N) Partial darkness"],
"dust": ["(N) Fine dry particles", "(V) To remove dust from surfaces"],
"dusty": ["(Adj) Covered with dust", "(Adj) Dull or muted in color"],
"duty": ["(N) A moral or legal obligation", "(N) A tax on imports"],
"dwarf": ["(N) A small mythical being", "(V) To make something seem small by comparison"],
"dwell": ["(V) To live in a place", "(V) To think or speak at length about something"],
"dwelling": ["(N) A place to live", "(N) A residence or home"],
"dwindle": ["(V) To shrink gradually", "(V) To diminish in size or amount"],
"dye": ["(N) A substance used to color materials", "(V) To apply color to something"],
"dyer": ["(N) A person who dyes cloth", "(N) Someone skilled in coloring materials"],
"dynamic": ["(Adj) Energetic and forceful", "(N) A driving force or factor"],
"dynamo": ["(N) A generator producing electricity", "(N) A very energetic person"],
"dynasty": ["(N) A succession of rulers from one family", "(N) A powerful family line"],
"dysfunction": ["(N) Impaired or abnormal functioning", "(N) A breakdown in normal operations"],
"eager": ["(Adj) Enthusiastic or impatiently desirous", "(Adj) Keenly interested"],
"eagle": ["(N) A large bird of prey", "(N) A symbol of strength and freedom"],
"ear": ["(N) The organ of hearing", "(N) The part of a plant that contains grain"],
"earl": ["(N) A British nobleman", "(N) A title ranking below marquess"],
"early": ["(Adj) Happening before expected", "(Adv) Before the usual time"],
"earn": ["(V) To receive as payment", "(V) To gain through effort"],
"earnest": ["(Adj) Serious and sincere", "(N) A token of good faith"],
"earring": ["(N) Jewelry worn on the ear", "(N) An ornament attached to the earlobe"],
"earth": ["(N) The planet we live on", "(N) Soil or ground"],
"earthbound": ["(Adj) Unable to fly", "(Adj) Practical or mundane"],
"earthquake": ["(N) A shaking of the ground", "(N) A sudden seismic disturbance"],
"earthy": ["(Adj) Relating to soil", "(Adj) Simple, natural, or coarse"],
"ease": ["(N) Freedom from difficulty", "(V) To make less severe"],
"east": ["(N) The direction of sunrise", "(Adj) Situated toward the east"],
"eastern": ["(Adj) Located in the east", "(Adj) Relating to eastern regions"],
"easy": ["(Adj) Not difficult", "(Adj) Relaxed or comfortable"],
"eat": ["(V) To consume food", "(V) To erode or wear away"],
"eaves": ["(N) The lower edges of a roof", "(N) Overhanging roof sections"],
"ebb": ["(V) To recede or diminish", "(N) The movement of the tide outward"],
"ebony": ["(N) A dark, dense wood", "(Adj) Deep black in color"],
"echo": ["(N) A reflected sound", "(V) To repeat or resound"],
"eclipse": ["(N) The blocking of one celestial body by another", "(V) To overshadow or surpass"],
"ecology": ["(N) The study of organisms and their environment", "(N) The relationship between living things and surroundings"],
"economy": ["(N) A system of production and consumption", "(N) Careful management of resources"],
"ecstasy": ["(N) Intense joy or delight", "(N) A trance-like emotional state"],
"eddy": ["(N) A circular movement of water or air", "(V) To swirl in a circular motion"],
"edge": ["(N) The boundary of a surface", "(V) To move gradually or cautiously"],
"edible": ["(Adj) Safe to eat", "(N) Something suitable for consumption"],
"edict": ["(N) An official order", "(N) A formal proclamation"],
"edify": ["(V) To instruct morally or intellectually", "(V) To improve knowledge or character"],
"edit": ["(V) To revise or correct", "(N) A change made to text or film"],
"edition": ["(N) A particular version of a publication", "(N) A set of printed copies"],
"editor": ["(N) A person who prepares text for publication", "(N) Someone who revises written work"],
"educate": ["(V) To teach or train", "(V) To provide knowledge or skill"],
"eel": ["(N) A long, snake-like fish", "(N) A slippery aquatic creature"],
"eerie": ["(Adj) Strange and unsettling", "(Adj) Mysteriously frightening"],
"efface": ["(V) To erase or wipe out", "(V) To make oneself inconspicuous"],
"effect": ["(N) A result or consequence", "(V) To bring about or cause"],
"effective": ["(Adj) Producing the desired result", "(Adj) In operation or active"],
"effervescent": ["(Adj) Bubbly or fizzy", "(Adj) Lively and enthusiastic"],
"effete": ["(Adj) Weak or exhausted", "(Adj) Over-refined and ineffective"],
"efficacy": ["(N) The ability to produce results", "(N) Effectiveness or power"],
"effigy": ["(N) A crude representation of a person", "(N) A sculpted likeness used symbolically"],
"effort": ["(N) Physical or mental exertion", "(N) A determined attempt"],
"egg": ["(N) An oval reproductive body", "(V) To urge or incite (egg on)"],
"eggplant": ["(N) A purple vegetable", "(N) A plant producing such fruit"],
"eggshell": ["(N) The hard outer covering of an egg", "(N) A pale, off-white color"],
"ego": ["(N) A person’s sense of self-esteem", "(N) The conscious self in psychology"],
"egress": ["(N) A way out or exit", "(V) To leave or go out"],
"eight": ["(N) The number 8", "(Adj) Being one more than seven"],
"eject": ["(V) To force out", "(V) To expel from a place"],
"eke": ["(V) To manage with difficulty", "(V) To supplement with effort"],
"elaborate": ["(Adj) Detailed and complex", "(V) To explain further"],
"elapse": ["(V) To pass or slip by (time)", "(N) The passage of time"],
"elastic": ["(Adj) Stretchy and flexible", "(N) A stretchy fabric or band"],
"elate": ["(V) To fill with joy", "(V) To make extremely happy"],
"elbow": ["(N) The joint between upper and lower arm", "(V) To push aside with the elbow"],
"elder": ["(Adj) Older in age", "(N) A respected senior person"],
"elect": ["(V) To choose by voting", "(Adj) Chosen for office but not yet installed"],
"elegant": ["(Adj) Graceful and stylish", "(Adj) Tastefully refined"],
"element": ["(N) A basic component", "(N) A substance that cannot be broken down further"],
"elephant": ["(N) A large herbivorous mammal", "(N) A symbol of memory or strength"],
"elevate": ["(V) To raise to a higher level", "(V) To improve mood or status"],
"eleven": ["(N) The number 11", "(Adj) One more than ten"],
"elf": ["(N) A small mythical creature", "(N) A mischievous supernatural being"],
"elicit": ["(V) To draw out a response", "(V) To evoke or bring forth"],
"eligible": ["(Adj) Qualified for selection", "(Adj) Suitable or desirable"],
"eliminate": ["(V) To remove completely", "(V) To defeat in a competition"],
"dollar": ["(N) A unit of currency", "(N) A basic monetary measure in several countries"],
"dollop": ["(N) A small lump or portion", "(V) To add casually in small amounts"],
"dolly": ["(N) A small platform on wheels", "(V) To move something using a dolly"],
"dolphin": ["(N) A highly intelligent marine mammal", "(N) A fast-swimming aquatic creature"],
"domain": ["(N) An area of control or knowledge", "(N) A territory governed by a ruler"],
"dome": ["(N) A rounded roof structure", "(N) A large, curved enclosure"],
"domestic": ["(Adj) Relating to the home", "(Adj) Tame or not wild"],
"domicile": ["(N) A place of residence", "(V) To establish a home"],
"dominant": ["(Adj) Most powerful or influential", "(N) A dominant genetic trait"],
"dominate": ["(V) To control or rule over", "(V) To be the most prominent"],
"don": ["(V) To put on clothing", "(N) A university teacher or leader"],
"donate": ["(V) To give as a gift or contribution", "(V) To provide without expecting return"],
"donkey": ["(N) A domesticated hoofed animal", "(N) A stubborn person (informal)"],
"donor": ["(N) A person who gives something", "(N) One who contributes money or organs"],
"doom": ["(N) Fate, often unpleasant", "(V) To condemn to a negative outcome"],
"door": ["(N) A hinged barrier for entry", "(N) An opportunity or access point"],
"dope": ["(N) Information or news (slang)", "(V) To administer drugs"],
"dormant": ["(Adj) Inactive but capable of awakening", "(Adj) Temporarily quiet or still"],
"dorsal": ["(Adj) Relating to the back of an organism", "(Adj) Positioned on the upper side"],
"dosage": ["(N) The amount of medicine to be taken", "(N) A prescribed quantity of a substance"],
"dose": ["(N) A measured amount of medicine", "(V) To administer a dose"],
"dote": ["(V) To show excessive love", "(V) To be overly fond of someone"],
"dotted": ["(Adj) Marked with dots", "(Adj) Spotted or speckled"],
"double": ["(Adj) Twice as much", "(V) To duplicate or fold over"],
"doubt": ["(N) A feeling of uncertainty", "(V) To question the truth of something"],
"dough": ["(N) A mixture of flour and liquid", "(N) Money (slang)"],
"douse": ["(V) To drench with liquid", "(V) To extinguish a flame"],
"dove": ["(N) A gentle bird symbolizing peace", "(N) A person favoring peaceful policies"],
"dovetail": ["(V) To fit together harmoniously", "(N) A joint used in carpentry"],
"down": ["(Adv) Toward a lower place", "(N) Soft fluffy feathers"],
"downcast": ["(Adj) Sad or discouraged", "(Adj) Directed downward"],
"downpour": ["(N) A heavy rainstorm", "(N) A sudden, intense rainfall"],
"downtown": ["(N) The central business district", "(Adj) Located in the city center"],
"dowry": ["(N) Property a bride brings to marriage", "(N) A gift given at a wedding"],
"doyle": ["(N) A surname", "(N) A reference to works by Arthur Conan Doyle"],
"doze": ["(V) To sleep lightly", "(N) A short nap"],
"drab": ["(Adj) Dull and lacking color", "(N) A dull, grayish color"],
"draft": ["(N) A preliminary version of writing", "(V) To prepare a first version"],
"drag": ["(V) To pull with effort", "(N) Something tedious or boring"],
"dragon": ["(N) A mythical fire-breathing creature", "(N) A fierce or intimidating person"],
"drain": ["(V) To remove liquid", "(N) A pipe that carries away water"],
"drake": ["(N) A male duck", "(N) A dragon in some folklore"],
"dram": ["(N) A small drink of liquor", "(N) A unit of weight"],
"drama": ["(N) A serious play or story", "(N) Emotional or intense events"],
"drastic": ["(Adj) Extreme or severe", "(Adj) Having a strong effect"],
"draw": ["(V) To pull or sketch", "(N) A tie in a contest"],
"drawer": ["(N) A sliding storage compartment", "(N) A person who draws"],
"dread": ["(N) Great fear", "(V) To anticipate with anxiety"],
"dream": ["(N) Thoughts during sleep", "(V) To imagine or aspire"],
"dredge": ["(V) To scoop from the bottom of water", "(V) To coat food in flour"],
"dress": ["(N) A garment for women", "(V) To put on clothes"],
"dresser": ["(N) A piece of furniture with drawers", "(N) A person who assists with costumes"],
"drew": ["(V) Past tense of draw", "(V) Pulled or sketched"],
"dribble": ["(V) To let liquid fall in drops", "(V) To move a ball skillfully"],
"dried": ["(Adj) Without moisture", "(V) Past tense of dry"],
"drift": ["(V) To move slowly without direction", "(N) A pile formed by wind or water"],
"drill": ["(N) A tool for making holes", "(V) To practice repeatedly"],
"drink": ["(V) To swallow liquid", "(N) A beverage"],
"drip": ["(V) To fall in drops", "(N) A small drop of liquid"],
"drive": ["(V) To operate a vehicle", "(N) Motivation or energy"],
"drizzle": ["(N) Light rain", "(V) To pour in a thin stream"],
"droll": ["(Adj) Amusing in an odd way", "(N) A comical person"],
"drone": ["(N) A continuous low sound", "(V) To speak monotonously"],
"droop": ["(V) To hang downward", "(V) To lose spirit or strength"],
"drop": ["(N) A small amount of liquid", "(V) To let fall"],
"drought": ["(N) A prolonged lack of rain", "(N) A severe water shortage"],
"drove": ["(N) A herd or flock", "(V) Past tense of drive"],
"drown": ["(V) To die by submersion", "(V) To overwhelm with liquid"],
"drowse": ["(V) To be half-asleep", "(N) A light sleep"],
"drudge": ["(N) A person who does dull work", "(V) To do tedious labor"],
"drug": ["(N) A chemical used as medicine", "(V) To administer a drug"],
"drum": ["(N) A percussion instrument", "(V) To beat rhythmically"],
"drunk": ["(Adj) Intoxicated by alcohol", "(N) A person who is intoxicated"],
"dry": ["(Adj) Free from moisture", "(V) To remove liquid"],
"dual": ["(Adj) Having two parts", "(Adj) Double in nature"],
"dub": ["(V) To give a title or name", "(V) To add sound to film"],
"duck": ["(N) A waterfowl bird", "(V) To lower the head quickly"],
"duct": ["(N) A tube for air or liquid", "(V) To channel through a duct"],
"dude": ["(N) A man or guy (informal)", "(N) A stylish or refined man (old use)"],
"duel": ["(N) A formal fight between two people", "(V) To fight in a duel"],
"duet": ["(N) A performance by two people", "(N) A musical composition for two"],
"duff": ["(N) A pudding-like dessert", "(Adj) Useless or worthless (slang)"],
"dug": ["(V) Past tense of dig", "(N) A teat of a female mammal"],
"duke": ["(N) A nobleman of high rank", "(V) To fight (slang: duke it out)"],
"dull": ["(Adj) Not sharp or bright", "(V) To make less intense"],
"duly": ["(Adv) In a proper manner", "(Adv) At the expected time"],
"dumb": ["(Adj) Unable to speak", "(Adj) Foolish or stupid (informal)"],
"dummy": ["(N) A model or replica", "(N) A person acting as a stand-in"],
"dump": ["(V) To drop or dispose of", "(N) A place for waste"],
"dune": ["(N) A hill of sand", "(N) A ridge formed by wind"],
"dung": ["(N) Animal excrement", "(V) To fertilize with manure"],
"dungeon": ["(N) A dark underground prison", "(N) A strong, confining cell"],
"dunk": ["(V) To dip into liquid", "(N) A basketball shot pushing the ball downward"],
"dupe": ["(V) To deceive or trick", "(N) A person easily fooled"],
"duplicate": ["(V) To make an exact copy", "(N) A replica or double"],
"durable": ["(Adj) Able to withstand wear", "(Adj) Long-lasting or sturdy"],
"duration": ["(N) The length of time something lasts", "(N) A period of continued existence"],
"duress": ["(N) Threats used to force action", "(N) Coercion or pressure"],
"dusk": ["(N) The time just after sunset", "(N) Partial darkness"],
"dust": ["(N) Fine dry particles", "(V) To remove dust from surfaces"],
"dusty": ["(Adj) Covered with dust", "(Adj) Dull or muted in color"],
"duty": ["(N) A moral or legal obligation", "(N) A tax on imports"],
"dwarf": ["(N) A small mythical being", "(V) To make something seem small by comparison"],
"dwell": ["(V) To live in a place", "(V) To think or speak at length about something"],
"dwelling": ["(N) A place to live", "(N) A residence or home"],
"dwindle": ["(V) To shrink gradually", "(V) To diminish in size or amount"],
"dye": ["(N) A substance used to color materials", "(V) To apply color to something"],
"dyer": ["(N) A person who dyes cloth", "(N) Someone skilled in coloring materials"],
"dynamic": ["(Adj) Energetic and forceful", "(N) A driving force or factor"],
"dynamo": ["(N) A generator producing electricity", "(N) A very energetic person"],
"dynasty": ["(N) A succession of rulers from one family", "(N) A powerful family line"],
"dysfunction": ["(N) Impaired or abnormal functioning", "(N) A breakdown in normal operations"],
"eager": ["(Adj) Enthusiastic or impatiently desirous", "(Adj) Keenly interested"],
"eagle": ["(N) A large bird of prey", "(N) A symbol of strength and freedom"],
"ear": ["(N) The organ of hearing", "(N) The part of a plant that contains grain"],
"earl": ["(N) A British nobleman", "(N) A title ranking below marquess"],
"early": ["(Adj) Happening before expected", "(Adv) Before the usual time"],
"earn": ["(V) To receive as payment", "(V) To gain through effort"],
"earnest": ["(Adj) Serious and sincere", "(N) A token of good faith"],
"earring": ["(N) Jewelry worn on the ear", "(N) An ornament attached to the earlobe"],
"earth": ["(N) The planet we live on", "(N) Soil or ground"],
"earthbound": ["(Adj) Unable to fly", "(Adj) Practical or mundane"],
"earthquake": ["(N) A shaking of the ground", "(N) A sudden seismic disturbance"],
"earthy": ["(Adj) Relating to soil", "(Adj) Simple, natural, or coarse"],
"ease": ["(N) Freedom from difficulty", "(V) To make less severe"],
"east": ["(N) The direction of sunrise", "(Adj) Situated toward the east"],
"eastern": ["(Adj) Located in the east", "(Adj) Relating to eastern regions"],
"easy": ["(Adj) Not difficult", "(Adj) Relaxed or comfortable"],
"eat": ["(V) To consume food", "(V) To erode or wear away"],
"eaves": ["(N) The lower edges of a roof", "(N) Overhanging roof sections"],
"ebb": ["(V) To recede or diminish", "(N) The movement of the tide outward"],
"ebony": ["(N) A dark, dense wood", "(Adj) Deep black in color"],
"echo": ["(N) A reflected sound", "(V) To repeat or resound"],
"eclipse": ["(N) The blocking of one celestial body by another", "(V) To overshadow or surpass"],
"ecology": ["(N) The study of organisms and their environment", "(N) The relationship between living things and surroundings"],
"economy": ["(N) A system of production and consumption", "(N) Careful management of resources"],
"ecstasy": ["(N) Intense joy or delight", "(N) A trance-like emotional state"],
"eddy": ["(N) A circular movement of water or air", "(V) To swirl in a circular motion"],
"edge": ["(N) The boundary of a surface", "(V) To move gradually or cautiously"],
"edible": ["(Adj) Safe to eat", "(N) Something suitable for consumption"],
"edict": ["(N) An official order", "(N) A formal proclamation"],
"edify": ["(V) To instruct morally or intellectually", "(V) To improve knowledge or character"],
"edit": ["(V) To revise or correct", "(N) A change made to text or film"],
"edition": ["(N) A particular version of a publication", "(N) A set of printed copies"],
"editor": ["(N) A person who prepares text for publication", "(N) Someone who revises written work"],
"educate": ["(V) To teach or train", "(V) To provide knowledge or skill"],
"eel": ["(N) A long, snake-like fish", "(N) A slippery aquatic creature"],
"eerie": ["(Adj) Strange and unsettling", "(Adj) Mysteriously frightening"],
"efface": ["(V) To erase or wipe out", "(V) To make oneself inconspicuous"],
"effect": ["(N) A result or consequence", "(V) To bring about or cause"],
"effective": ["(Adj) Producing the desired result", "(Adj) In operation or active"],
"effervescent": ["(Adj) Bubbly or fizzy", "(Adj) Lively and enthusiastic"],
"effete": ["(Adj) Weak or exhausted", "(Adj) Over-refined and ineffective"],
"efficacy": ["(N) The ability to produce results", "(N) Effectiveness or power"],
"effigy": ["(N) A crude representation of a person", "(N) A sculpted likeness used symbolically"],
"effort": ["(N) Physical or mental exertion", "(N) A determined attempt"],
"egg": ["(N) An oval reproductive body", "(V) To urge or incite (egg on)"],
"eggplant": ["(N) A purple vegetable", "(N) A plant producing such fruit"],
"eggshell": ["(N) The hard outer covering of an egg", "(N) A pale, off-white color"],
"ego": ["(N) A person’s sense of self-esteem", "(N) The conscious self in psychology"],
"egress": ["(N) A way out or exit", "(V) To leave or go out"],
"eight": ["(N) The number 8", "(Adj) Being one more than seven"],
"eject": ["(V) To force out", "(V) To expel from a place"],
"eke": ["(V) To manage with difficulty", "(V) To supplement with effort"],
"elaborate": ["(Adj) Detailed and complex", "(V) To explain further"],
"elapse": ["(V) To pass or slip by (time)", "(N) The passage of time"],
"elastic": ["(Adj) Stretchy and flexible", "(N) A stretchy fabric or band"],
"elate": ["(V) To fill with joy", "(V) To make extremely happy"],
"elbow": ["(N) The joint between upper and lower arm", "(V) To push aside with the elbow"],
"elder": ["(Adj) Older in age", "(N) A respected senior person"],
"elect": ["(V) To choose by voting", "(Adj) Chosen for office but not yet installed"],
"elegant": ["(Adj) Graceful and stylish", "(Adj) Tastefully refined"],
"element": ["(N) A basic component", "(N) A substance that cannot be broken down further"],
"elephant": ["(N) A large herbivorous mammal", "(N) A symbol of memory or strength"],
"elevate": ["(V) To raise to a higher level", "(V) To improve mood or status"],
"eleven": ["(N) The number 11", "(Adj) One more than ten"],
"elf": ["(N) A small mythical creature", "(N) A mischievous supernatural being"],
"elicit": ["(V) To draw out a response", "(V) To evoke or bring forth"],
"eligible": ["(Adj) Qualified for selection", "(Adj) Suitable or desirable"],
"eliminate": ["(V) To remove completely", "(V) To defeat in a competition"],
"elite": ["(N) A group of superior status", "(Adj) Representing the highest level of quality"],
"elixir": ["(N) A magical or medicinal potion", "(N) A substance believed to cure all ills"],
"elk": ["(N) A large deer with branching antlers", "(N) A species of cervid native to North America"],
"ell": ["(N) A right-angled extension of a building", "(N) An old unit of measurement for cloth"],
"ellipse": ["(N) An oval geometric shape", "(N) A closed curve with two focal points"],
"elm": ["(N) A tall deciduous tree", "(N) Wood from such a tree"],
"elongate": ["(V) To make longer", "(V) To stretch or extend in length"],
"elope": ["(V) To run away secretly to marry", "(V) To escape for a romantic union"],
"eloquent": ["(Adj) Fluent and persuasive in speech", "(Adj) Expressive and moving"],
"else": ["(Adv) In addition; besides", "(Adj) Different or alternative"],
"elude": ["(V) To escape from danger or capture", "(V) To avoid understanding"],
"elusive": ["(Adj) Difficult to catch or grasp", "(Adj) Hard to define or remember"],
"emaciate": ["(V) To make extremely thin", "(V) To waste away physically"],
"email": ["(N) Electronic mail", "(V) To send a message electronically"],
"emanate": ["(V) To come forth or flow out", "(V) To originate from a source"],
"embark": ["(V) To begin a journey", "(V) To board a ship or aircraft"],
"embarrass": ["(V) To cause someone to feel awkward", "(V) To make a situation uncomfortable"],
"embed": ["(V) To fix firmly within", "(V) To implant deeply"],
"embellish": ["(V) To decorate or add detail", "(V) To exaggerate for effect"],
"embezzle": ["(V) To steal money entrusted to one’s care", "(V) To misuse funds fraudulently"],
"embody": ["(V) To represent in physical form", "(V) To give tangible shape to an idea"],
"embrace": ["(V) To hug warmly", "(V) To accept willingly"],
"embroider": ["(V) To decorate with needlework", "(V) To add exaggerated details"],
"emerge": ["(V) To come into view", "(V) To become known or apparent"],
"emerald": ["(N) A green gemstone", "(Adj) Bright green in color"],
"emigrate": ["(V) To leave one’s country to settle elsewhere", "(V) To move out permanently"],
"emit": ["(V) To give off or release", "(V) To send out sound, light, or gas"],
"emotion": ["(N) A strong feeling", "(N) A mental reaction such as joy or anger"],
"empathize": ["(V) To understand another’s feelings", "(V) To share emotional experience"],
"emperor": ["(N) A supreme ruler of an empire", "(N) A monarch with absolute authority"],
"emphasis": ["(N) Special importance placed on something", "(N) Stress in speech or writing"],
"empire": ["(N) A group of territories under one ruler", "(N) A large, powerful organization"],
"employ": ["(V) To hire for work", "(V) To use or apply something"],
"empower": ["(V) To give authority or confidence", "(V) To enable someone to act"],
"empty": ["(Adj) Containing nothing", "(V) To remove contents"],
"emu": ["(N) A large flightless bird", "(N) A species native to Australia"],
"enable": ["(V) To make possible", "(V) To provide ability or means"],
"enact": ["(V) To make into law", "(V) To perform or act out"],
"enamel": ["(N) A glossy coating", "(V) To coat with a hard, shiny surface"],
"encamp": ["(V) To set up a temporary camp", "(V) To settle in tents"],
"encase": ["(V) To enclose completely", "(V) To cover in a protective layer"],
"enchant": ["(V) To delight greatly", "(V) To cast a magical spell"],
"encircle": ["(V) To surround completely", "(V) To form a ring around"],
"enclave": ["(N) A distinct area within a larger one", "(N) A territory surrounded by another"],
"enclose": ["(V) To surround on all sides", "(V) To include within something"],
"encode": ["(V) To convert into coded form", "(V) To express in symbols"],
"encompass": ["(V) To include or contain", "(V) To surround or encircle"],
"encounter": ["(V) To meet unexpectedly", "(N) A brief meeting or clash"],
"encourage": ["(V) To give support or confidence", "(V) To stimulate development"],
"end": ["(N) The final part of something", "(V) To bring to a close"],
"endanger": ["(V) To put at risk", "(V) To expose to harm"],
"endeavor": ["(N) A serious effort", "(V) To attempt earnestly"],
"endemic": ["(Adj) Native to a particular region", "(Adj) Common in a specific area"],
"endorse": ["(V) To approve or support", "(V) To sign the back of a check"],
"endow": ["(V) To provide with income or property", "(V) To equip with a quality"],
"endure": ["(V) To suffer patiently", "(V) To last over time"],
"enemy": ["(N) One who opposes or harms", "(N) A hostile force"],
"energetic": ["(Adj) Full of energy", "(Adj) Active and vigorous"],
"energy": ["(N) The capacity for work", "(N) Enthusiasm or vitality"],
"enforce": ["(V) To compel obedience", "(V) To carry out effectively"],
"engage": ["(V) To participate or become involved", "(V) To attract attention"],
"engine": ["(N) A machine that converts energy into motion", "(N) A motor powering a vehicle"],
"engineer": ["(N) A person trained in technical design", "(V) To plan or construct skillfully"],
"engrave": ["(V) To carve into a surface", "(V) To inscribe permanently"],
"engulf": ["(V) To swallow up completely", "(V) To overwhelm or surround"],
"enhance": ["(V) To improve or increase", "(V) To heighten in quality"],
"enigma": ["(N) A puzzling or mysterious thing", "(N) Something difficult to understand"],
"enjoy": ["(V) To take pleasure in", "(V) To experience with satisfaction"],
"enlarge": ["(V) To make bigger", "(V) To expand in scope"],
"enlighten": ["(V) To give knowledge or insight", "(V) To clarify understanding"],
"enlist": ["(V) To join the armed forces", "(V) To secure help or support"],
"enliven": ["(V) To make more lively", "(V) To brighten or invigorate"],
"enmesh": ["(V) To entangle deeply", "(V) To involve in a difficult situation"],
"enmity": ["(N) Deep-seated hostility", "(N) Hatred or ill will"],
"ennui": ["(N) A feeling of boredom", "(N) A sense of listlessness"],
"enrich": ["(V) To improve the quality of", "(V) To make wealthier"],
"enroll": ["(V) To register formally", "(V) To join a course or organization"],
"ensconce": ["(V) To settle comfortably", "(V) To hide securely"],
"ensemble": ["(N) A group performing together", "(N) A coordinated outfit"],
"enshrine": ["(V) To preserve as sacred", "(V) To enclose in a protective place"],
"ensnare": ["(V) To trap or capture", "(V) To involve in difficulty"],
"ensue": ["(V) To follow as a result", "(V) To occur afterward"],
"ensure": ["(V) To make certain", "(V) To guarantee"],
"entail": ["(V) To involve as a necessary part", "(V) To require logically"],
"entangle": ["(V) To twist together", "(V) To involve in complications"],
"enter": ["(V) To go into", "(V) To record information formally"],
"enterprise": ["(N) A business or project", "(N) Initiative or resourcefulness"],
"entertain": ["(V) To amuse or interest", "(V) To host guests"],
"enthrall": ["(V) To captivate completely", "(V) To hold spellbound"],
"enthuse": ["(V) To express excitement", "(V) To inspire enthusiasm"],
"entice": ["(V) To attract by offering pleasure", "(V) To tempt or lure"],
"entire": ["(Adj) Whole or complete", "(Adj) Not broken or divided"],
"entitle": ["(V) To give a right to", "(V) To name or label a work"],
"entity": ["(N) Something that exists independently", "(N) A being or organization"],
"entomb": ["(V) To bury in a tomb", "(V) To trap or confine"],
"entourage": ["(N) A group accompanying an important person", "(N) A retinue or following"],
"entrance": ["(N) A way into a place", "(V) To fill with wonder or delight"],
"entreat": ["(V) To beg earnestly", "(V) To plead with urgency"],
"entrench": ["(V) To establish firmly", "(V) To dig defensive positions"],
"entrepreneur": ["(N) A person who starts a business", "(N) Someone who takes financial risks for profit"],
"entry": ["(N) A way in", "(N) A written item in a record"],
"entwine": ["(V) To twist together", "(V) To interweave closely"],
"envelop": ["(V) To surround completely", "(V) To cover or enclose"],
"envelope": ["(N) A flat paper container for letters", "(N) A covering or outer layer"],
"envious": ["(Adj) Feeling jealousy", "(Adj) Wanting what another has"],
"environment": ["(N) Surrounding conditions", "(N) The natural world"],
"envision": ["(V) To imagine as a future possibility", "(V) To picture mentally"],
"envoy": ["(N) A diplomatic representative", "(N) A messenger or emissary"],
"envy": ["(N) A feeling of jealousy", "(V) To desire what another has"],
"enzyme": ["(N) A protein that speeds chemical reactions", "(N) A biological catalyst"],
"ephemeral": ["(Adj) Lasting a very short time", "(Adj) Fleeting or temporary"],
"epic": ["(N) A long heroic poem", "(Adj) Grand or impressive in scale"],
"epicure": ["(N) A person devoted to fine food", "(N) Someone with refined taste"],
"epidemic": ["(N) A widespread outbreak of disease", "(Adj) Rapidly spreading"],
"epilogue": ["(N) A concluding section of a book", "(N) A final commentary"],
"episode": ["(N) An event or incident", "(N) A single installment of a series"],
"epitaph": ["(N) Words inscribed on a tomb", "(N) A short tribute to someone deceased"],
"epithet": ["(N) A descriptive phrase", "(N) A term used as a label or insult"],
"epitome": ["(N) A perfect example", "(N) A summary of a written work"],
"epoch": ["(N) A significant period in history", "(N) A notable era or age"],
"equal": ["(Adj) The same in value or amount", "(N) A person of the same rank"],
"equate": ["(V) To consider as equal", "(V) To compare as equivalent"],
"equator": ["(N) The imaginary line dividing Earth", "(N) A circle equidistant from the poles"],
"equestrian": ["(Adj) Relating to horseback riding", "(N) A rider on horseback"],
"equidistant": ["(Adj) At equal distances", "(Adj) Positioned evenly apart"],
"equilibrium": ["(N) A state of balance", "(N) Mental or emotional stability"],
"equip": ["(V) To provide with necessary items", "(V) To prepare for a task"],
"equitable": ["(Adj) Fair and impartial", "(Adj) Just and reasonable"],
"equity": ["(N) Fairness or justice", "(N) Ownership value in property"],
"equivalent": ["(Adj) Equal in value or meaning", "(N) Something equal in function"],
"era": ["(N) A long and distinct period of history", "(N) A significant time span"],
"erase": ["(V) To remove written marks", "(V) To eliminate completely"],
"erode": ["(V) To wear away gradually", "(V) To deteriorate over time"],
"err": ["(V) To make a mistake", "(V) To be incorrect"],
"errand": ["(N) A short trip to accomplish a task", "(N) A small chore"],
"erratic": ["(Adj) Unpredictable or inconsistent", "(Adj) Irregular in movement"],
"error": ["(N) A mistake", "(N) A wrong action or judgment"],
"erudite": ["(Adj) Highly educated", "(Adj) Showing great knowledge"],
"erupt": ["(V) To burst forth suddenly", "(V) To explode or break out"],
"escalate": ["(V) To increase rapidly", "(V) To intensify in severity"],
"escape": ["(V) To break free from confinement", "(N) A means of getting away"],
"escort": ["(V) To accompany for protection", "(N) A person who accompanies another"],
"esoteric": ["(Adj) Understood by only a few", "(Adj) Intended for a specialized audience"],
"espionage": ["(N) The practice of spying", "(N) Secret intelligence gathering"],
"espouse": ["(V) To support or adopt a cause", "(V) To marry (archaic)"],
"essay": ["(N) A short written composition", "(V) To attempt or try"],
"essence": ["(N) The fundamental nature of something", "(N) A concentrated extract"],
"estate": ["(N) A large area of land or property", "(N) All property owned by a person"],
"esteem": ["(N) Respect or admiration", "(V) To regard highly"],
"estimate": ["(V) To approximate a value", "(N) A rough calculation"],
"estrange": ["(V) To cause separation in a relationship", "(V) To alienate emotionally"],
"eternal": ["(Adj) Lasting forever", "(Adj) Without beginning or end"],
"ethereal": ["(Adj) Light and delicate", "(Adj) Heavenly or otherworldly"],
"ethic": ["(N) A moral principle", "(N) A system of values"],
"ethnic": ["(Adj) Relating to cultural groups", "(N) A member of an ethnic group"],
"etiquette": ["(N) Proper social behavior", "(N) Accepted rules of conduct"],
"eucalyptus": ["(N) A fragrant Australian tree", "(N) A plant with aromatic leaves"],
"eulogy": ["(N) A speech praising someone who died", "(N) A tribute or commendation"],
"euphoria": ["(N) Intense happiness", "(N) A feeling of elation"],
"evacuate": ["(V) To leave a dangerous place", "(V) To remove people for safety"],
"evade": ["(V) To avoid or escape", "(V) To dodge responsibility"],
"evaluate": ["(V) To assess or judge", "(V) To determine value or quality"],
"evaporate": ["(V) To turn into vapor", "(V) To disappear gradually"],
"evasion": ["(N) The act of avoiding something", "(N) A clever escape"],
"eve": ["(N) The day or period before an event", "(N) The evening"],
"even": ["(Adj) Flat or level", "(Adv) Used to emphasize surprise"],
"evening": ["(N) The period between afternoon and night", "(N) The later part of the day"],
"event": ["(N) Something that happens", "(N) A planned social occasion"],
"evergreen": ["(N) A plant that stays green year-round", "(Adj) Perennially fresh or enduring"],
"evermore": ["(Adv) Forever", "(Adv) Always in the future"],
"evidence": ["(N) Proof supporting a claim", "(V) To show clearly"],
"evil": ["(Adj) Morally wrong", "(N) Harmful or wicked force"],
"evince": ["(V) To show clearly", "(V) To reveal the presence of something"],
"evoke": ["(V) To bring to mind", "(V) To elicit a reaction"],
"evolve": ["(V) To develop gradually", "(V) To change over time"],
"exact": ["(Adj) Precise or accurate", "(V) To demand or require"],
"exaggerate": ["(V) To overstate or magnify", "(V) To describe as larger than reality"],
"exalt": ["(V) To raise in rank or honor", "(V) To praise highly"],
"examine": ["(V) To inspect closely", "(V) To test knowledge"],
"example": ["(N) A representative instance", "(N) A model for imitation"],
"excavate": ["(V) To dig out", "(V) To uncover by removing earth"],
"exceed": ["(V) To go beyond limits", "(V) To surpass expectations"],
"excel": ["(V) To be exceptionally good at something", "(V) To surpass others"],
"except": ["(Prep) Not including; other than", "(V) To exclude from a group or category"],
"excerpt": ["(N) A short passage taken from a larger work", "(V) To select a portion for quotation"],
"excess": ["(N) An amount more than necessary", "(Adj) Extra or additional beyond limits"],
"exchange": ["(V) To give and receive reciprocally", "(N) A trade or substitution"],
"excise": ["(V) To cut out or remove", "(N) A tax on certain goods"],
"excite": ["(V) To stir up strong feelings", "(V) To cause enthusiasm or eagerness"],
"exclude": ["(V) To keep out or deny entry", "(V) To leave out intentionally"],
"excrete": ["(V) To expel waste from the body", "(V) To discharge as a biological process"],
"excursion": ["(N) A short trip or outing", "(N) A deviation from a regular path"],
"excuse": ["(N) A reason offered to justify behavior", "(V) To forgive or overlook"],
"execute": ["(V) To carry out or perform", "(V) To put to death as a legal penalty"],
"exemplary": ["(Adj) Serving as a desirable model", "(Adj) Outstanding or commendable"],
"exempt": ["(Adj) Free from obligation", "(V) To release from a requirement"],
"exercise": ["(N) Physical activity for health", "(V) To practice or train"],
"exert": ["(V) To apply force or effort", "(V) To make a strenuous attempt"],
"exhale": ["(V) To breathe out", "(V) To emit air or vapor"],
"exhaust": ["(V) To tire out completely", "(N) Waste gases expelled from an engine"],
"exhibit": ["(V) To display publicly", "(N) An item shown in a museum or gallery"],
"exile": ["(N) Forced absence from one’s home", "(V) To banish from a country"],
"exist": ["(V) To have actual being", "(V) To live or continue in reality"],
"exit": ["(N) A way out", "(V) To leave or depart"],
"exodus": ["(N) A mass departure of people", "(N) A large-scale migration"],
"exonerate": ["(V) To clear from blame", "(V) To absolve of wrongdoing"],
"exorbitant": ["(Adj) Unreasonably high in amount", "(Adj) Excessive beyond normal limits"],
"exorcise": ["(V) To drive out evil spirits", "(V) To rid of harmful influences"],
"exotic": ["(Adj) Strikingly unusual or foreign", "(Adj) From a distant or unfamiliar place"],
"expand": ["(V) To increase in size or scope", "(V) To elaborate or develop further"],
"expanse": ["(N) A wide, open area", "(N) A large stretch of something"],
"expect": ["(V) To anticipate or look forward to", "(V) To assume as likely"],
"expedite": ["(V) To speed up a process", "(V) To make something happen sooner"],
"expel": ["(V) To force out or eject", "(V) To remove from membership or school"],
"expend": ["(V) To use up resources", "(V) To spend time, energy, or money"],
"expense": ["(N) The cost required for something", "(N) A financial burden"],
"expert": ["(N) A person with special skill", "(Adj) Highly knowledgeable or skilled"],
"expire": ["(V) To come to an end", "(V) To die (formal)"],
"explain": ["(V) To make clear or understandable", "(V) To give reasons or details"],
"explicit": ["(Adj) Stated clearly and directly", "(Adj) Leaving no room for confusion"],
"explode": ["(V) To burst violently", "(V) To increase suddenly and dramatically"],
"exploit": ["(V) To use unfairly for advantage", "(N) A bold or daring achievement"],
"explore": ["(V) To investigate or travel through", "(V) To examine in detail"],
"export": ["(V) To send goods abroad", "(N) A product sold to another country"],
"expose": ["(V) To reveal something hidden", "(V) To make vulnerable to harm"],
"express": ["(V) To communicate thoughts or feelings", "(Adj) Fast and direct"],
"expunge": ["(V) To erase completely", "(V) To remove from a record"],
"extend": ["(V) To stretch out or lengthen", "(V) To offer or grant"],
"extent": ["(N) The degree or scope of something", "(N) The area covered by something"],
"exterior": ["(N) The outer surface", "(Adj) Situated on the outside"],
"external": ["(Adj) Outside or outer", "(Adj) Coming from the outside"],
"extinct": ["(Adj) No longer existing", "(Adj) Having died out completely"],
"extinguish": ["(V) To put out a fire", "(V) To end or suppress"],
"extol": ["(V) To praise enthusiastically", "(V) To glorify or commend highly"],
"extort": ["(V) To obtain by force or threats", "(V) To coerce into giving up something"],
"extra": ["(Adj) More than usual", "(N) Something additional"],
"extract": ["(V) To remove by pulling out", "(N) A concentrated substance"],
"extradite": ["(V) To hand over a fugitive to another authority", "(V) To transfer for legal prosecution"],
"extraordinary": ["(Adj) Very unusual or remarkable", "(Adj) Beyond the ordinary"],
"extravagant": ["(Adj) Excessively lavish", "(Adj) Spending more than necessary"],
"extreme": ["(Adj) Far from the usual", "(N) The highest or lowest degree"],
"exuberant": ["(Adj) Full of energy and excitement", "(Adj) Overflowing with enthusiasm"],
"exude": ["(V) To ooze or discharge slowly", "(V) To display strongly (emotion or quality)"],
"exult": ["(V) To rejoice triumphantly", "(V) To celebrate with great joy"],
"eye": ["(N) The organ of sight", "(V) To look at closely"],
"eyebrow": ["(N) The hair above the eye", "(N) A ridge that expresses emotion"],
"eyelid": ["(N) The fold of skin covering the eye", "(N) A protective covering for the eyeball"],
"fable": ["(N) A short tale teaching a moral", "(N) A fictional or legendary story"],
"fabric": ["(N) Cloth produced by weaving or knitting", "(N) The underlying structure of something"],
"fabricate": ["(V) To invent or concoct", "(V) To construct or manufacture"],
"fabulous": ["(Adj) Extremely good", "(Adj) Legendary or mythical"],
"facet": ["(N) One side of a many-sided object", "(N) An aspect or feature"],
"facile": ["(Adj) Easily achieved but superficial", "(Adj) Effortless or simplistic"],
"facilitate": ["(V) To make easier", "(V) To assist in progress"],
"facility": ["(N) A place designed for a specific purpose", "(N) Ease in doing something"],
"faction": ["(N) A dissenting group within a larger one", "(N) A small organized group in politics"],
"factor": ["(N) Something contributing to a result", "(V) To include as a component"],
"factory": ["(N) A building where goods are manufactured", "(N) A place of large-scale production"],
"factual": ["(Adj) Based on facts", "(Adj) True and verifiable"],
"faculty": ["(N) A natural ability", "(N) The teaching staff of a school"],
"fade": ["(V) To gradually lose brightness", "(V) To diminish in strength"],
"faint": ["(Adj) Weak or barely perceptible", "(V) To lose consciousness"],
"fair": ["(Adj) Just or impartial", "(N) A public event with entertainment"],
"fairy": ["(N) A mythical small being with magical powers", "(Adj) Delicate or enchanting"],
"faith": ["(N) Strong belief or trust", "(N) Religious conviction"],
"fake": ["(Adj) Not genuine", "(V) To imitate deceptively"],
"falcon": ["(N) A bird of prey trained for hunting", "(V) To hunt using a falcon"],
"fall": ["(V) To drop downward", "(N) The season of autumn"],
"false": ["(Adj) Not true", "(Adj) Artificial or misleading"],
"falter": ["(V) To hesitate or waver", "(V) To lose strength or momentum"],
"fame": ["(N) Widespread recognition", "(N) Public reputation"],
"familiar": ["(Adj) Well known", "(N) A close associate or companion"],
"family": ["(N) A group of related individuals", "(N) A household unit"],
"famine": ["(N) Extreme scarcity of food", "(N) Widespread hunger"],
"famous": ["(Adj) Widely known", "(Adj) Celebrated or renowned"],
"fan": ["(N) A device for moving air", "(N) An enthusiastic admirer"],
"fancy": ["(Adj) Elaborate or decorative", "(V) To imagine or desire"],
"fantastic": ["(Adj) Extremely good", "(Adj) Imaginary or fanciful"],
"fantasy": ["(N) Imaginative fiction", "(N) A daydream or illusion"],
"far": ["(Adj) Distant", "(Adv) To a great extent"],
"farce": ["(N) A ridiculous comedy", "(N) An absurd situation"],
"fare": ["(N) The cost of travel", "(V) To perform or get along"],
"farm": ["(N) Land used for agriculture", "(V) To cultivate crops or raise animals"],
"farmer": ["(N) A person who works a farm", "(N) Someone who cultivates land"],
"farsighted": ["(Adj) Able to see distant objects clearly", "(Adj) Showing wise long-term planning"],
"fascinate": ["(V) To attract intensely", "(V) To hold someone’s attention"],
"fashion": ["(N) A popular style", "(V) To shape or create"],
"fast": ["(Adj) Moving quickly", "(V) To abstain from food"],
"fasten": ["(V) To attach securely", "(V) To close or lock"],
"fat": ["(N) A natural oily substance", "(Adj) Overweight or thick"],
"fatal": ["(Adj) Causing death", "(Adj) Leading to failure or disaster"],
"fate": ["(N) A predetermined outcome", "(N) Destiny or inevitable events"],
"father": ["(N) A male parent", "(V) To be the father of"],
"fathom": ["(V) To understand deeply", "(N) A unit of depth (six feet)"],
"fatigue": ["(N) Extreme tiredness", "(V) To exhaust physically"],
"fault": ["(N) A flaw or mistake", "(V) To criticize or blame"],
"fauna": ["(N) The animals of a region", "(N) A collection of wildlife"],
"favor": ["(N) A kind or helpful act", "(V) To prefer or support"],
"fawn": ["(N) A young deer", "(V) To flatter excessively"],
"fear": ["(N) A feeling of dread", "(V) To be afraid of"],
"feast": ["(N) A large celebratory meal", "(V) To eat lavishly"],
"feat": ["(N) An impressive achievement", "(N) A notable act of skill"],
"feather": ["(N) A bird’s plumage", "(V) To cover with feathers"],
"feature": ["(N) A distinctive attribute", "(V) To include prominently"],
"federal": ["(Adj) Relating to a national government", "(Adj) Pertaining to a union of states"],
"fee": ["(N) A payment for services", "(N) A charge or cost"],
"feeble": ["(Adj) Weak or lacking strength", "(Adj) Ineffective or faint"],
"feed": ["(V) To give food", "(N) A supply of nourishment"],
"feel": ["(V) To sense by touch", "(V) To experience emotion"],
"feign": ["(V) To pretend or fake", "(V) To simulate a feeling"],
"feint": ["(N) A deceptive movement", "(V) To make a pretended attack"],
"felicity": ["(N) Great happiness", "(N) Skillful expression"],
"feline": ["(Adj) Cat-like", "(N) A member of the cat family"],
"fell": ["(V) To cut down a tree", "(Adj) Fierce or deadly"],
"fellow": ["(N) A companion or colleague", "(Adj) Belonging to the same group"],
"felon": ["(N) A person guilty of a serious crime", "(N) Someone convicted of a felony"],
"felt": ["(N) A fabric made by matting fibers", "(V) Past tense of feel"],
"female": ["(Adj) Of the sex that bears offspring", "(N) A woman or girl"],
"fence": ["(N) A barrier enclosing an area", "(V) To enclose or protect"],
"fend": ["(V) To ward off or defend", "(V) To manage independently"],
"feral": ["(Adj) Wild or untamed", "(Adj) Returned to a wild state"],
"ferment": ["(V) To undergo chemical breakdown", "(N) A state of agitation"],
"fern": ["(N) A leafy non-flowering plant", "(N) A plant with feathery fronds"],
"ferocious": ["(Adj) Fierce or violent", "(Adj) Intensely aggressive"],
"ferret": ["(N) A small domesticated mammal", "(V) To search persistently"],
"ferry": ["(N) A boat for short crossings", "(V) To transport by boat"],
"fertile": ["(Adj) Capable of producing abundantly", "(Adj) Rich in nutrients"],
"fervent": ["(Adj) Passionate and intense", "(Adj) Showing great enthusiasm"],
"fervor": ["(N) Intense passion", "(N) Strong, heated emotion"],
"festival": ["(N) A celebration or event", "(N) A series of performances"],
"fetch": ["(V) To go and bring back", "(N) The distance a wave travels"],
"fetter": ["(V) To restrain or shackle", "(N) A chain for the feet"],
"feud": ["(N) A long-standing quarrel", "(V) To engage in bitter conflict"],
"fever": ["(N) Elevated body temperature", "(N) Intense excitement"],
"few": ["(Adj) Not many", "(N) A small number"],
"fiber": ["(N) A thread-like structure", "(N) Material from plants or animals"],
"fiction": ["(N) Literature created from imagination", "(N) Something untrue or invented"],
"fiddle": ["(N) A violin (informal)", "(V) To play with or adjust aimlessly"],
"fidelity": ["(N) Faithfulness or loyalty", "(N) Accuracy in reproduction"],
"field": ["(N) An open area of land", "(N) A particular area of study"],
"fiend": ["(N) An evil spirit or demon", "(N) A person extremely devoted to something"],
"fierce": ["(Adj) Violent or intense", "(Adj) Showing strong emotion"],
"fiery": ["(Adj) Burning or flaming", "(Adj) Passionate or spirited"],
"fifteen": ["(N) The number 15", "(Adj) One more than fourteen"],
"fifth": ["(Adj) In the position after fourth", "(N) One part in five equal parts"],
"fifty": ["(N) The number 50", "(Adj) Half of one hundred"],
"fight": ["(V) To engage in combat", "(N) A struggle or conflict"],
"figure": ["(N) A number or shape", "(V) To calculate or assume"],
"filament": ["(N) A thin thread-like structure", "(N) A wire in a light bulb"],
"file": ["(N) A collection of documents", "(V) To organize or submit formally"],
"fill": ["(V) To make full", "(N) An amount that completes a container"],
"film": ["(N) A motion picture", "(V) To record on camera"],
"filter": ["(V) To remove impurities", "(N) A device for straining"],
"filth": ["(N) Extreme dirt", "(N) Obscene or corrupt matter"],
"final": ["(Adj) Last or concluding", "(N) The last game or exam"],
"finance": ["(N) The management of money", "(V) To provide funds for"],
"find": ["(V) To discover", "(N) Something located unexpectedly"],
"fine": ["(Adj) Of high quality", "(N) A monetary penalty"],
"finger": ["(N) A digit of the hand", "(V) To touch or handle"],
"finish": ["(V) To complete", "(N) The final part of something"],
"finite": ["(Adj) Having limits", "(Adj) Not infinite"],
"fire": ["(N) Combustion producing heat and light", "(V) To dismiss from a job"],
"firm": ["(Adj) Solid or stable", "(N) A business organization"],
"first": ["(Adj) Coming before all others", "(N) The earliest in order"],
"fiscal": ["(Adj) Relating to government revenue", "(Adj) Pertaining to financial matters"],
"fish": ["(N) An aquatic animal", "(V) To catch fish"],
"fissure": ["(N) A narrow opening or crack", "(V) To split or crack open"],
"fist": ["(N) A hand with fingers clenched", "(N) A symbol of strength or defiance"],
"fit": ["(Adj) Suitable or appropriate", "(V) To be the right size or shape"],
"fitness": ["(N) Physical health and strength", "(N) Suitability for a purpose"],
"fitting": ["(Adj) Appropriate or proper", "(N) A small part used to connect or fasten"],
"five": ["(N) The number 5", "(Adj) One more than four"],
"fix": ["(V) To repair or mend", "(N) A difficult or tricky situation"],
"fixture": ["(N) A permanent attachment", "(N) A scheduled event"],
"flag": ["(N) A piece of cloth used as a symbol", "(V) To mark or signal attention"],
"flail": ["(V) To wave or swing wildly", "(N) A tool for threshing grain"],
"flair": ["(N) A natural talent", "(N) A stylish or distinctive quality"],
"flake": ["(N) A small, thin piece", "(V) To break into small fragments"],
"flame": ["(N) A burning fire", "(V) To burn brightly"],
"flank": ["(N) The side of an animal or object", "(V) To be positioned on either side"],
"flannel": ["(N) A soft woven fabric", "(N) Clothing made from such fabric"],
"flap": ["(N) A piece of material that hangs loosely", "(V) To move up and down rapidly"],
"flare": ["(V) To burn with a sudden intensity", "(N) A bright burst of light"],
"flash": ["(N) A sudden burst of light", "(V) To shine briefly"],
"flask": ["(N) A small bottle for liquids", "(N) A container used in laboratories"],
"flat": ["(Adj) Level and smooth", "(N) A type of housing unit"],
"flatten": ["(V) To make flat", "(V) To defeat decisively (informal)"],
"flatter": ["(V) To praise excessively", "(V) To compliment insincerely"],
"flavor": ["(N) The taste of something", "(V) To add seasoning"],
"flaw": ["(N) An imperfection or defect", "(V) To spoil or mar"],
"flax": ["(N) A plant used to make linen", "(N) The fiber from such a plant"],
"flea": ["(N) A small jumping insect", "(N) A pest that feeds on blood"],
"fleck": ["(N) A small spot or mark", "(V) To mark with small patches"],
"fled": ["(V) Past tense of flee", "(V) Ran away quickly"],
"flee": ["(V) To run away from danger", "(V) To escape swiftly"],
"fleet": ["(N) A group of ships", "(Adj) Fast or swift"],
"flesh": ["(N) The soft tissue of the body", "(V) To add substance or detail"],
"flex": ["(V) To bend or tighten muscles", "(N) A show of strength (informal)"],
"flick": ["(V) To strike lightly", "(N) A quick, light movement"],
"flier": ["(N) A printed advertisement", "(N) A person or thing that flies"],
"flight": ["(N) The act of flying", "(N) A set of stairs between landings"],
"flinch": ["(V) To shrink back in fear", "(V) To react nervously"],
"fling": ["(V) To throw forcefully", "(N) A brief, casual relationship"],
"flint": ["(N) A hard stone used to make sparks", "(N) A tool-making material"],
"flip": ["(V) To turn over quickly", "(N) A quick, light movement"],
"flirt": ["(V) To behave playfully romantic", "(N) A person who flirts"],
"float": ["(V) To rest on the surface of liquid", "(N) A decorated parade platform"],
"flock": ["(N) A group of birds or animals", "(V) To gather in large numbers"],
"flood": ["(N) An overflow of water", "(V) To inundate or overwhelm"],
"floor": ["(N) The surface you walk on", "(V) To knock down or astonish"],
"flop": ["(V) To fall or drop heavily", "(N) A complete failure"],
"flora": ["(N) The plants of a region", "(N) Plant life collectively"],
"flour": ["(N) Powdered grain used for baking", "(V) To coat with flour"],
"flourish": ["(V) To thrive or prosper", "(N) A bold or extravagant gesture"],
"flow": ["(V) To move smoothly like a liquid", "(N) A steady, continuous movement"],
"flower": ["(N) A blooming plant", "(V) To blossom or develop"],
"fluent": ["(Adj) Able to speak smoothly", "(Adj) Flowing effortlessly"],
"fluff": ["(N) Soft, light material", "(V) To shake or puff up"],
"fluid": ["(N) A substance that flows", "(Adj) Smooth and adaptable"],
"fluke": ["(N) A stroke of luck", "(N) A flatfish species"],
"flume": ["(N) A narrow channel for water", "(N) A chute for logs or water rides"],
"flung": ["(V) Past tense of fling", "(V) Thrown forcefully"],
"flunk": ["(V) To fail a test or course", "(N) A failure (informal)"],
"fluorescent": ["(Adj) Glowing under ultraviolet light", "(Adj) Bright and vivid"],
"flurry": ["(N) A brief burst of activity", "(N) A light snowfall"],
"flush": ["(V) To redden or clean with water", "(N) A sudden rush of emotion"],
"flute": ["(N) A woodwind instrument", "(V) To make grooves or decorative ridges"],
"flutter": ["(V) To move with quick, light motions", "(N) A rapid, trembling movement"],
"fly": ["(V) To move through the air", "(N) A winged insect"],
"foal": ["(N) A young horse", "(V) To give birth to a foal"],
"foam": ["(N) Bubbles formed on liquid", "(V) To froth or bubble"],
"focal": ["(Adj) Central or important", "(Adj) Relating to focus"],
"focus": ["(N) The center of attention", "(V) To concentrate effort"],
"fodder": ["(N) Food for livestock", "(N) Material used for a particular purpose"],
"fog": ["(N) Thick mist", "(V) To obscure or confuse"],
"foil": ["(N) Thin metal sheet", "(V) To prevent success"],
"fold": ["(V) To bend over itself", "(N) A crease or layer"],
"folk": ["(N) People in general", "(Adj) Traditional or cultural"],
"follow": ["(V) To come after", "(V) To obey or adhere to"],
"folly": ["(N) Foolish behavior", "(N) A costly ornamental building"],
"fond": ["(Adj) Having affection for", "(Adj) Loving or tender"],
"font": ["(N) A style of printed letters", "(N) A receptacle for holy water"],
"food": ["(N) Something eaten for nourishment", "(N) A source of sustenance"],
"fool": ["(N) A person lacking judgment", "(V) To deceive or trick"],
"foot": ["(N) The lower extremity of the leg", "(N) A unit of measurement"],
"football": ["(N) A sport played with a ball", "(N) The ball used in the sport"],
"footing": ["(N) A secure grip or position", "(N) The foundation of a structure"],
"footprint": ["(N) A mark left by a foot", "(N) The impact or presence of something"],
"forage": ["(V) To search for food", "(N) Food for animals"],
"foray": ["(N) A sudden attack or venture", "(V) To make an initial attempt"],
"forbid": ["(V) To prohibit or ban", "(V) To command against"],
"force": ["(N) Strength or power", "(V) To compel or push"],
"ford": ["(N) A shallow place to cross a river", "(V) To cross at a shallow point"],
"fore": ["(Adj) Situated at the front", "(N) The front part of something"],
"forecast": ["(N) A prediction of future events", "(V) To predict or estimate"],
"forego": ["(V) To do without", "(V) To precede in time"],
"forehead": ["(N) The front part of the head", "(N) The area above the eyebrows"],
"foreign": ["(Adj) From another country", "(Adj) Strange or unfamiliar"],
"foreman": ["(N) A supervisor of workers", "(N) The leader of a jury"],
"foremost": ["(Adj) Most important", "(Adv) In the first place"],
"forensic": ["(Adj) Relating to legal investigation", "(Adj) Scientific analysis for evidence"],
"forest": ["(N) A large area of trees", "(V) To plant with trees"],
"foresee": ["(V) To predict or anticipate", "(V) To imagine beforehand"],
"foretell": ["(V) To predict the future", "(V) To prophesy"],
"forge": ["(V) To form by heating and hammering", "(V) To create fraudulently"],
"forget": ["(V) To fail to remember", "(V) To overlook or neglect"],
"forgive": ["(V) To pardon wrongdoing", "(V) To stop feeling resentment"],
"fork": ["(N) A utensil with prongs", "(V) To divide into branches"],
"form": ["(N) The shape or structure of something", "(V) To create or establish"],
"formal": ["(Adj) Following established rules", "(Adj) Proper and ceremonious"],
"format": ["(N) The arrangement of something", "(V) To organize or structure"],
"former": ["(Adj) Previous or earlier", "(N) The first of two mentioned"],
"fort": ["(N) A fortified building", "(N) A strong defensive structure"],
"forth": ["(Adv) Forward in time or place", "(Adv) Out into view"],
"fortify": ["(V) To strengthen or reinforce", "(V) To add nutrients to food"],
"fortune": ["(N) Wealth or luck", "(N) A large amount of money"],
"forty": ["(N) The number 40", "(Adj) Four tens"],
"forum": ["(N) A place for discussion", "(N) A public meeting or assembly"],
"forward": ["(Adv) Toward the front", "(V) To send onward"],
"fossil": ["(N) Preserved remains of ancient life", "(Adj) Outdated or old-fashioned"],
"foster": ["(V) To encourage growth", "(Adj) Providing parental care temporarily"],
"found": ["(V) To establish or create", "(V) Past tense of find"],
"foundation": ["(N) The base of a structure", "(N) An organization providing support"],
"fountain": ["(N) A structure that sends water upward", "(N) A source of something"],
"four": ["(N) The number 4", "(Adj) One more than three"],
"fowl": ["(N) A bird used for food", "(N) Domestic poultry"],
"fox": ["(N) A cunning wild animal", "(V) To confuse or puzzle"],
"fraction": ["(N) A part of a whole", "(N) A small portion"],
"fracture": ["(N) A break in a bone", "(V) To break or crack"],
"fragile": ["(Adj) Easily broken", "(Adj) Delicate or vulnerable"],
"fragment": ["(N) A small broken piece", "(V) To break into pieces"],
"fragrant": ["(Adj) Having a pleasant smell", "(Adj) Sweet-smelling"],
"frail": ["(Adj) Weak or delicate", "(Adj) Easily damaged"],
"frame": ["(N) A structure supporting something", "(V) To construct or devise"],
"frank": ["(Adj) Honest and direct", "(V) To mark mail as paid"],
"frantic": ["(Adj) Wild with emotion", "(Adj) Desperate or frenzied"],
"fraud": ["(N) Deception for gain", "(N) A person who deceives"],
"fray": ["(N) A noisy fight", "(V) To wear away at the edges"],
"freak": ["(N) An unusual or abnormal person", "(V) To react wildly (informal)"],
"free": ["(Adj) Not restricted", "(V) To release from confinement"],
"freedom": ["(N) The state of being free", "(N) Independence or liberty"],
"freeze": ["(V) To turn to ice", "(N) A period of cold weather"],
"freight": ["(N) Goods transported in bulk", "(V) To transport goods"],
"frenzy": ["(N) A state of wild excitement", "(V) To drive into agitation"],
"frequency": ["(N) The rate of occurrence", "(N) The number of cycles per second"],
"frequent": ["(Adj) Occurring often", "(V) To visit regularly"],
"fresh": ["(Adj) Newly made or obtained", "(Adj) Energetic or lively"],
"fret": ["(V) To worry or be anxious", "(N) A ridge on a guitar neck"],
"friar": ["(N) A member of a religious order", "(N) A traveling monk"],
"friction": ["(N) Rubbing of one surface against another", "(N) Conflict or tension"],
"Friday": ["(N) The sixth day of the week", "(N) A day associated with endings"],
"friend": ["(N) A person one knows well", "(V) To add someone to a social network"],
"fright": ["(N) A sudden fear", "(V) To scare or startle"],
"frigid": ["(Adj) Extremely cold", "(Adj) Lacking warmth or emotion"],
"frill": ["(N) A decorative ruffle", "(N) An unnecessary extra"],
"fringe": ["(N) A decorative border", "(N) The outer edge of something"],
"frolic": ["(V) To play energetically", "(N) A lively, playful activity"],
"front": ["(N) The forward part", "(V) To face or confront"],
"frost": ["(N) Ice crystals on surfaces", "(V) To cover with icing"],
"frown": ["(V) To make a displeased expression", "(N) A look of disapproval"],
"frozen": ["(Adj) Turned to ice", "(Adj) Very cold or immobile"],
"fruit": ["(N) The edible part of a plant", "(N) The result or outcome of effort"],
"frustrate": ["(V) To prevent success", "(V) To cause annoyance"],
"fry": ["(V) To cook in hot oil", "(N) A small fish"],
"fuel": ["(N) A substance burned for energy", "(V) To supply with power"],
"fugitive": ["(N) A person fleeing capture", "(Adj) Running away or elusive"],
"fulfill": ["(V) To complete or satisfy", "(V) To carry out a promise"],
"full": ["(Adj) Containing as much as possible", "(Adj) Complete or entire"],
"fumble": ["(V) To handle clumsily", "(N) A mistake in handling"],
"fume": ["(N) A gas or vapor", "(V) To be very angry"],
"fun": ["(N) Enjoyment or amusement", "(Adj) Entertaining or playful"],
"function": ["(N) A purpose or role", "(V) To operate or work"],
"fund": ["(N) A supply of money", "(V) To provide financial support"],
"funeral": ["(N) A ceremony for the dead", "(N) A burial or memorial service"],
"fungus": ["(N) A spore-producing organism", "(N) Mold or mushroom"],
"funnel": ["(N) A cone-shaped tool for pouring", "(V) To channel or direct"],
"funny": ["(Adj) Causing laughter", "(Adj) Strange or unusual"],
"fur": ["(N) The thick hair of an animal", "(N) A garment made from animal hair"],
"furious": ["(Adj) Extremely angry", "(Adj) Very fast or intense"],
"furl": ["(V) To roll up tightly", "(V) To fold neatly"],
"furnace": ["(N) A heating device", "(N) A chamber for high-temperature processes"],
"furnish": ["(V) To provide furniture", "(V) To supply or equip"],
"furniture": ["(N) Movable items in a room", "(N) Household furnishings"],
"furry": ["(Adj) Covered with fur", "(Adj) Soft and fuzzy"],
"further": ["(Adv) At a greater distance", "(V) To promote or advance"],
"fury": ["(N) Violent anger", "(N) A fierce, destructive force"],
"fuse": ["(N) A safety device that melts to break a circuit", "(V) To join by melting together"],
"fusion": ["(N) The merging of two things", "(N) A nuclear reaction combining atoms"],
"fuss": ["(N) Unnecessary excitement", "(V) To worry over details"],
"futile": ["(Adj) Incapable of producing results", "(Adj) Pointless or ineffective"],
"future": ["(N) Time yet to come", "(Adj) Relating to coming events"],
"gadget": ["(N) A small mechanical device", "(N) A clever or novel tool"],
"gaffe": ["(N) A social or verbal blunder", "(N) An embarrassing mistake"],
"gag": ["(N) A joke or prank", "(V) To choke or prevent speech"],
"gain": ["(V) To obtain or secure", "(N) An increase or advantage"],
"gait": ["(N) A manner of walking", "(N) A horse’s particular pace"],
"galaxy": ["(N) A massive system of stars", "(N) A large, impressive group"],
"gale": ["(N) A very strong wind", "(N) A burst of loud laughter"],
"gall": ["(N) Bold, rude behavior", "(V) To irritate or annoy"],
"gallery": ["(N) A room for displaying art", "(N) The highest balcony in a theater"],
"gallon": ["(N) A unit of liquid measure", "(N) A large quantity (informal)"],
"gallop": ["(V) To run at full speed (horse)", "(N) A fast, bounding gait"],
"galore": ["(Adj) In great abundance", "(Adv) Plentifully or abundantly"],
"gamble": ["(V) To risk money on chance", "(N) A risky action or decision"],
"game": ["(N) A form of play or sport", "(Adj) Willing or eager (informal)"],
"gamut": ["(N) The full range of something", "(N) A complete scale or extent"],
"gang": ["(N) A group of people acting together", "(V) To unite for a purpose"],
"gap": ["(N) An opening or break", "(N) A difference or disparity"],
"garage": ["(N) A building for vehicles", "(V) To store in a garage"],
"garb": ["(N) Clothing or attire", "(V) To dress in a particular style"],
"garbage": ["(N) Waste material", "(N) Something worthless or inferior"],
"garden": ["(N) A cultivated area of plants", "(V) To grow plants as a hobby"],
"gargle": ["(V) To rinse the throat", "(N) A liquid used for rinsing"],
"garland": ["(N) A wreath of flowers", "(V) To decorate with garlands"],
"garment": ["(N) A piece of clothing", "(N) An article worn on the body"],
"garnish": ["(V) To decorate food", "(N) A decorative topping"],
"garrison": ["(N) A military post", "(V) To station troops"],
"garter": ["(N) A band worn to hold up stockings", "(N) A ceremonial wedding accessory"],
"gas": ["(N) A state of matter", "(V) To fill with fuel"],
"gash": ["(N) A deep cut", "(V) To wound with a long cut"],
"gasp": ["(V) To inhale suddenly", "(N) A sudden intake of breath"],
"gate": ["(N) A movable barrier", "(N) An entrance or exit point"],
"gather": ["(V) To bring together", "(V) To infer or conclude"],
"gauge": ["(N) A measuring instrument", "(V) To estimate or judge"],
"gaunt": ["(Adj) Extremely thin", "(Adj) Grim or desolate in appearance"],
"gauze": ["(N) A thin, transparent fabric", "(N) A medical dressing material"],
"gave": ["(V) Past tense of give", "(V) Provided or granted"],
"gavel": ["(N) A small hammer used by a judge", "(N) A symbol of authority in meetings"],
"gawk": ["(V) To stare stupidly", "(N) An awkward or clumsy person"],
"gaze": ["(V) To look steadily", "(N) A fixed, intent look"],
"gear": ["(N) Equipment or apparatus", "(V) To adjust for a purpose"],
"gecko": ["(N) A small climbing lizard", "(N) A reptile known for sticky feet"],
"geese": ["(N) Plural of goose", "(N) Waterfowl known for honking"],
"gel": ["(N) A thick, jelly-like substance", "(V) To solidify or take shape"],
"gem": ["(N) A precious stone", "(N) Something admired for beauty"],
"gender": ["(N) Social or cultural identity", "(N) A grammatical classification"],
"gene": ["(N) A unit of heredity", "(N) A segment of DNA"],
"general": ["(Adj) Widespread or common", "(N) A high-ranking military officer"],
"generate": ["(V) To produce or create", "(V) To bring into existence"],
"generous": ["(Adj) Willing to give freely", "(Adj) Larger than expected"],
"genial": ["(Adj) Friendly and cheerful", "(Adj) Pleasant in manner"],
"genius": ["(N) Exceptional intellectual ability", "(N) A person of great talent"],
"genre": ["(N) A category of artistic work", "(N) A style or type"],
"gentle": ["(Adj) Mild and kind", "(V) To make soft or calm"],
"genuine": ["(Adj) Authentic or real", "(Adj) Sincere and honest"],
"geology": ["(N) The study of Earth’s structure", "(N) The physical composition of a region"],
"geometry": ["(N) A branch of mathematics", "(N) The shape or arrangement of objects"],
"gerbil": ["(N) A small burrowing rodent", "(N) A common household pet"],
"germ": ["(N) A microorganism", "(N) The beginning or origin of something"],
"gesture": ["(N) A movement expressing meaning", "(V) To signal with movement"],
"get": ["(V) To obtain or receive", "(V) To become or grow into"],
"ghost": ["(N) A spirit of the dead", "(V) To disappear without explanation (informal)"],
"giant": ["(N) A very large being", "(Adj) Extremely large"],
"gift": ["(N) A present", "(V) To give as a gift"],
"giggle": ["(V) To laugh lightly", "(N) A silly or nervous laugh"],
"gild": ["(V) To cover with gold", "(V) To make something appear more attractive"],
"gill": ["(N) A respiratory organ of fish", "(N) A unit of liquid measure"],
"gilt": ["(Adj) Covered with gold leaf", "(N) Gold-colored decoration"],
"gimlet": ["(N) A small hand tool for boring holes", "(N) A cocktail of gin and lime"],
"ginger": ["(N) A spicy root", "(Adj) Lively or spirited"],
"gingerly": ["(Adv) With great care", "(Adj) Cautious or delicate"],
"giraffe": ["(N) A tall African mammal", "(N) An animal with a long neck"],
"gird": ["(V) To encircle or bind", "(V) To prepare for action"],
"girl": ["(N) A female child", "(N) A young woman"],
"girth": ["(N) The measurement around something", "(N) A strap around a horse’s body"],
"gist": ["(N) The main point", "(N) The essential meaning"],
"give": ["(V) To hand over", "(V) To yield or collapse under pressure"],
"glacier": ["(N) A large mass of moving ice", "(N) A slow-moving frozen river"],
"glad": ["(Adj) Pleased or happy", "(Adj) Willing or eager"],
"glade": ["(N) An open space in a forest", "(N) A clearing among trees"],
"glance": ["(V) To look quickly", "(N) A brief look"],
"glare": ["(V) To stare angrily", "(N) A harsh, bright light"],
"glass": ["(N) A transparent material", "(N) A drinking vessel"],
"gleam": ["(V) To shine softly", "(N) A faint or brief light"],
"glean": ["(V) To gather bit by bit", "(V) To extract information gradually"],
"glee": ["(N) Great delight", "(N) Joyful enthusiasm"],
"glide": ["(V) To move smoothly", "(N) A smooth, continuous motion"],
"glimmer": ["(N) A faint light", "(V) To shine weakly"],
"glimpse": ["(N) A quick look", "(V) To see briefly"],
"glint": ["(N) A tiny flash of light", "(V) To sparkle briefly"],
"glisten": ["(V) To shine with a wet or smooth surface", "(V) To sparkle faintly"],
"glitter": ["(V) To shine brightly", "(N) Tiny sparkling particles"],
"gloat": ["(V) To dwell on one’s success smugly", "(N) A smug expression"],
"glob": ["(N) A lump of thick liquid", "(V) To stick together in clumps"],
"globe": ["(N) A spherical model of Earth", "(N) A round object"],
"gloom": ["(N) Partial darkness", "(N) Sadness or depression"],
"glory": ["(N) Great honor or praise", "(N) Magnificence or splendor"],
"gloss": ["(N) A shiny surface", "(V) To give a smooth finish"],
"glove": ["(N) A covering for the hand", "(V) To put gloves on"],
"glow": ["(V) To shine steadily", "(N) A soft, steady light"],
"glue": ["(N) An adhesive substance", "(V) To stick together"],
"glum": ["(Adj) Gloomy or sad", "(Adj) Sullen or depressed"],
"glut": ["(N) An oversupply", "(V) To flood with excess"],
"gnarl": ["(V) To twist into a knot", "(N) A rough, knotty growth"],
"gnash": ["(V) To grind teeth angrily", "(V) To strike together harshly"],
"gnat": ["(N) A tiny flying insect", "(N) A small pest"],
"gnaw": ["(V) To bite or chew persistently", "(V) To wear away gradually"],
"gnome": ["(N) A small mythical earth-dweller", "(N) A garden figurine"],
"goal": ["(N) An objective or aim", "(N) A point scored in sports"],
"goat": ["(N) A horned farm animal", "(N) A scapegoat or blamed person (informal)"],
"gobble": ["(V) To eat quickly and greedily", "(N) A turkey’s call"],
"goblet": ["(N) A drinking cup with a stem", "(N) A ceremonial vessel"],
"god": ["(N) A deity or supreme being", "(N) A greatly admired person (informal)"],
"goddess": ["(N) A female deity", "(N) A woman admired for beauty"],
"goggle": ["(V) To stare with wide eyes", "(N) Protective eyewear"],
"gold": ["(N) A precious yellow metal", "(Adj) Made of or colored like gold"],
"golf": ["(N) A sport played with clubs and balls", "(V) To play the game of golf"],
"gone": ["(Adj) No longer present", "(V) Past participle of go"],
"good": ["(Adj) Morally right or beneficial", "(N) Something positive or useful"],
"goose": ["(N) A large waterfowl", "(V) To poke or prod playfully"],
"gorge": ["(N) A deep, narrow valley", "(V) To eat greedily"],
"gorgeous": ["(Adj) Extremely beautiful", "(Adj) Magnificent or splendid"],
"gory": ["(Adj) Covered with blood", "(Adj) Violent or gruesome"],
"gosh": ["(Interj) An expression of mild surprise", "(Interj) A polite exclamation"],
"gospel": ["(N) Religious teachings of Christ", "(N) Something accepted as unquestionably true"],
"gossip": ["(N) Idle talk about others", "(V) To spread rumors"],
"got": ["(V) Past tense of get", "(V) Obtained or received"],
"gouge": ["(V) To dig or scoop out", "(N) A groove or hole"],
"gourd": ["(N) A hard-shelled fruit", "(N) A container made from such a shell"],
"gout": ["(N) A painful joint disease", "(N) A drop or spot of liquid (archaic)"],
"govern": ["(V) To rule or control", "(V) To influence or guide"],
"gown": ["(N) A long formal dress", "(N) A robe worn for ceremonies"],
"grab": ["(V) To seize quickly", "(N) A quick snatch"],
"grace": ["(N) Elegance or beauty", "(V) To honor or adorn"],
"grade": ["(N) A level of quality", "(V) To evaluate or score"],
"grain": ["(N) A small hard seed", "(N) The texture of wood or fabric"],
"grand": ["(Adj) Magnificent or impressive", "(N) A thousand dollars (slang)"],
"grandfather": ["(N) The father of one’s parent", "(V) To exempt from new rules"],
"grant": ["(V) To give or allow", "(N) A sum of money awarded"],
"grape": ["(N) A small juicy fruit", "(N) A vine producing such fruit"],
"graph": ["(N) A diagram showing relationships", "(V) To plot data visually"],
"grasp": ["(V) To seize firmly", "(N) Understanding or comprehension"],
"grass": ["(N) Green vegetation covering ground", "(V) To inform on someone (slang)"],
"grate": ["(V) To shred into small pieces", "(N) A metal frame for a fire"],
"gratify": ["(V) To please or satisfy", "(V) To indulge a desire"],
"grave": ["(N) A burial place", "(Adj) Serious or solemn"],
"gravity": ["(N) The force of attraction", "(N) Seriousness or importance"],
"gravy": ["(N) A sauce made from meat juices", "(N) Easy profit (informal)"],
"gray": ["(Adj) Of a color between black and white", "(N) A neutral color tone"],
"graze": ["(V) To feed on growing grass", "(V) To scrape lightly"],
"grease": ["(N) Oily or fatty substance", "(V) To lubricate"],
"great": ["(Adj) Very good", "(Adj) Large in size or degree"],
"greed": ["(N) Excessive desire for wealth", "(N) Intense selfish craving"],
"green": ["(Adj) The color of grass", "(Adj) Inexperienced or naive"],
"greet": ["(V) To welcome or address", "(V) To meet with a reaction"],
"grew": ["(V) Past tense of grow", "(V) Increased in size"],
"grid": ["(N) A network of lines", "(N) An electrical distribution system"],
"grief": ["(N) Deep sorrow", "(N) Trouble or difficulty (informal)"],
"grill": ["(N) A cooking grate", "(V) To question intensely"],
"grim": ["(Adj) Harsh or forbidding", "(Adj) Depressing or gloomy"],
"grime": ["(N) Dirt or soot", "(V) To cover with filth"],
"grin": ["(V) To smile broadly", "(N) A wide smile"],
"grind": ["(V) To crush into powder", "(N) Hard, monotonous work"],
"grip": ["(V) To grasp firmly", "(N) A tight hold"],
"grit": ["(N) Small, loose particles", "(N) Courage and determination"],
"groan": ["(V) To make a deep sound of pain", "(N) A sound expressing discomfort"],
"grocer": ["(N) A person who sells food", "(N) A shopkeeper of provisions"],
"groom": ["(N) A man getting married", "(V) To clean or prepare"],
"groove": ["(N) A long, narrow cut", "(V) To enjoy rhythm or music"],
"grope": ["(V) To feel blindly", "(V) To search uncertainly"],
"gross": ["(Adj) Disgusting or coarse", "(N) A total amount before deductions"],
"ground": ["(N) The solid surface of Earth", "(V) To prohibit from flying or going out"],
"group": ["(N) A number of people or things", "(V) To arrange together"],
"grove": ["(N) A small group of trees", "(N) A wooded area"],
"grow": ["(V) To increase in size", "(V) To cultivate plants"],
"growth": ["(N) An increase in size", "(N) A tumor or abnormal mass"],
"grub": ["(N) Food (informal)", "(N) A larval insect"],
"grudge": ["(N) A persistent feeling of resentment", "(V) To resent or envy"],
"gruel": ["(N) A thin porridge", "(N) Something punishing or exhausting"],
"grumble": ["(V) To complain quietly", "(N) A low, complaining sound"],
"grunt": ["(V) To make a deep, short sound", "(N) A low-ranking soldier (slang)"],
"guard": ["(N) A person who protects", "(V) To watch over"],
"guess": ["(V) To estimate without certainty", "(N) A conjecture or assumption"],
"guest": ["(N) A person invited to visit", "(N) A paying customer at a hotel"],
"guide": ["(N) A person who leads or directs", "(V) To show the way"],
"guild": ["(N) An association of craftsmen", "(N) A group formed for mutual aid"],
"guile": ["(N) Sly or cunning intelligence", "(N) Crafty deceit"],
"guilt": ["(N) Responsibility for wrongdoing", "(N) A feeling of remorse"],
"guise": ["(N) An outward appearance", "(N) A false or deceptive form"],
"gulf": ["(N) A large sea inlet", "(N) A wide gap or separation"],
"gull": ["(N) A seabird", "(V) To deceive or trick"],
"gulp": ["(V) To swallow quickly", "(N) A large, hurried swallow"],
"gum": ["(N) A sticky substance from trees", "(N) The tissue around the teeth"],
"gun": ["(N) A weapon that fires bullets", "(V) To accelerate rapidly (informal)"],
"gush": ["(V) To flow out suddenly", "(V) To speak with excessive enthusiasm"],
"gust": ["(N) A sudden strong wind", "(N) A burst of emotion"],
"gut": ["(N) The stomach or intestines", "(V) To remove the insides of something"],
"gutter": ["(N) A channel for carrying off rainwater", "(N) The lowest or dirtiest level"],
"guy": ["(N) A man or person", "(V) To mock or ridicule"],
"gym": ["(N) A place for physical exercise", "(N) A school class for athletics"],
"gypsum": ["(N) A soft mineral used in plaster", "(N) A hydrated calcium sulfate"],
"gypsy": ["(N) A member of the Romani people", "(N) A wanderer or traveler (informal)"],
"gyrate": ["(V) To move in a circular motion", "(V) To spin rapidly"],
"gyro": ["(N) A Greek sandwich", "(N) A device for measuring rotation"],
"habit": ["(N) A regular practice or routine", "(N) A long, loose garment worn by monks"],
"habitat": ["(N) The natural home of an organism", "(N) An environment suited for life"],
"hack": ["(V) To cut roughly", "(N) A person who does dull work"],
"hacker": ["(N) A person skilled at breaking into computer systems", "(N) Someone who tinkers with technology"],
"hail": ["(N) Frozen pellets of ice", "(V) To call out or greet"],
"hair": ["(N) The strands growing from skin", "(N) A very small amount"],
"haircut": ["(N) A style of trimmed hair", "(N) A reduction in value (finance)"],
"half": ["(N) One of two equal parts", "(Adj) Partial or incomplete"],
"hall": ["(N) A large room or corridor", "(N) A building for public events"],
"halt": ["(V) To stop suddenly", "(N) A temporary stop"],
"ham": ["(N) Cured pork meat", "(N) An overly theatrical performer"],
"hammer": ["(N) A tool for pounding nails", "(V) To strike forcefully"],
"hamper": ["(V) To hinder or obstruct", "(N) A basket for laundry"],
"hand": ["(N) The end part of the arm", "(V) To give or pass something"],
"handful": ["(N) A small quantity", "(N) A difficult person to manage"],
"handle": ["(N) A part designed to be held", "(V) To manage or deal with"],
"handsome": ["(Adj) Good-looking", "(Adj) Generous in amount"],
"handy": ["(Adj) Useful or convenient", "(Adj) Skilled with manual tasks"],
"hang": ["(V) To suspend from above", "(V) To linger or remain"],
"happen": ["(V) To occur or take place", "(V) To come about by chance"],
"happy": ["(Adj) Feeling pleasure", "(Adj) Willing or ready (as in 'happy to help')"],
"harbor": ["(N) A sheltered port", "(V) To keep in mind secretly"],
"hard": ["(Adj) Firm or solid", "(Adv) With great effort"],
"harden": ["(V) To make firm", "(V) To become unfeeling"],
"hardly": ["(Adv) Barely or scarcely", "(Adv) Not quite"],
"hare": ["(N) A fast-running mammal", "(V) To run quickly (informal)"],
"hark": ["(V) To listen attentively", "(V) To pay close attention"],
"harm": ["(N) Physical or mental injury", "(V) To cause damage"],
"harp": ["(N) A stringed musical instrument", "(V) To dwell on repeatedly"],
"harsh": ["(Adj) Rough or severe", "(Adj) Unpleasant to the senses"],
"harvest": ["(N) The gathering of crops", "(V) To collect or gather"],
"haste": ["(N) Speed or urgency", "(V) To hurry (archaic)"],
"hasty": ["(Adj) Done quickly", "(Adj) Rash or impulsive"],
"hat": ["(N) A head covering", "(N) A role or position (as in 'wear many hats')"],
"hatch": ["(V) To emerge from an egg", "(N) A small opening or door"],
"hate": ["(V) To feel intense dislike", "(N) Strong aversion"],
"haul": ["(V) To pull or drag", "(N) A large amount gained at once"],
"haunt": ["(V) To visit repeatedly in the mind", "(N) A place frequently visited"],
"have": ["(V) To possess or own", "(V) To experience or undergo"],
"haven": ["(N) A safe place", "(N) A refuge or sanctuary"],
"hawk": ["(N) A bird of prey", "(V) To sell aggressively"],
"hay": ["(N) Dried grass for animals", "(N) A rural field (informal)"],
"hazard": ["(N) A danger or risk", "(V) To venture or risk"],
"haze": ["(N) A slight obscurity in the air", "(V) To make cloudy or unclear"],
"hazel": ["(N) A type of tree", "(Adj) Light brown with green or gold tones"],
"head": ["(N) The upper part of the body", "(V) To lead or direct"],
"headache": ["(N) Pain in the head", "(N) A source of annoyance"],
"heal": ["(V) To restore to health", "(V) To mend or repair"],
"health": ["(N) The state of well-being", "(N) A person’s physical condition"],
"heap": ["(N) A pile of things", "(V) To pile up"],
"hear": ["(V) To perceive sound", "(V) To be informed of something"],
"heart": ["(N) The organ that pumps blood", "(N) The center of emotion"],
"hearty": ["(Adj) Warm and enthusiastic", "(Adj) Substantial or filling"],
"heat": ["(N) Warmth or high temperature", "(V) To make hot"],
"heave": ["(V) To lift with effort", "(V) To throw or toss"],
"heaven": ["(N) A place of divine beings", "(N) A state of bliss"],
"heavy": ["(Adj) Weighing a lot", "(Adj) Serious or intense"],
"hedge": ["(N) A row of shrubs", "(V) To avoid giving a clear answer"],
"heed": ["(V) To pay attention to", "(N) Careful notice"],
"heel": ["(N) The back part of the foot", "(N) A contemptible person (informal)"],
"height": ["(N) The measurement from base to top", "(N) The highest point"],
"heir": ["(N) A person entitled to inherit", "(N) A successor to a position"],
"heist": ["(N) A robbery", "(V) To steal (slang)"],
"held": ["(V) Past tense of hold", "(V) Kept or maintained"],
"hell": ["(N) A place of torment", "(N) A severe or unpleasant situation"],
"helm": ["(N) A steering apparatus", "(V) To take charge of"],
"helmet": ["(N) Protective headgear", "(N) A covering for safety"],
"help": ["(V) To assist", "(N) Aid or support"],
"hem": ["(N) The edge of a garment", "(V) To fold and sew the edge"],
"hen": ["(N) A female chicken", "(N) A woman (informal, dated)"],
"her": ["(Pron) The object form of 'she'", "(Det) Belonging to a female"],
"herald": ["(N) A messenger announcing news", "(V) To signal the arrival of"],
"herb": ["(N) A plant used for flavor or medicine", "(N) A non-woody plant"],
"herd": ["(N) A group of animals", "(V) To gather or move as a group"],
"here": ["(Adv) In this place", "(Interj) Used to attract attention"],
"heritage": ["(N) Traditions passed down", "(N) Property inherited"],
"hero": ["(N) A person admired for courage", "(N) The main character in a story"],
"heroic": ["(Adj) Brave or noble", "(Adj) Grand or impressive"],
"hesitate": ["(V) To pause before acting", "(V) To be reluctant"],
"hex": ["(N) A spell or curse", "(V) To cast a spell on"],
"hey": ["(Interj) A greeting or call for attention", "(Interj) An expression of surprise"],
"hibernate": ["(V) To sleep through winter", "(V) To remain inactive"],
"hiccup": ["(N) A sudden diaphragm spasm", "(N) A small, unexpected problem"],
"hide": ["(V) To conceal", "(N) The skin of an animal"],
"high": ["(Adj) Tall or elevated", "(Adj) Euphoric or intoxicated"],
"highlight": ["(N) The best or most important part", "(V) To emphasize"],
"highway": ["(N) A major public road", "(N) A main route for travel"],
"hike": ["(V) To walk long distances", "(N) A long outdoor walk"],
"hill": ["(N) A raised area of land", "(N) A slope or incline"],
"hinder": ["(V) To obstruct or delay", "(V) To make difficult"],
"hinge": ["(N) A joint allowing movement", "(V) To depend entirely on"],
"hint": ["(N) A small suggestion", "(V) To imply subtly"],
"hip": ["(N) The joint between thigh and pelvis", "(Adj) Stylish or trendy"],
"hire": ["(V) To employ", "(N) Payment for temporary use"],
"his": ["(Det) Belonging to a male", "(Pron) Something owned by him"],
"hiss": ["(V) To make a sharp s-sound", "(N) A prolonged sibilant noise"],
"history": ["(N) The study of past events", "(N) A record of past occurrences"],
"hit": ["(V) To strike", "(N) A successful or popular item"],
"hitch": ["(V) To fasten or connect", "(N) A problem or delay"],
"hive": ["(N) A colony of bees", "(V) To store or gather"],
"hoard": ["(V) To accumulate secretly", "(N) A hidden supply"],
"hoarse": ["(Adj) Rough or husky in voice", "(Adj) Harsh-sounding"],
"hobble": ["(V) To walk with difficulty", "(V) To impede progress"],
"hobby": ["(N) A leisure activity", "(N) A small horse (archaic)"],
"hockey": ["(N) A sport played on ice or field", "(N) The equipment used in the sport"],
"hoe": ["(N) A gardening tool", "(V) To cultivate with a hoe"],
"hog": ["(N) A pig", "(V) To take more than one’s share"],
"hoist": ["(V) To lift or raise", "(N) A device for lifting"],
"hold": ["(V) To grasp or keep", "(N) A grip or control"],
"hole": ["(N) An opening or cavity", "(N) A difficult situation (informal)"],
"holiday": ["(N) A day of celebration", "(N) A vacation or break"],
"hollow": ["(Adj) Empty inside", "(N) A small valley or depression"],
"holy": ["(Adj) Sacred or divine", "(Adj) Morally pure"],
"home": ["(N) A place where one lives", "(Adv) To or toward one’s residence"],
"honest": ["(Adj) Truthful and sincere", "(Adj) Genuine or fair"],
"honey": ["(N) A sweet substance made by bees", "(N) A term of affection"],
"honor": ["(N) High respect", "(V) To show esteem"],
"hood": ["(N) A covering for the head", "(N) A neighborhood (slang)"],
"hoof": ["(N) The hard foot of certain animals", "(V) To walk or travel (informal)"],
"hook": ["(N) A curved piece for catching", "(V) To attach or secure"],
"hoop": ["(N) A circular band", "(V) To encircle or bind"],
"hoot": ["(N) A loud call (owl)", "(V) To shout or jeer"],
"hope": ["(N) A feeling of expectation", "(V) To desire a positive outcome"],
"horn": ["(N) A hard projection on an animal", "(N) A wind instrument"],
"horrid": ["(Adj) Extremely unpleasant", "(Adj) Terrible or dreadful"],
"horror": ["(N) Intense fear", "(N) A genre of frightening stories"],
"horse": ["(N) A large four-legged mammal", "(V) To play roughly (informal)"],
"hose": ["(N) A flexible tube for water", "(V) To spray with water"],
"hospital": ["(N) A place for medical treatment", "(N) An institution for the sick"],
"host": ["(N) A person who receives guests", "(V) To organize or present"],
"hostile": ["(Adj) Unfriendly or aggressive", "(Adj) Opposed or antagonistic"],
"hot": ["(Adj) Having high temperature", "(Adj) Popular or in demand"],
"hotel": ["(N) A place offering lodging", "(N) A commercial accommodation"],
"hound": ["(N) A hunting dog", "(V) To pursue relentlessly"],
"hour": ["(N) A period of sixty minutes", "(N) A specific time of day"],
"house": ["(N) A building for living", "(V) To provide shelter"],
"hover": ["(V) To remain suspended in air", "(V) To linger uncertainly"],
"howl": ["(V) To make a long, loud cry", "(N) A wailing sound"],
"hub": ["(N) The central part of a wheel", "(N) A center of activity"],
"huddle": ["(V) To gather closely", "(N) A tight group"],
"hue": ["(N) A color or shade", "(N) A characteristic appearance"],
"huff": ["(N) A fit of anger", "(V) To blow out air loudly"],
"hug": ["(V) To embrace warmly", "(N) A close, affectionate hold"],
"huge": ["(Adj) Very large", "(Adj) Enormous in size"],
"hull": ["(N) The outer covering of a seed or fruit", "(N) The body of a ship"],
"hum": ["(V) To make a low, steady sound", "(N) A continuous vibration"],
"human": ["(Adj) Relating to people", "(N) A person"],
"humble": ["(Adj) Modest or unassuming", "(V) To lower in pride"],
"humid": ["(Adj) Moist or damp in the air", "(Adj) Having high humidity"],
"humiliate": ["(V) To embarrass deeply", "(V) To make someone feel ashamed"],
"humor": ["(N) The quality of being amusing", "(V) To indulge or comply with"],
"hump": ["(N) A rounded raised area", "(V) To carry with effort"],
"hunch": ["(N) A gut feeling", "(V) To bend forward"],
"hundred": ["(N) The number 100", "(Adj) One hundred in count"],
"hunger": ["(N) The need for food", "(V) To crave strongly"],
"hunt": ["(V) To search for animals", "(N) A pursuit or chase"],
"hurdle": ["(N) A barrier to jump over", "(V) To overcome an obstacle"],
"hurl": ["(V) To throw forcefully", "(V) To vomit (informal)"],
"hurt": ["(V) To cause pain", "(Adj) Injured or upset"],
"hush": ["(V) To make quiet", "(N) Silence or calm"],
"husk": ["(N) The dry outer covering of a seed", "(V) To remove the husk"],
"hustle": ["(V) To move quickly", "(N) A busy activity or scheme"],
"hut": ["(N) A small, simple shelter", "(N) A crude dwelling"],
"hymn": ["(N) A religious song", "(V) To praise in song"],
"hyper": ["(Adj) Extremely energetic", "(Adj) Overexcited or nervous"],
"hypnotize": ["(V) To put into a trance", "(V) To fascinate completely"],
"hypothesis": ["(N) A proposed explanation", "(N) A theory requiring testing"],
"ice": ["(N) Frozen water", "(V) To cover with icing or frost"],
"iceberg": ["(N) A large floating mass of ice", "(N) A small visible part of something larger"],
"icicle": ["(N) A hanging spike of ice", "(N) Something cold or rigid"],
"icy": ["(Adj) Covered with ice", "(Adj) Cold in manner or tone"],
"idea": ["(N) A thought or concept", "(N) A plan or suggestion"],
"ideal": ["(Adj) Perfect or most suitable", "(N) A standard of perfection"],
"identify": ["(V) To recognize or establish identity", "(V) To associate closely with"],
"idiom": ["(N) A phrase with a figurative meaning", "(N) A style of expression"],
"idle": ["(Adj) Not active or working", "(V) To spend time doing nothing"],
"idol": ["(N) A greatly admired person", "(N) A statue worshipped as a deity"],
"ignite": ["(V) To set on fire", "(V) To spark emotion or excitement"],
"ignore": ["(V) To pay no attention to", "(V) To disregard intentionally"],
"ill": ["(Adj) Sick or unwell", "(Adv) Badly or poorly"],
"illegal": ["(Adj) Against the law", "(Adj) Not permitted by rules"],
"illuminate": ["(V) To light up", "(V) To clarify or explain"],
"illusion": ["(N) A false perception", "(N) A deceptive appearance"],
"illustrate": ["(V) To explain with examples", "(V) To provide pictures for a text"],
"image": ["(N) A visual representation", "(V) To picture in the mind"],
"imagine": ["(V) To form a mental picture", "(V) To suppose or assume"],
"imitate": ["(V) To copy or mimic", "(V) To reproduce behavior or style"],
"immense": ["(Adj) Extremely large", "(Adj) Vast in degree or scale"],
"immerse": ["(V) To submerge in liquid", "(V) To involve deeply"],
"immigrant": ["(N) A person who moves to a new country", "(N) Someone settling permanently elsewhere"],
"imminent": ["(Adj) About to happen", "(Adj) Impending or near"],
"immune": ["(Adj) Protected from disease", "(Adj) Exempt from obligation"],
"impact": ["(N) A strong effect", "(V) To collide or influence strongly"],
"impart": ["(V) To give or communicate", "(V) To bestow a quality"],
"impatient": ["(Adj) Unable to wait calmly", "(Adj) Eager for something to happen"],
"impeach": ["(V) To charge a public official with misconduct", "(V) To challenge credibility"],
"impede": ["(V) To obstruct progress", "(V) To slow down movement"],
"impel": ["(V) To drive or urge forward", "(V) To motivate strongly"],
"imperial": ["(Adj) Relating to an empire", "(Adj) Majestic or grand"],
"impersonate": ["(V) To mimic someone", "(V) To pretend to be another person"],
"impertinent": ["(Adj) Rude or disrespectful", "(Adj) Irrelevant to the matter"],
"implant": ["(V) To insert into the body", "(N) A device placed inside tissue"],
"implement": ["(N) A tool or instrument", "(V) To carry out or put into effect"],
"implicate": ["(V) To show involvement in wrongdoing", "(V) To imply or suggest indirectly"],
"implicit": ["(Adj) Implied but not stated", "(Adj) Absolute or unquestioning"],
"imply": ["(V) To suggest indirectly", "(V) To indicate without stating"],
"import": ["(V) To bring goods into a country", "(N) Significance or importance"],
"impose": ["(V) To force something on others", "(V) To take advantage of"],
"impress": ["(V) To make a strong impact on", "(N) A mark or imprint"],
"imprint": ["(V) To stamp or impress", "(N) A lasting effect"],
"improve": ["(V) To make better", "(V) To enhance quality"],
"impulse": ["(N) A sudden urge", "(N) A driving force"],
"inability": ["(N) Lack of ability", "(N) Incapacity to perform"],
"inaugurate": ["(V) To formally begin or introduce", "(V) To induct into office"],
"incapable": ["(Adj) Lacking ability", "(Adj) Unable to perform a task"],
"incense": ["(N) A fragrant substance burned for aroma", "(V) To make extremely angry"],
"incentive": ["(N) A reward motivating action", "(N) Something encouraging effort"],
"inception": ["(N) The beginning of something", "(N) The initial stage"],
"inch": ["(N) A unit of length", "(V) To move slowly and carefully"],
"incident": ["(N) An event or occurrence", "(N) A minor conflict or disturbance"],
"incline": ["(V) To lean or bend", "(N) A sloping surface"],
"include": ["(V) To contain as part of a whole", "(V) To involve or comprise"],
"income": ["(N) Money earned", "(N) Revenue or earnings"],
"increase": ["(V) To become larger", "(N) A rise in amount"],
"incur": ["(V) To bring upon oneself", "(V) To become subject to"],
"indeed": ["(Adv) Truly or certainly", "(Adv) Used to emphasize"],
"indefinite": ["(Adj) Not clearly defined", "(Adj) Lasting for an unknown time"],
"independent": ["(Adj) Free from control", "(N) A person not aligned with a group"],
"index": ["(N) An alphabetical list of topics", "(V) To arrange or categorize"],
"indicate": ["(V) To point out", "(V) To show or suggest"],
"indict": ["(V) To formally accuse", "(V) To charge with a crime"],
"indifferent": ["(Adj) Unconcerned or apathetic", "(Adj) Neither good nor bad"],
"indigo": ["(N) A deep blue color", "(Adj) Dark purplish-blue"],
"indoor": ["(Adj) Located inside", "(Adj) Intended for interior use"],
"induce": ["(V) To persuade or influence", "(V) To bring about or cause"],
"indulge": ["(V) To allow oneself pleasure", "(V) To yield to a desire"],
"industry": ["(N) Economic activity or manufacturing", "(N) Hard work or diligence"],
"inept": ["(Adj) Clumsy or incompetent", "(Adj) Lacking skill"],
"inert": ["(Adj) Unable to move", "(Adj) Chemically inactive"],
"inevitable": ["(Adj) Certain to happen", "(Adj) Unavoidable"],
"infer": ["(V) To conclude from evidence", "(V) To deduce indirectly"],
"inferior": ["(Adj) Lower in quality", "(N) A person of lower rank"],
"infinite": ["(Adj) Without limits", "(Adj) Endless or immeasurable"],
"inflame": ["(V) To arouse strong emotion", "(V) To set on fire"],
"inflation": ["(N) A rise in prices", "(N) Expansion or swelling"],
"influence": ["(N) The power to affect others", "(V) To sway or shape behavior"],
"inform": ["(V) To give knowledge", "(V) To shape or influence"],
"information": ["(N) Knowledge or facts", "(N) Data communicated"],
"infrared": ["(Adj) Relating to wavelengths beyond red light", "(N) Infrared radiation"],
"infringe": ["(V) To violate or break a rule", "(V) To encroach upon"],
"infuse": ["(V) To fill with a quality", "(V) To steep in liquid"],
"ingenious": ["(Adj) Clever and inventive", "(Adj) Resourceful"],
"ingest": ["(V) To take into the body", "(V) To absorb information"],
"inhabit": ["(V) To live in a place", "(V) To occupy or dwell"],
"inhale": ["(V) To breathe in", "(V) To draw air or gas into lungs"],
"inherit": ["(V) To receive from a predecessor", "(V) To acquire genetically"],
"initial": ["(Adj) Occurring at the beginning", "(N) The first letter of a name"],
"initiate": ["(V) To begin or start", "(V) To admit into a group"],
"inject": ["(V) To force into with a syringe", "(V) To introduce suddenly"],
"injure": ["(V) To cause physical harm", "(V) To damage or hurt"],
"ink": ["(N) A colored fluid for writing", "(V) To sign or mark"],
"inn": ["(N) A small hotel", "(N) A lodging place for travelers"],
"inner": ["(Adj) Located inside", "(Adj) Relating to the mind or emotions"],
"innocent": ["(Adj) Not guilty", "(Adj) Pure or harmless"],
"innovate": ["(V) To introduce new ideas", "(V) To modernize"],
"input": ["(N) Information entered", "(V) To provide data"],
"inquire": ["(V) To ask for information", "(V) To investigate"],
"insane": ["(Adj) Mentally ill", "(Adj) Extremely foolish"],
"inscribe": ["(V) To write or carve on a surface", "(V) To dedicate formally"],
"insert": ["(V) To put into something", "(N) Something placed inside"],
"inside": ["(Prep) Within", "(N) The interior"],
"insight": ["(N) Deep understanding", "(N) An intuitive perception"],
"insist": ["(V) To demand firmly", "(V) To maintain as true"],
"inspect": ["(V) To examine closely", "(V) To review officially"],
"inspire": ["(V) To motivate creatively", "(V) To fill with emotion"],
"install": ["(V) To set up for use", "(V) To place in office"],
"instance": ["(N) An example or case", "(V) To cite as an example"],
"instant": ["(Adj) Immediate", "(N) A very short moment"],
"instead": ["(Adv) In place of", "(Adv) As an alternative"],
"instinct": ["(N) Natural impulse", "(N) Inborn tendency"],
"instruct": ["(V) To teach or direct", "(V) To order or command"],
"instrument": ["(N) A tool or device", "(N) A musical device"],
"insulate": ["(V) To protect from heat or cold", "(V) To isolate from influence"],
"insult": ["(V) To speak disrespectfully", "(N) An offensive remark"],
"insure": ["(V) To provide insurance", "(V) To guarantee against loss"],
"intact": ["(Adj) Undamaged", "(Adj) Whole or complete"],
"intake": ["(N) The amount consumed", "(N) A place where air or fluid enters"],
"integer": ["(N) A whole number", "(N) A number without fractions"],
"integrate": ["(V) To combine into a whole", "(V) To include all groups equally"],
"integrity": ["(N) Honesty and moral uprightness", "(N) Wholeness or unity"],
"intellect": ["(N) The ability to think", "(N) A highly intelligent person"],
"intense": ["(Adj) Very strong", "(Adj) Deep or extreme"],
"interact": ["(V) To communicate or work together", "(V) To affect one another"],
"interest": ["(N) Curiosity or concern", "(N) Money earned on savings"],
"interfere": ["(V) To meddle or obstruct", "(V) To hinder progress"],
"interior": ["(N) The inside part", "(Adj) Inner or internal"],
"interject": ["(V) To insert abruptly", "(V) To interrupt with a remark"],
"interlock": ["(V) To fit together", "(V) To connect securely"],
"interlude": ["(N) A break between events", "(N) A short performance"],
"intermediate": ["(Adj) Between two levels", "(N) A middle stage"],
"internal": ["(Adj) Inside or within", "(Adj) Relating to inner structure"],
"international": ["(Adj) Involving multiple nations", "(N) A foreign representative"],
"interpret": ["(V) To explain meaning", "(V) To translate orally"],
"interrupt": ["(V) To stop temporarily", "(V) To break continuity"],
"interval": ["(N) A pause or break", "(N) The distance between two points"],
"intervene": ["(V) To come between", "(V) To interfere to change outcome"],
"interview": ["(N) A formal meeting for questions", "(V) To question for information"],
"intimate": ["(Adj) Close or personal", "(V) To hint or suggest"],
"into": ["(Prep) Entering or going within", "(Prep) Indicating transformation"],
"intone": ["(V) To speak in a steady tone", "(V) To chant or recite"],
"intoxicate": ["(V) To make drunk", "(V) To excite or exhilarate"],
"intricate": ["(Adj) Complex and detailed", "(Adj) Hard to understand"],
"intrigue": ["(V) To arouse curiosity", "(N) A secret plot"],
"introduce": ["(V) To present for the first time", "(V) To bring into use"],
"invade": ["(V) To enter forcefully", "(V) To intrude upon"],
"invent": ["(V) To create something new", "(V) To fabricate a story"],
"inventory": ["(N) A list of goods", "(V) To make a detailed list"],
"invert": ["(V) To turn upside down", "(V) To reverse order"],
"invest": ["(V) To put money into for profit", "(V) To devote time or effort"],
"investigate": ["(V) To examine thoroughly", "(V) To inquire into"],
"invite": ["(V) To ask someone to attend", "(V) To encourage or attract"],
"involve": ["(V) To include as part", "(V) To engage or affect"],
"ion": ["(N) A charged atom", "(N) An electrically charged particle"],
"iron": ["(N) A strong metal", "(V) To press clothes smooth"],
"irony": ["(N) A contrast between expectation and reality", "(N) A humorous or sarcastic twist"],
"irrigate": ["(V) To supply water to land", "(V) To flush with liquid"],
"irritate": ["(V) To annoy or anger", "(V) To cause inflammation"],
"island": ["(N) A piece of land surrounded by water", "(N) Something isolated"],
"isolate": ["(V) To separate from others", "(V) To set apart for study"],
"issue": ["(N) A topic of concern", "(V) To distribute or release"],
"itch": ["(N) An irritating sensation", "(V) To feel a need to scratch"],
"item": ["(N) A single thing", "(N) A news report or entry"],
"ivory": ["(N) A hard white material from tusks", "(Adj) Creamy white in color"],
"ivy": ["(N) A climbing plant", "(N) A symbol of academic tradition"],
"jab": ["(V) To poke sharply", "(N) A quick, sharp blow"],
"jacket": ["(N) A short coat", "(N) A protective covering"],
"jade": ["(N) A green gemstone", "(Adj) Of a dull green color"],
"jagged": ["(Adj) Having sharp, uneven edges", "(Adj) Rough or irregular"],
"jail": ["(N) A place of confinement", "(V) To imprison"],
"jam": ["(N) A fruit spread", "(V) To press tightly together"],
"jangle": ["(V) To make a harsh ringing sound", "(N) A discordant noise"],
"janitor": ["(N) A person who cleans and maintains buildings", "(N) A caretaker"],
"jar": ["(N) A container with a wide mouth", "(V) To shake or disturb"],
"jargon": ["(N) Specialized language of a group", "(N) Confusing technical speech"],
"jasmine": ["(N) A fragrant flowering plant", "(N) A scent derived from the plant"],
"jaunt": ["(N) A short, pleasant trip", "(V) To travel for pleasure"],
"javelin": ["(N) A light spear thrown in sport", "(N) A weapon used for throwing"],
"jaw": ["(N) The bones of the mouth", "(V) To chatter or talk (informal)"],
"jay": ["(N) A brightly colored bird", "(N) A foolish person (slang)"],
"jazz": ["(N) A style of music with improvisation", "(V) To enliven or excite"],
"jealous": ["(Adj) Feeling envy", "(Adj) Protective of affection"],
"jeans": ["(N) Denim trousers", "(N) Casual pants made of sturdy fabric"],
"jeer": ["(V) To mock loudly", "(N) A rude or mocking remark"],
"jelly": ["(N) A soft, sweet spread", "(N) A gelatinous substance"],
"jeopardy": ["(N) Danger or risk", "(N) Exposure to harm"],
"jerk": ["(V) To pull suddenly", "(N) A rude or foolish person"],
"jester": ["(N) A historical entertainer", "(N) A person who jokes"],
"jet": ["(N) A fast aircraft", "(N) A stream of liquid or gas"],
"jewel": ["(N) A precious stone", "(N) Something treasured"],
"jingle": ["(N) A light ringing sound", "(V) To make a tinkling noise"],
"jitter": ["(N) Nervous movement", "(V) To act nervously"],
"job": ["(N) A task or occupation", "(N) A responsibility or duty"],
"jockey": ["(N) A horse rider in races", "(V) To maneuver for advantage"],
"jog": ["(V) To run at a slow pace", "(N) A gentle run"],
"join": ["(V) To connect or unite", "(N) A point of connection"],
"joint": ["(N) A place where two things meet", "(N) A marijuana cigarette (slang)"],
"joke": ["(N) Something said to amuse", "(V) To speak humorously"],
"jolly": ["(Adj) Cheerful and lively", "(V) To encourage playfully"],
"jolt": ["(V) To shock or shake", "(N) A sudden movement"],
"jostle": ["(V) To push roughly", "(V) To compete for position"],
"journal": ["(N) A daily record", "(N) A periodical publication"],
"journey": ["(N) A trip from one place to another", "(V) To travel"],
"jovial": ["(Adj) Cheerful and friendly", "(Adj) Full of good humor"],
"joy": ["(N) Great happiness", "(V) To rejoice (archaic)"],
"judge": ["(N) A public official who decides cases", "(V) To form an opinion"],
"judgment": ["(N) A decision or opinion", "(N) The ability to make wise choices"],
"jug": ["(N) A large container with a handle", "(V) To put into a jug"],
"juice": ["(N) Liquid from fruit", "(N) Power or influence (slang)"],
"juicy": ["(Adj) Full of juice", "(Adj) Interesting or scandalous"],
"jumble": ["(V) To mix in confusion", "(N) A disordered mixture"],
"jump": ["(V) To leap into the air", "(N) A sudden movement"],
"junction": ["(N) A point where things meet", "(N) A place where roads or tracks cross"],
"jungle": ["(N) A dense tropical forest", "(N) A wild or chaotic place"],
"junior": ["(Adj) Younger or lower in rank", "(N) A younger person"],
"junk": ["(N) Old or discarded material", "(V) To throw away"],
"junta": ["(N) A military group ruling a country", "(N) A political faction"],
"juror": ["(N) A member of a jury", "(N) A person sworn to give a verdict"],
"jury": ["(N) A group deciding a legal case", "(N) A panel judging a competition"],
"just": ["(Adj) Fair or morally right", "(Adv) Exactly or only"],
"justice": ["(N) Fair treatment", "(N) The administration of law"],
"justify": ["(V) To show to be right", "(V) To give valid reasons"],
"jut": ["(V) To extend outward", "(N) A projecting part"],
"juvenile": ["(Adj) Youthful or immature", "(N) A young person"],
"kale": ["(N) A leafy green vegetable", "(N) A hardy cabbage variety"],
"kangaroo": ["(N) A large Australian marsupial", "(N) A person who jumps around energetically (informal)"],
"karat": ["(N) A unit measuring gold purity", "(N) A measure of fineness"],
"keen": ["(Adj) Sharp or eager", "(Adj) Intense or enthusiastic"],
"keep": ["(V) To retain possession of", "(N) A stronghold or fortress"],
"keg": ["(N) A small barrel", "(N) A container for beer"],
"kelp": ["(N) A large seaweed", "(N) Marine algae used as fertilizer"],
"ken": ["(N) Range of knowledge", "(V) To know or recognize (Scottish)"],
"kernel": ["(N) The inner part of a seed", "(N) The essential core of something"],
"kettle": ["(N) A container for boiling water", "(N) A metal pot used over fire"],
"key": ["(N) A device for unlocking", "(Adj) Essential or crucial"],
"keyboard": ["(N) A panel of keys for typing", "(N) A musical instrument with keys"],
"kick": ["(V) To strike with the foot", "(N) A burst of energy or excitement"],
"kid": ["(N) A child", "(V) To tease or joke"],
"kidnap": ["(V) To abduct someone", "(V) To seize and hold unlawfully"],
"kidney": ["(N) An organ that filters blood", "(N) A type or temperament (archaic)"],
"kill": ["(V) To cause death", "(N) A successful hunt"],
"kiln": ["(N) A furnace for baking pottery", "(V) To fire in a kiln"],
"kilogram": ["(N) A metric unit of mass", "(N) 1000 grams"],
"kilometer": ["(N) A metric unit of distance", "(N) 1000 meters"],
"kin": ["(N) Family or relatives", "(Adj) Related by blood"],
"kind": ["(Adj) Caring or gentle", "(N) A type or category"],
"kindle": ["(V) To start a fire", "(V) To inspire emotion"],
"king": ["(N) A male monarch", "(N) The most important piece in chess"],
"kingdom": ["(N) A territory ruled by a king", "(N) A domain or sphere of control"],
"kink": ["(N) A twist or bend", "(N) An unusual habit or quirk"],
"kiss": ["(V) To touch with the lips", "(N) A gesture of affection"],
"kit": ["(N) A set of tools or supplies", "(N) A young fox"],
"kitchen": ["(N) A room for cooking", "(N) The staff who prepare food"],
"kite": ["(N) A flying toy", "(V) To soar or move lightly"],
"kitten": ["(N) A young cat", "(V) To give birth to kittens"],
"kiwi": ["(N) A small flightless bird", "(N) A brown fuzzy fruit"],
"knack": ["(N) A special skill", "(N) A clever way of doing something"],
"knapsack": ["(N) A backpack", "(N) A bag carried on the back"],
"knead": ["(V) To work dough with hands", "(V) To massage or squeeze"],
"knee": ["(N) The joint between thigh and shin", "(V) To strike with the knee"],
"kneel": ["(V) To rest on the knees", "(V) To show submission"],
"knell": ["(N) A solemn ringing of a bell", "(V) To signal doom or death"],
"knelt": ["(V) Past tense of kneel", "(V) Lowered oneself to knees"],
"knew": ["(V) Past tense of know", "(V) Understood or was aware"],
"knife": ["(N) A cutting tool", "(V) To stab or cut"],
"knight": ["(N) A medieval mounted soldier", "(V) To grant someone knighthood"],
"knit": ["(V) To make fabric with needles", "(V) To join closely together"],
"knob": ["(N) A rounded handle", "(N) A small lump or bump"],
"knock": ["(V) To strike a surface", "(N) A tapping sound"],
"knot": ["(N) A fastening made by tying", "(N) A tight, tangled mass"],
"know": ["(V) To be aware of", "(V) To recognize or understand"],
"knowledge": ["(N) Information or understanding", "(N) Awareness gained through experience"],
"known": ["(Adj) Recognized or familiar", "(Adj) Identified or acknowledged"],
"koala": ["(N) A tree-dwelling Australian marsupial", "(N) A symbol of Australia"],
"kosher": ["(Adj) Conforming to Jewish dietary laws", "(Adj) Legitimate or acceptable (informal)"],
"lab": ["(N) A place for scientific work", "(N) A shortened form of 'laboratory'"],
"label": ["(N) A tag identifying something", "(V) To classify or name"],
"labor": ["(N) Work, especially physical", "(V) To work hard"],
"lace": ["(N) A delicate fabric with open patterns", "(V) To fasten with laces"],
"lack": ["(N) A shortage or absence", "(V) To be without"],
"lad": ["(N) A boy or young man", "(N) A lively or spirited youth"],
"ladder": ["(N) A structure for climbing", "(N) A series of ascending stages"],
"laden": ["(Adj) Heavily loaded", "(Adj) Burdened with something"],
"lag": ["(V) To fall behind", "(N) A delay or slowing"],
"lake": ["(N) A large body of water", "(N) A pool or reservoir"],
"lamb": ["(N) A young sheep", "(V) To give birth to lambs"],
"lament": ["(V) To express sorrow", "(N) A passionate expression of grief"],
"lamp": ["(N) A device that gives light", "(N) A source of illumination"],
"lance": ["(N) A long spear", "(V) To pierce or cut open"],
"land": ["(N) The solid part of Earth", "(V) To arrive on ground"],
"landmark": ["(N) A notable feature of a landscape", "(N) An important event"],
"lane": ["(N) A narrow road", "(N) A designated path for travel"],
"language": ["(N) A system of communication", "(N) The style of expression"],
"languid": ["(Adj) Lacking energy", "(Adj) Slow or relaxed"],
"lap": ["(N) The area formed when sitting", "(V) To drink with the tongue (animals)"],
"lapse": ["(N) A temporary failure", "(V) To fall into error"],
"large": ["(Adj) Big in size", "(Adj) Abundant or generous"],
"lark": ["(N) A small singing bird", "(N) A carefree adventure"],
"lash": ["(V) To strike with a whip", "(N) An eyelash"],
"lass": ["(N) A girl or young woman", "(N) A female sweetheart"],
"last": ["(Adj) Final in order", "(V) To continue or endure"],
"latch": ["(N) A fastening device", "(V) To lock or secure"],
"late": ["(Adj) After the expected time", "(Adj) Recently deceased"],
"lather": ["(N) Foam from soap", "(V) To cover with foam"],
"laugh": ["(V) To express amusement", "(N) The sound of amusement"],
"launch": ["(V) To set in motion", "(N) The act of starting something"],
"laundry": ["(N) Clothes to be washed", "(N) A place where clothes are cleaned"],
"lavish": ["(Adj) Luxurious or abundant", "(V) To give generously"],
"law": ["(N) A rule established by authority", "(N) The field of legal study"],
"lawn": ["(N) A grassy area", "(N) A fine linen fabric"],
"lawsuit": ["(N) A legal action", "(N) A claim brought before a court"],
"lay": ["(V) To place down", "(Adj) Non-professional or not ordained"],
"layer": ["(N) A thickness of material", "(V) To arrange in levels"],
"laze": ["(V) To relax idly", "(V) To be lazy"],
"lazy": ["(Adj) Unwilling to work", "(Adj) Slow-moving or sluggish"],
"lead": ["(V) To guide or direct", "(N) A heavy metallic element"],
"leader": ["(N) One who leads", "(N) A person in command"],
"leaf": ["(N) A flat part of a plant", "(V) To turn pages quickly"],
"league": ["(N) A group formed for mutual benefit", "(N) A unit of distance (archaic)"],
"leak": ["(V) To let fluid escape", "(N) An unintended opening"],
"lean": ["(Adj) Thin or spare", "(V) To incline or rely"],
"leap": ["(V) To jump high or far", "(N) A sudden increase"],
"learn": ["(V) To acquire knowledge", "(V) To become aware of"],
"lease": ["(N) A rental contract", "(V) To rent out property"],
"leash": ["(N) A cord for controlling an animal", "(V) To restrain"],
"least": ["(Adj) Smallest in amount", "(Adv) To the smallest extent"],
"leather": ["(N) Treated animal skin", "(Adj) Made of leather"],
"leave": ["(V) To go away from", "(N) Permission to be absent"],
"lecture": ["(N) A formal talk", "(V) To scold or reprimand"],
"ledge": ["(N) A narrow shelf", "(N) A projecting rock formation"],
"left": ["(Adj) On the side of the body opposite right", "(V) Past tense of leave"],
"leg": ["(N) A limb used for walking", "(N) A section of a journey"],
"legacy": ["(N) Something handed down", "(N) A lasting impact"],
"legal": ["(Adj) Allowed by law", "(Adj) Relating to the law"],
"legend": ["(N) A traditional story", "(N) A famous person"],
"legible": ["(Adj) Easy to read", "(Adj) Clear or decipherable"],
"legion": ["(N) A large group", "(N) A military unit"],
"leisure": ["(N) Free time", "(N) Activities done for relaxation"],
"lemon": ["(N) A sour yellow fruit", "(N) Something defective (informal)"],
"lend": ["(V) To give temporarily", "(V) To contribute or add"],
"length": ["(N) The measurement of something long", "(N) A piece or stretch"],
"lens": ["(N) A curved piece of glass for focusing light", "(N) A viewpoint or perspective"],
"lent": ["(V) Past tense of lend", "(N) A Christian fasting period"],
"leopard": ["(N) A spotted wild cat", "(N) A swift, agile predator"],
"less": ["(Adj) Not as much", "(Adv) To a smaller extent"],
"lesson": ["(N) Something learned", "(N) A period of instruction"],
"lest": ["(Conj) For fear that", "(Conj) To avoid the risk of"],
"let": ["(V) To allow or permit", "(V) To rent out property"],
"letter": ["(N) A written message", "(N) A character in the alphabet"],
"level": ["(N) A flat horizontal surface", "(V) To make even"],
"lever": ["(N) A bar used to lift or move", "(V) To move with leverage"],
"levy": ["(V) To impose a tax", "(N) A required payment"],
"liar": ["(N) A person who tells lies", "(N) Someone untruthful"],
"liberal": ["(Adj) Open-minded or generous", "(N) A person favoring reform"],
"liberty": ["(N) Freedom from restraint", "(N) A privilege or right"],
"library": ["(N) A place with books", "(N) A collection of information"],
"license": ["(N) Official permission", "(V) To authorize"],
"lick": ["(V) To pass the tongue over", "(N) A small amount"],
"lid": ["(N) A cover for a container", "(N) An eyelid (informal)"],
"lie": ["(V) To recline", "(V) To speak falsely"],
"life": ["(N) The state of being alive", "(N) A way of living"],
"lift": ["(V) To raise upward", "(N) A ride or elevator"],
"light": ["(N) Something that makes things visible", "(Adj) Not heavy"],
"lighten": ["(V) To make brighter", "(V) To reduce weight or burden"],
"like": ["(V) To enjoy or approve", "(Prep) Similar to"],
"liken": ["(V) To compare with", "(V) To represent as similar"],
"lilac": ["(N) A fragrant flowering shrub", "(N) A pale purple color"],
"lily": ["(N) A flowering plant", "(N) A symbol of purity"],
"limb": ["(N) An arm or leg", "(N) A large branch of a tree"],
"lime": ["(N) A green citrus fruit", "(N) A calcium-based substance"],
"limit": ["(N) A boundary or restriction", "(V) To set bounds"],
"limp": ["(V) To walk unevenly", "(Adj) Lacking firmness"],
"line": ["(N) A long narrow mark", "(V) To cover the inside of something"],
"linger": ["(V) To stay longer than necessary", "(V) To be slow to disappear"],
"link": ["(N) A connection", "(V) To join together"],
"lion": ["(N) A large wild cat", "(N) A brave or important person"],
"lip": ["(N) The edge of the mouth", "(N) Impudent speech (slang)"],
"liquid": ["(N) A flowing substance", "(Adj) Not solid or gas"],
"list": ["(N) A series of items", "(V) To record or enumerate"],
"listen": ["(V) To pay attention to sound", "(V) To heed advice"],
"lit": ["(Adj) Illuminated", "(Adj) Exciting or excellent (slang)"],
"literal": ["(Adj) Taking words in their exact meaning", "(Adj) Not figurative"],
"litter": ["(N) Trash scattered around", "(V) To scatter waste"],
"little": ["(Adj) Small in size", "(Adv) To a small extent"],
"live": ["(V) To be alive", "(Adj) Happening in real time"],
"liver": ["(N) A vital organ", "(N) A person who lives in a certain way"],
"livid": ["(Adj) Furiously angry", "(Adj) Bluish or discolored"],
"load": ["(N) Something carried", "(V) To fill or pack"],
"loaf": ["(N) A shaped mass of bread", "(V) To idle or lounge"],
"loan": ["(N) Money lent", "(V) To lend"],
"loathe": ["(V) To hate intensely", "(V) To feel deep disgust"],
"lob": ["(V) To throw in a high arc", "(N) A high, arching shot"],
"lobby": ["(N) A public entrance hall", "(V) To influence lawmakers"],
"local": ["(Adj) Nearby or regional", "(N) A resident of the area"],
"locate": ["(V) To find or discover", "(V) To position or place"],
"lock": ["(N) A device for securing", "(V) To fasten securely"],
"lodge": ["(N) A small house or cabin", "(V) To become stuck"],
"loft": ["(N) An upper room or attic", "(V) To hit a ball high"],
"log": ["(N) A cut piece of wood", "(V) To record information"],
"logic": ["(N) Reasoning or sound judgment", "(N) A system of principles"],
"loin": ["(N) The part of the body near the hips", "(N) A cut of meat"],
"lonely": ["(Adj) Feeling alone", "(Adj) Isolated or deserted"],
"long": ["(Adj) Measuring a great distance", "(V) To yearn for"],
"look": ["(V) To direct one’s eyes", "(N) An appearance or expression"],
"loom": ["(V) To appear large or threatening", "(N) A machine for weaving"],
"loop": ["(N) A curved shape", "(V) To form into a loop"],
"loose": ["(Adj) Not tight", "(Adj) Free or released"],
"loot": ["(N) Stolen goods", "(V) To steal during chaos"],
"lord": ["(N) A nobleman", "(V) To act in a superior manner"],
"lose": ["(V) To misplace or be defeated", "(V) To fail to keep"],
"loss": ["(N) The act of losing", "(N) A decrease or deficit"],
"lot": ["(N) A large amount", "(N) A parcel of land"],
"loud": ["(Adj) Making much noise", "(Adj) Showy or bold"],
"lounge": ["(N) A comfortable sitting room", "(V) To relax lazily"],
"love": ["(N) Deep affection", "(V) To feel strong attachment"],
"lovely": ["(Adj) Beautiful or charming", "(Adj) Delightful"],
"lover": ["(N) A romantic partner", "(N) Someone fond of something"],
"low": ["(Adj) Not high", "(Adj) Depressed or weak"],
"loyal": ["(Adj) Faithful or devoted", "(Adj) Showing firm allegiance"],
"luck": ["(N) Success by chance", "(N) Fortune or fate"],
"lucky": ["(Adj) Fortunate", "(Adj) Bringing good luck"],
"lull": ["(V) To soothe or calm", "(N) A temporary pause"],
"lumber": ["(N) Processed wood", "(V) To move clumsily"],
"luminous": ["(Adj) Giving off light", "(Adj) Bright or radiant"],
"lump": ["(N) A small mass", "(V) To group together"],
"lunar": ["(Adj) Relating to the moon", "(Adj) Moon-like"],
"lunch": ["(N) A midday meal", "(V) To eat lunch"],
"lung": ["(N) An organ for breathing", "(N) A respiratory structure"],
"lure": ["(N) Something that attracts", "(V) To tempt or entice"],
"lurk": ["(V) To hide and wait", "(V) To move secretly"],
"lush": ["(Adj) Rich and abundant", "(N) A heavy drinker (slang)"],
"lust": ["(N) Intense desire", "(V) To crave passionately"],
"lute": ["(N) A stringed musical instrument", "(N) A sealant used in pottery"],
"luxury": ["(N) Great comfort or wealth", "(Adj) Expensive and high-quality"],
"lyric": ["(N) Words of a song", "(Adj) Expressing personal emotion"],
"machine": ["(N) A device with moving parts", "(V) To shape or finish by machine"],
"mad": ["(Adj) Very angry", "(Adj) Mentally ill or wildly excited"],
"made": ["(V) Past tense of make", "(Adj) Created or constructed"],
"magazine": ["(N) A periodical publication", "(N) A chamber for holding ammunition"],
"magic": ["(N) The art of producing illusions", "(Adj) Enchanting or supernatural"],
"magnet": ["(N) An object that attracts metal", "(N) Something that draws interest"],
"magnify": ["(V) To make larger", "(V) To exaggerate importance"],
"magnitude": ["(N) Size or extent", "(N) Great importance"],
"maid": ["(N) A female servant", "(N) An unmarried young woman (archaic)"],
"mail": ["(N) Letters and packages", "(V) To send by post"],
"main": ["(Adj) Most important", "(N) A principal pipe or cable"],
"maintain": ["(V) To keep in good condition", "(V) To assert or claim"],
"major": ["(Adj) Greater in importance", "(N) A military rank or college specialization"],
"make": ["(V) To create or produce", "(N) The brand or type of a product"],
"maker": ["(N) A creator or manufacturer", "(N) A person who produces something"],
"male": ["(Adj) Of the sex that produces sperm", "(N) A man or boy"],
"mall": ["(N) A shopping center", "(N) A public walkway (archaic)"],
"mammal": ["(N) A warm-blooded vertebrate with hair", "(N) An animal that nurses its young"],
"man": ["(N) An adult male human", "(V) To operate or staff"],
"manage": ["(V) To control or direct", "(V) To succeed despite difficulty"],
"mandate": ["(N) An official order", "(V) To require or command"],
"mane": ["(N) Long hair on the neck of an animal", "(N) A person’s thick hair (figurative)"],
"mango": ["(N) A tropical fruit", "(N) The tree that bears mangoes"],
"manner": ["(N) A way of doing something", "(N) Social behavior"],
"manor": ["(N) A large country house", "(N) An estate with land"],
"manual": ["(Adj) Done by hand", "(N) A handbook or guide"],
"manufacture": ["(V) To produce goods", "(N) The process of making products"],
"many": ["(Adj) A large number", "(Pron) Numerous people or things"],
"map": ["(N) A visual representation of an area", "(V) To chart or plan"],
"marble": ["(N) A hard stone used in sculpture", "(N) A small glass ball used in games"],
"march": ["(V) To walk in a steady rhythm", "(N) A month of the year"],
"margin": ["(N) The edge or border", "(N) The amount by which something exceeds"],
"marine": ["(Adj) Related to the sea", "(N) A member of the naval infantry"],
"mark": ["(N) A visible impression", "(V) To label or indicate"],
"market": ["(N) A place for buying and selling", "(V) To promote or sell products"],
"marry": ["(V) To wed", "(V) To combine harmoniously"],
"marsh": ["(N) A wetland area", "(N) Soft, waterlogged land"],
"mart": ["(N) A marketplace", "(N) A store or shop"],
"martial": ["(Adj) Relating to war or the military", "(Adj) Warlike in nature"],
"marvel": ["(N) Something wonderful", "(V) To be filled with wonder"],
"mask": ["(N) A covering for the face", "(V) To conceal or disguise"],
"mass": ["(N) A large quantity", "(N) A religious ceremony"],
"master": ["(N) A skilled expert", "(V) To become proficient in"],
"match": ["(N) A contest or pairing", "(V) To correspond or equal"],
"mate": ["(N) A companion or partner", "(V) To pair for reproduction"],
"material": ["(N) Substance from which things are made", "(Adj) Physical rather than spiritual"],
"math": ["(N) The study of numbers", "(N) Mathematical calculations"],
"matter": ["(N) A subject or issue", "(N) Physical substance"],
"mature": ["(Adj) Fully developed", "(V) To reach full growth"],
"maximum": ["(N) The greatest amount", "(Adj) As large as possible"],
"may": ["(V) To be permitted", "(N) The fifth month of the year"],
"maybe": ["(Adv) Possibly", "(N) A possibility or uncertainty"],
"maze": ["(N) A complex network of paths", "(V) To bewilder or confuse"],
"mead": ["(N) A fermented honey drink", "(N) A meadow (poetic)"],
"meal": ["(N) Food eaten at one time", "(N) Ground grain"],
"mean": ["(Adj) Unkind or harsh", "(V) To signify or intend"],
"measure": ["(V) To determine size or amount", "(N) A unit or standard"],
"meat": ["(N) Animal flesh used as food", "(N) The essential part of something"],
"mechanic": ["(N) A person who repairs machines", "(N) A manual worker"],
"medal": ["(N) A metal award", "(N) A symbol of achievement"],
"media": ["(N) Means of communication", "(N) Journalistic organizations"],
"medical": ["(Adj) Related to medicine", "(N) A medical examination (informal)"],
"medicine": ["(N) A substance used to treat illness", "(N) The science of healing"],
"medium": ["(N) A middle state", "(N) A means of communication"],
"meet": ["(V) To come together", "(N) A gathering for competition"],
"mellow": ["(Adj) Soft or gentle", "(V) To become more relaxed"],
"melody": ["(N) A sequence of musical notes", "(N) A tuneful arrangement"],
"melt": ["(V) To change from solid to liquid", "(V) To soften emotionally"],
"member": ["(N) A person belonging to a group", "(N) A part of a whole"],
"memory": ["(N) The ability to recall", "(N) Something remembered"],
"menace": ["(N) A threat or danger", "(V) To threaten"],
"mend": ["(V) To repair", "(V) To improve or heal"],
"mental": ["(Adj) Related to the mind", "(Adj) Performed in the mind"],
"mention": ["(V) To refer to briefly", "(N) A reference or remark"],
"menu": ["(N) A list of food options", "(N) A selection of choices"],
"merchant": ["(N) A person who buys and sells goods", "(N) A trader"],
"mercy": ["(N) Compassion or forgiveness", "(N) Relief from suffering"],
"mere": ["(Adj) Nothing more than", "(N) A small lake (archaic)"],
"merge": ["(V) To combine into one", "(V) To blend smoothly"],
"merit": ["(N) Worth or excellence", "(V) To deserve or earn"],
"merry": ["(Adj) Cheerful and lively", "(Adj) Festive or joyful"],
"mesh": ["(N) A net-like fabric", "(V) To fit together well"],
"mess": ["(N) A disorderly state", "(V) To make untidy"],
"metal": ["(N) A hard, shiny material", "(V) To cover with metal"],
"meter": ["(N) A unit of measurement", "(N) A device for measuring"],
"method": ["(N) A systematic way of doing something", "(N) A procedure or technique"],
"middle": ["(N) The center point", "(Adj) In between two extremes"],
"midnight": ["(N) 12 o’clock at night", "(N) The middle of the night"],
"might": ["(N) Strength or power", "(V) Expressing possibility"],
"mild": ["(Adj) Gentle or moderate", "(Adj) Not spicy or harsh"],
"mile": ["(N) A unit of distance", "(N) A long distance (figurative)"],
"military": ["(Adj) Relating to armed forces", "(N) The armed services"],
"milk": ["(N) A white liquid from mammals", "(V) To exploit for profit"],
"mill": ["(N) A building for grinding grain", "(V) To grind or process"],
"million": ["(N) The number 1,000,000", "(N) A very large amount"],
"mimic": ["(V) To imitate closely", "(N) A person who imitates"],
"mind": ["(N) The faculty of thought", "(V) To pay attention to"],
"mine": ["(Pron) Belonging to me", "(N) A place where minerals are extracted"],
"mineral": ["(N) A natural inorganic substance", "(N) A nutrient needed by the body"],
"mingle": ["(V) To mix or socialize", "(V) To blend together"],
"miniature": ["(Adj) Very small", "(N) A small-scale model"],
"minimum": ["(N) The least amount", "(Adj) As small as possible"],
"minister": ["(N) A government official", "(N) A clergy member"],
"minor": ["(Adj) Less important", "(N) A person under legal age"],
"mint": ["(N) A place where money is made", "(N) A fragrant herb"],
"minute": ["(N) A unit of time", "(Adj) Extremely small"],
"miracle": ["(N) A wondrous event", "(N) Something extraordinary"],
"mirror": ["(N) A reflective surface", "(V) To reflect or imitate"],
"mirth": ["(N) Amusement or laughter", "(N) Cheerfulness"],
"misery": ["(N) Great suffering", "(N) A cause of distress"],
"miss": ["(V) To fail to hit or reach", "(N) A title for an unmarried woman"],
"mission": ["(N) A special task", "(N) A religious or diplomatic assignment"],
"mist": ["(N) A fine spray of water", "(V) To cover with moisture"],
"mistake": ["(N) An error", "(V) To misunderstand"],
"mister": ["(N) A title for a man", "(N) A polite form of address"],
"mix": ["(V) To combine substances", "(N) A blend or mixture"],
"moan": ["(V) To make a low sound of pain", "(N) A complaint or groan"],
"moat": ["(N) A deep, wide ditch", "(N) A defensive trench around a castle"],
"mob": ["(N) A disorderly crowd", "(V) To crowd around"],
"mobile": ["(Adj) Able to move", "(N) A portable phone"],
"mock": ["(V) To ridicule", "(Adj) Imitation or fake"],
"mode": ["(N) A manner or style", "(N) A statistical value"],
"model": ["(N) A representation or example", "(V) To pose for artists"],
"moderate": ["(Adj) Not extreme", "(V) To regulate or guide"],
"modern": ["(Adj) Contemporary or current", "(Adj) Up-to-date"],
"modest": ["(Adj) Humble or unassuming", "(Adj) Moderate in size"],
"modify": ["(V) To change slightly", "(V) To alter or adjust"],
"moist": ["(Adj) Slightly wet", "(Adj) Damp or humid"],
"mold": ["(N) A fungus that grows on food", "(V) To shape or form"],
"mole": ["(N) A small burrowing mammal", "(N) A dark skin spot"],
"moment": ["(N) A brief period of time", "(N) Importance or significance"],
"money": ["(N) Currency used for exchange", "(N) Wealth or funds"],
"monitor": ["(N) A screen or observer", "(V) To watch closely"],
"monk": ["(N) A member of a religious order", "(N) A man devoted to monastic life"],
"monkey": ["(N) A primate with a tail", "(V) To play or fool around"],
"month": ["(N) One-twelfth of a year", "(N) A period of about 30 days"],
"mood": ["(N) A temporary state of mind", "(N) A distinctive atmosphere"],
"moon": ["(N) Earth’s natural satellite", "(V) To expose one’s buttocks (slang)"],
"moor": ["(N) Open uncultivated land", "(V) To secure a boat"],
"moral": ["(Adj) Concerned with right and wrong", "(N) A lesson from a story"],
"more": ["(Adj) Greater in amount", "(Adv) To a greater degree"],
"morning": ["(N) The early part of the day", "(N) The time before noon"],
"mortal": ["(Adj) Subject to death", "(N) A human being"],
"mortgage": ["(N) A loan for property", "(V) To pledge as security"],
"mosaic": ["(N) A picture made of small pieces", "(Adj) Varied or diverse"],
"mosquito": ["(N) A biting insect", "(N) A pest that feeds on blood"],
"most": ["(Adj) Greatest in amount", "(Adv) Extremely or very"],
"moth": ["(N) A nocturnal insect", "(N) A creature attracted to light"],
"mother": ["(N) A female parent", "(V) To care for lovingly"],
"motion": ["(N) Movement", "(V) To signal with a gesture"],
"motor": ["(N) A machine that produces motion", "(Adj) Related to movement"],
"mound": ["(N) A raised pile of earth", "(V) To heap up"],
"mount": ["(V) To climb or ascend", "(N) A horse or steed"],
"mountain": ["(N) A large natural elevation", "(N) A huge amount"],
"mourn": ["(V) To feel sorrow for a loss", "(V) To grieve"],
"mouse": ["(N) A small rodent", "(N) A computer pointing device"],
"mouth": ["(N) The opening of the face", "(V) To speak silently"],
"move": ["(V) To change position", "(N) An action or step"],
"movie": ["(N) A motion picture", "(N) A film shown in theaters"],
"much": ["(Adj) A large amount", "(Adv) To a great degree"],
"mud": ["(N) Wet, soft earth", "(V) To cover with mud"],
"muffin": ["(N) A small baked cake", "(N) A type of quick bread"],
"mug": ["(N) A drinking cup", "(V) To rob violently"],
"mulch": ["(N) Material spread on soil", "(V) To cover with mulch"],
"mule": ["(N) A hybrid animal (donkey × horse)", "(N) A stubborn person (informal)"],
"multiply": ["(V) To increase in number", "(V) To perform multiplication"],
"mumble": ["(V) To speak unclearly", "(N) A low, indistinct utterance"],
"mummy": ["(N) A preserved dead body", "(N) A mother (British informal)"],
"munch": ["(V) To chew loudly", "(N) A snack or bite"],
"mural": ["(N) A large wall painting", "(N) Artwork applied directly to a surface"],
"murder": ["(N) The unlawful killing of a person", "(V) To kill intentionally"],
"murmur": ["(N) A soft, indistinct sound", "(V) To speak quietly"],
"muscle": ["(N) Tissue that produces movement", "(V) To force one’s way"],
"museum": ["(N) A place displaying artifacts", "(N) An institution preserving history"],
"mushroom": ["(N) A fungus with a stem and cap", "(V) To grow rapidly"],
"music": ["(N) Organized sound", "(N) A form of artistic expression"],
"musical": ["(Adj) Related to music", "(N) A play with songs"],
"must": ["(V) To be required", "(N) Something essential"],
"mustard": ["(N) A spicy yellow condiment", "(N) A plant producing mustard seeds"],
"mute": ["(Adj) Silent or unable to speak", "(V) To soften or quiet"],
"mutter": ["(V) To speak in a low voice", "(N) A quiet complaint"],
"mutton": ["(N) Meat from a mature sheep", "(N) A sheep (archaic)"],
"mutual": ["(Adj) Shared by two or more", "(Adj) Reciprocal"],
"myriad": ["(N) A countless number", "(Adj) Innumerable"],
"myself": ["(Pron) The reflexive form of 'me'", "(Pron) Used for emphasis"],
"nab": ["(V) To seize or grab quickly", "(V) To arrest (informal)"],
"nag": ["(V) To annoy with repeated demands", "(N) A persistent complainer"],
"nail": ["(N) A thin metal fastener", "(V) To fasten or secure"],
"naive": ["(Adj) Lacking experience or sophistication", "(Adj) Innocently trusting"],
"naked": ["(Adj) Without clothing", "(Adj) Exposed or unprotected"],
"name": ["(N) A word by which someone is known", "(V) To identify or designate"],
"nap": ["(N) A short sleep", "(V) To sleep briefly"],
"napkin": ["(N) A cloth for wiping the mouth", "(N) A small table linen"],
"narrate": ["(V) To tell a story", "(V) To give a spoken account"],
"narrow": ["(Adj) Not wide", "(V) To limit or reduce"],
"nasty": ["(Adj) Unpleasant or offensive", "(Adj) Mean or spiteful"],
"nation": ["(N) A large group of people under one government", "(N) A country"],
"native": ["(Adj) Belonging to a place by birth", "(N) An original inhabitant"],
"natural": ["(Adj) Existing in nature", "(Adj) Not artificial or forced"],
"nature": ["(N) The physical world", "(N) A person's inherent qualities"],
"naughty": ["(Adj) Mischievous or disobedient", "(Adj) Improper or indecent"],
"naval": ["(Adj) Related to a navy", "(Adj) Pertaining to warships"],
"navel": ["(N) The belly button", "(N) The central point of something"],
"navigate": ["(V) To plan and follow a route", "(V) To find one’s way"],
"near": ["(Adj) Close in distance", "(Prep) Close to"],
"nearby": ["(Adj) Close at hand", "(Adv) Not far away"],
"nearly": ["(Adv) Almost", "(Adv) Very close to"],
"neat": ["(Adj) Clean and orderly", "(Adj) Simple and effective"],
"necessary": ["(Adj) Required or essential", "(N) Something needed"],
"neck": ["(N) The part connecting head and body", "(V) To kiss passionately (informal)"],
"need": ["(V) To require", "(N) A necessity or want"],
"needle": ["(N) A thin pointed tool", "(V) To provoke or annoy"],
"neglect": ["(V) To fail to care for", "(N) Lack of attention"],
"negotiate": ["(V) To discuss terms", "(V) To overcome or navigate"],
"neighbor": ["(N) A person living nearby", "(N) Someone close in relation or position"],
"neither": ["(Det) Not one nor the other", "(Adv) Similarly not"],
"nephew": ["(N) The son of one’s sibling", "(N) A male relative"],
"nerve": ["(N) A fiber transmitting signals", "(N) Courage or boldness"],
"nervous": ["(Adj) Anxious or uneasy", "(Adj) Easily agitated"],
"nest": ["(N) A bird’s home", "(V) To settle comfortably"],
"net": ["(N) A mesh fabric", "(V) To earn or gain after deductions"],
"network": ["(N) A connected system", "(V) To interact socially for advantage"],
"neutral": ["(Adj) Not taking sides", "(Adj) Without strong color or charge"],
"never": ["(Adv) At no time", "(Adv) Not ever"],
"new": ["(Adj) Recently created", "(Adj) Unfamiliar or fresh"],
"news": ["(N) Information about recent events", "(N) A broadcast or report"],
"next": ["(Adj) Immediately following", "(Adv) After this"],
"nice": ["(Adj) Pleasant or agreeable", "(Adj) Kind or considerate"],
"nick": ["(N) A small cut or notch", "(V) To steal (informal)"],
"nickname": ["(N) A familiar or humorous name", "(V) To give such a name"],
"niece": ["(N) The daughter of one’s sibling", "(N) A female relative"],
"night": ["(N) The period of darkness", "(N) An evening event"],
"nightmare": ["(N) A frightening dream", "(N) A terrible situation"],
"nimble": ["(Adj) Quick and light in movement", "(Adj) Mentally quick"],
"nine": ["(N) The number 9", "(Adj) One more than eight"],
"nineteen": ["(N) The number 19", "(Adj) One more than eighteen"],
"ninety": ["(N) The number 90", "(Adj) Nine tens"],
"ninth": ["(Adj) In the position after eighth", "(N) One of nine equal parts"],
"nip": ["(V) To pinch sharply", "(N) A small sip of alcohol"],
"nit": ["(N) A louse egg", "(N) A foolish person (informal)"],
"noble": ["(Adj) Having high moral qualities", "(N) A person of high rank"],
"nobody": ["(Pron) No person", "(N) A person of no importance"],
"nod": ["(V) To move the head up and down", "(N) A gesture of agreement"],
"noise": ["(N) Unwanted sound", "(N) A disturbance or commotion"],
"nomad": ["(N) A wanderer", "(N) A member of a roaming group"],
"none": ["(Pron) Not any", "(Adv) Not at all"],
"noodle": ["(N) A strip of pasta", "(N) The head or brain (slang)"],
"noon": ["(N) 12 o’clock midday", "(N) The middle of the day"],
"nor": ["(Conj) And not", "(Conj) Used after neither"],
"normal": ["(Adj) Usual or typical", "(N) A standard or pattern"],
"north": ["(N) A cardinal direction", "(Adj) Situated toward the north"],
"nose": ["(N) The organ of smell", "(V) To search or pry"],
"nostril": ["(N) One of the openings of the nose", "(N) A nasal passage"],
"not": ["(Adv) Expressing negation", "(Adv) Used to form a negative"],
"note": ["(N) A brief written message", "(V) To observe or remark"],
"nothing": ["(N) No thing", "(N) Something of no importance"],
"notice": ["(N) A written announcement", "(V) To observe or become aware"],
"notify": ["(V) To inform officially", "(V) To give notice"],
"notion": ["(N) An idea or belief", "(N) A whimsical impulse"],
"novel": ["(N) A long fictional story", "(Adj) New or unusual"],
"novice": ["(N) A beginner", "(N) Someone inexperienced"],
"now": ["(Adv) At the present time", "(Conj) Since or because (archaic)"],
"nowhere": ["(Adv) In no place", "(N) A nonexistent or insignificant place"],
"nuclear": ["(Adj) Relating to atomic energy", "(Adj) Relating to the nucleus of a cell"],
"nude": ["(Adj) Without clothing", "(N) A naked figure in art"],
"nudge": ["(V) To push gently", "(N) A slight push"],
"nuisance": ["(N) Something annoying", "(N) A bothersome person"],
"number": ["(N) A mathematical value", "(V) To count or assign numbers"],
"numb": ["(Adj) Without feeling", "(V) To make insensitive"],
"numerous": ["(Adj) Many", "(Adj) Existing in large numbers"],
"nurse": ["(N) A person who cares for the sick", "(V) To tend or care for"],
"nursery": ["(N) A room for babies", "(N) A place where plants are grown"],
"nut": ["(N) A hard-shelled seed", "(N) A crazy person (slang)"],
"nutmeg": ["(N) A spice from a tropical seed", "(N) A trick in sports (ball through legs)"],
"nutrient": ["(N) A substance that nourishes", "(Adj) Providing nourishment"],
"nutshell": ["(N) The shell of a nut", "(N) A brief summary"],
"oak": ["(N) A strong hardwood tree", "(N) The wood from such a tree"],
"oar": ["(N) A paddle for rowing", "(V) To row a boat"],
"oath": ["(N) A solemn promise", "(N) A sworn declaration"],
"oat": ["(N) A cereal grain", "(N) A plant producing edible seeds"],
"oatmeal": ["(N) Ground oats used as food", "(N) A porridge made from oats"],
"obedient": ["(Adj) Willing to obey", "(Adj) Dutiful and compliant"],
"obey": ["(V) To follow commands", "(V) To comply with rules"],
"object": ["(N) A physical thing", "(V) To express opposition"],
"oblige": ["(V) To do a favor for", "(V) To require or compel"],
"obscure": ["(Adj) Not well known", "(V) To hide or make unclear"],
"observe": ["(V) To watch carefully", "(V) To comment or remark"],
"obtain": ["(V) To get or acquire", "(V) To succeed in gaining"],
"obvious": ["(Adj) Easily seen or understood", "(Adj) Clear or apparent"],
"occasion": ["(N) A special event", "(N) A particular time"],
"occupy": ["(V) To take up space", "(V) To reside in or control"],
"occur": ["(V) To happen", "(V) To come to mind"],
"ocean": ["(N) A vast body of salt water", "(N) A large expanse of something"],
"octagon": ["(N) An eight-sided shape", "(N) A figure with eight angles"],
"october": ["(N) The tenth month of the year", "(N) A period associated with autumn"],
"odd": ["(Adj) Strange or unusual", "(Adj) Not divisible by two"],
"odds": ["(N) The likelihood of something", "(N) A disagreement or difference"],
"ode": ["(N) A lyrical poem", "(N) A poem expressing strong emotion"],
"odor": ["(N) A smell", "(N) A distinctive scent"],
"off": ["(Adv) Away from", "(Adj) Not operating or functioning"],
"offend": ["(V) To cause displeasure", "(V) To break a rule or law"],
"offer": ["(V) To present for acceptance", "(N) A proposal or bid"],
"office": ["(N) A place of business", "(N) A position of authority"],
"officer": ["(N) A person in authority", "(N) A member of the police or military"],
"official": ["(Adj) Authorized or formal", "(N) A person holding public office"],
"often": ["(Adv) Frequently", "(Adv) Many times"],
"oil": ["(N) A viscous liquid used as fuel or lubricant", "(V) To lubricate"],
"ointment": ["(N) A medicinal cream", "(N) A soothing salve"],
"old": ["(Adj) Having lived a long time", "(Adj) Former or previous"],
"olive": ["(N) A small green or black fruit", "(N) A tree producing olives"],
"omen": ["(N) A sign of future events", "(N) A prophetic indication"],
"omit": ["(V) To leave out", "(V) To fail to include"],
"once": ["(Adv) One time", "(Conj) As soon as"],
"one": ["(N) The number 1", "(Adj) Single or unique"],
"onion": ["(N) A layered vegetable", "(N) A plant with a pungent bulb"],
"only": ["(Adj) Sole or exclusive", "(Adv) No more than"],
"onto": ["(Prep) Moving to a surface", "(Prep) Becoming aware of"],
"ooze": ["(V) To seep slowly", "(N) A thick, sticky fluid"],
"open": ["(Adj) Not closed", "(V) To make accessible"],
"opera": ["(N) A dramatic musical work", "(N) A theater for such performances"],
"operate": ["(V) To function or work", "(V) To perform surgery"],
"opinion": ["(N) A personal belief", "(N) A judgment not based on fact alone"],
"oppose": ["(V) To resist or fight against", "(V) To be in conflict with"],
"opposite": ["(Adj) Completely different", "(N) A contrary position"],
"option": ["(N) A choice", "(N) Something available as an alternative"],
"orange": ["(N) A citrus fruit", "(Adj) The color between red and yellow"],
"orbit": ["(N) A curved path around a body", "(V) To travel in a circular path"],
"orchard": ["(N) A grove of fruit trees", "(N) A cultivated area for fruit"],
"order": ["(N) A command or arrangement", "(V) To request or arrange"],
"ordinary": ["(Adj) Common or usual", "(Adj) Not special or distinctive"],
"organ": ["(N) A body part with a function", "(N) A large musical instrument"],
"organize": ["(V) To arrange systematically", "(V) To coordinate activities"],
"origin": ["(N) The beginning or source", "(N) A person's ancestry"],
"ornament": ["(N) A decorative object", "(V) To decorate"],
"orphan": ["(N) A child without parents", "(V) To deprive of parents"],
"ostrich": ["(N) A large flightless bird", "(N) A person avoiding reality (figurative)"],
"other": ["(Adj) Different or additional", "(Pron) The second of two"],
"ought": ["(V) Used to express duty", "(V) Indicating advisability"],
"ounce": ["(N) A unit of weight", "(N) A very small amount"],
"our": ["(Det) Belonging to us", "(Det) Shared by a group"],
"ourselves": ["(Pron) The reflexive form of 'us'", "(Pron) Used for emphasis"],
"out": ["(Adv) Away from inside", "(Adj) Not fashionable or available"],
"outcome": ["(N) A result", "(N) A final consequence"],
"outdoor": ["(Adj) Outside", "(Adj) Suitable for outside use"],
"outer": ["(Adj) On the outside", "(Adj) Further from the center"],
"outfit": ["(N) A set of clothes", "(V) To provide equipment"],
"outgoing": ["(Adj) Sociable and friendly", "(Adj) Leaving or departing"],
"outline": ["(N) A general description", "(V) To summarize"],
"outlook": ["(N) A point of view", "(N) A forecast or expectation"],
"output": ["(N) Production or result", "(V) To produce or deliver"],
"outside": ["(Prep) Not within", "(N) The external part"],
"outstanding": ["(Adj) Excellent", "(Adj) Not yet resolved"],
"oval": ["(Adj) Egg-shaped", "(N) An elongated circle"],
"oven": ["(N) A chamber for baking", "(N) A heated compartment"],
"over": ["(Prep) Above or across", "(Adv) Finished or ended"],
"overall": ["(Adj) Including everything", "(N) A protective garment"],
"overcome": ["(V) To defeat or conquer", "(V) To overwhelm emotionally"],
"overdo": ["(V) To do too much", "(V) To exaggerate"],
"overeat": ["(V) To eat too much", "(V) To indulge excessively in food"],
"overflow": ["(V) To spill over", "(N) Excess beyond capacity"],
"overhear": ["(V) To hear unintentionally", "(V) To catch part of a conversation"],
"overlap": ["(V) To extend over part of something", "(N) A shared area"],
"overlook": ["(V) To fail to notice", "(V) To have a view from above"],
"overnight": ["(Adv) During the night", "(Adj) Sudden or immediate"],
"overtake": ["(V) To catch up and pass", "(V) To come upon suddenly"],
"owe": ["(V) To be in debt", "(V) To feel obligated"],
"owl": ["(N) A nocturnal bird", "(N) A symbol of wisdom"],
"own": ["(V) To possess", "(Adj) Belonging to oneself"],
"owner": ["(N) A person who possesses something", "(N) A proprietor"],
"ox": ["(N) A large domesticated bovine", "(N) A castrated bull used for work"],
"pace": ["(N) A step or speed of movement", "(V) To walk back and forth"],
"pack": ["(N) A bundle or group", "(V) To fill tightly"],
"package": ["(N) A wrapped parcel", "(V) To prepare for shipping"],
"pad": ["(N) A cushion or soft support", "(V) To fill or stuff"],
"paddle": ["(N) A tool for rowing", "(V) To move through water with a paddle"],
"page": ["(N) One side of a sheet of paper", "(V) To call someone over a speaker"],
"pail": ["(N) A bucket", "(N) A container for carrying liquids"],
"pain": ["(N) Physical or emotional suffering", "(V) To cause distress"],
"paint": ["(N) A colored liquid for coating surfaces", "(V) To apply paint"],
"pair": ["(N) Two of something", "(V) To join two things together"],
"pal": ["(N) A friend", "(V) To associate closely"],
"palace": ["(N) A grand residence", "(N) A home of royalty"],
"pale": ["(Adj) Light in color", "(V) To become faint or dim"],
"palm": ["(N) The inner surface of the hand", "(N) A tropical tree"],
"pan": ["(N) A shallow cooking container", "(V) To criticize harshly"],
"pancake": ["(N) A flat, round breakfast food", "(N) A makeup powder (informal)"],
"pane": ["(N) A sheet of glass", "(N) A section of a window"],
"panel": ["(N) A flat board or surface", "(N) A group of people for discussion"],
"panic": ["(N) Sudden fear", "(V) To become extremely frightened"],
"panther": ["(N) A large wild cat", "(N) A black leopard or jaguar"],
"pant": ["(V) To breathe quickly", "(N) A short, quick breath"],
"paper": ["(N) A thin material for writing", "(N) A written report"],
"parade": ["(N) A public procession", "(V) To march in display"],
"paradise": ["(N) A perfect place", "(N) Heaven or bliss"],
"paragraph": ["(N) A section of writing", "(V) To divide into paragraphs"],
"parallel": ["(Adj) Side by side and never meeting", "(N) A similarity"],
"parcel": ["(N) A package", "(V) To divide into parts"],
"pardon": ["(N) Forgiveness", "(V) To excuse or forgive"],
"parent": ["(N) A father or mother", "(V) To raise or care for a child"],
"park": ["(N) A public green area", "(V) To leave a vehicle in a place"],
"parrot": ["(N) A colorful bird", "(V) To repeat without understanding"],
"part": ["(N) A portion of a whole", "(V) To separate or divide"],
"particle": ["(N) A tiny piece", "(N) A very small amount"],
"partner": ["(N) A companion or associate", "(V) To join with someone"],
"party": ["(N) A social gathering", "(N) A political group"],
"pass": ["(V) To move by or go through", "(N) A permit or ticket"],
"passage": ["(N) A corridor or route", "(N) A portion of text"],
"passenger": ["(N) A person traveling in a vehicle", "(N) Someone not driving"],
"passion": ["(N) Strong emotion", "(N) Intense enthusiasm"],
"past": ["(N) A previous time", "(Adj) Gone by or earlier"],
"paste": ["(N) A thick, soft substance", "(V) To stick things together"],
"pasture": ["(N) Grassland for grazing animals", "(V) To feed animals on grass"],
"pat": ["(V) To tap lightly", "(N) A gentle touch"],
"patch": ["(N) A small piece used to cover something", "(V) To repair by covering"],
"path": ["(N) A track or route", "(N) A course of action"],
"patience": ["(N) The ability to wait calmly", "(N) Tolerance of delay"],
"patient": ["(N) A person receiving medical care", "(Adj) Able to wait calmly"],
"patrol": ["(V) To guard an area", "(N) A group assigned to watch"],
"pattern": ["(N) A repeated design", "(N) A model or example"],
"pause": ["(V) To stop briefly", "(N) A temporary stop"],
"pave": ["(V) To cover with a hard surface", "(V) To prepare the way for"],
"paw": ["(N) An animal’s foot", "(V) To scrape or handle clumsily"],
"pay": ["(V) To give money for goods or services", "(N) Wages or salary"],
"payment": ["(N) Money given for something", "(N) A financial obligation"],
"pea": ["(N) A small green vegetable", "(N) The plant that produces peas"],
"peace": ["(N) Freedom from conflict", "(N) Calm or tranquility"],
"peach": ["(N) A soft, sweet fruit", "(N) A lovely person (informal)"],
"peak": ["(N) The top of a mountain", "(V) To reach the highest point"],
"pearl": ["(N) A smooth, round gem", "(N) Something precious"],
"peasant": ["(N) A poor farmer", "(N) A rural laborer"],
"peck": ["(V) To strike with a beak", "(N) A quick, light kiss"],
"peculiar": ["(Adj) Strange or unusual", "(Adj) Unique to something"],
"pedal": ["(N) A foot lever", "(V) To operate with the feet"],
"peel": ["(V) To remove the outer layer", "(N) The skin of a fruit"],
"peep": ["(V) To look quickly or secretly", "(N) A faint sound"],
"peer": ["(V) To look closely", "(N) A person of equal rank"],
"pen": ["(N) A writing instrument", "(N) An enclosure for animals"],
"penalty": ["(N) A punishment", "(N) A disadvantage or cost"],
"pencil": ["(N) A writing tool with graphite", "(V) To write lightly"],
"pendulum": ["(N) A swinging weight", "(N) Something that moves back and forth"],
"penguin": ["(N) A flightless bird", "(N) A black-and-white seabird"],
"peninsula": ["(N) Land surrounded by water on three sides", "(N) A narrow land extension"],
"penny": ["(N) A coin worth one cent", "(N) A very small amount"],
"people": ["(N) Human beings", "(V) To populate"],
"pepper": ["(N) A spicy seasoning", "(V) To sprinkle or hit repeatedly"],
"perceive": ["(V) To become aware of", "(V) To interpret or understand"],
"perfect": ["(Adj) Without flaws", "(V) To improve to completion"],
"perform": ["(V) To carry out an action", "(V) To entertain an audience"],
"perhaps": ["(Adv) Possibly", "(Adv) By chance"],
"peril": ["(N) Danger", "(V) To expose to risk"],
"period": ["(N) A length of time", "(N) A punctuation mark"],
"permit": ["(V) To allow", "(N) An official document of permission"],
"perplex": ["(V) To confuse", "(V) To puzzle deeply"],
"persist": ["(V) To continue firmly", "(V) To endure over time"],
"person": ["(N) A human being", "(N) An individual identity"],
"persuade": ["(V) To convince", "(V) To influence by argument"],
"pest": ["(N) An annoying creature", "(N) A troublesome person"],
"pet": ["(N) A domesticated animal", "(V) To stroke affectionately"],
"petition": ["(N) A formal request", "(V) To ask earnestly"],
"petty": ["(Adj) Small or trivial", "(Adj) Narrow-minded"],
"phase": ["(N) A stage in a process", "(V) To carry out gradually"],
"pheasant": ["(N) A colorful game bird", "(N) A bird hunted for sport"],
"phenomenon": ["(N) An observable event", "(N) Something extraordinary"],
"philosophy": ["(N) The study of knowledge and existence", "(N) A guiding principle"],
"phone": ["(N) A device for communication", "(V) To call someone"],
"photo": ["(N) A photograph", "(V) To take a picture"],
"phrase": ["(N) A small group of words", "(V) To express in words"],
"physical": ["(Adj) Related to the body", "(N) A medical examination"],
"piano": ["(N) A musical instrument", "(Adj) Softly, in music"],
"pick": ["(V) To choose or select", "(N) A tool for digging"],
"pickle": ["(N) A preserved cucumber", "(N) A difficult situation (informal)"],
"picture": ["(N) An image or photograph", "(V) To imagine"],
"pie": ["(N) A baked dish with crust", "(N) A whole divided into parts"],
"piece": ["(N) A part of something", "(V) To assemble from parts"],
"pier": ["(N) A structure extending into water", "(N) A support for a bridge"],
"pierce": ["(V) To penetrate", "(V) To make a hole in"],
"pig": ["(N) A farm animal", "(V) To eat greedily (informal)"],
"pigeon": ["(N) A common city bird", "(N) A gullible person (slang)"],
"pile": ["(N) A heap of things", "(V) To stack up"],
"pill": ["(N) A small medicinal tablet", "(N) A boring person (informal)"],
"pillar": ["(N) A supporting column", "(N) A key figure in a group"],
"pillow": ["(N) A cushion for the head", "(V) To rest on a soft surface"],
"pilot": ["(N) A person who flies aircraft", "(V) To guide or steer"],
"pin": ["(N) A small metal fastener", "(V) To attach or hold in place"],
"pinch": ["(V) To squeeze tightly", "(N) A small amount"],
"pine": ["(N) A type of evergreen tree", "(V) To long for something"],
"pink": ["(Adj) A pale red color", "(N) A shade of red"],
"pint": ["(N) A unit of liquid measure", "(N) A glass of beer (informal)"],
"pipe": ["(N) A tube for conveying fluids", "(V) To convey through pipes"],
"pirate": ["(N) A sea robber", "(V) To illegally copy"],
"pistol": ["(N) A small firearm", "(N) A lively or spirited person (informal)"],
"pit": ["(N) A large hole", "(V) To set in competition"],
"pitch": ["(N) The level of sound", "(N) A throw in sports"],
"pity": ["(N) Sympathy for suffering", "(V) To feel compassion"],
"place": ["(N) A location", "(V) To put in a position"],
"plague": ["(N) A widespread disease", "(V) To trouble or annoy"],
"plain": ["(Adj) Simple or clear", "(N) A flat expanse of land"],
"plan": ["(N) A detailed proposal", "(V) To arrange in advance"],
"plane": ["(N) A flat surface", "(N) An aircraft"],
"planet": ["(N) A celestial body orbiting a star", "(N) Earth itself"],
"plant": ["(N) A living organism that grows in soil", "(V) To place in the ground"],
"plaster": ["(N) A material for coating walls", "(V) To cover thickly"],
"plate": ["(N) A flat dish", "(V) To coat with metal"],
"platform": ["(N) A raised surface", "(N) A political or software base"],
"play": ["(V) To engage in activity for enjoyment", "(N) A dramatic performance"],
"plea": ["(N) A request or appeal", "(N) A defendant’s answer in court"],
"plead": ["(V) To beg or implore", "(V) To argue a case"],
"pleasant": ["(Adj) Enjoyable or agreeable", "(Adj) Friendly or polite"],
"please": ["(V) To satisfy or delight", "(Interj) A polite request"],
"pledge": ["(N) A solemn promise", "(V) To commit or promise"],
"plenty": ["(N) A large amount", "(Adv) More than enough"],
"plight": ["(N) A difficult situation", "(V) To pledge (archaic)"],
"plot": ["(N) A secret plan", "(N) The storyline of a narrative"],
"plow": ["(N) A farm tool for turning soil", "(V) To dig or move forcefully"],
"pluck": ["(V) To pull off or out", "(N) Courage or determination"],
"plug": ["(N) A stopper or connector", "(V) To block or fill"],
"plum": ["(N) A sweet fruit", "(Adj) Highly desirable"],
"plumber": ["(N) A person who repairs pipes", "(N) A specialist in water systems"],
"plunge": ["(V) To dive or fall suddenly", "(N) A sudden drop"],
"plural": ["(Adj) More than one", "(N) A grammatical form"],
"plus": ["(Prep) Added to", "(N) A positive quantity"],
"pocket": ["(N) A small pouch in clothing", "(V) To take secretly"],
"poem": ["(N) A piece of writing in verse", "(N) A composition expressing emotion"],
"poet": ["(N) A writer of poems", "(N) A person with creative expression"],
"point": ["(N) A sharp end or idea", "(V) To indicate direction"],
"poison": ["(N) A harmful substance", "(V) To contaminate"],
"poke": ["(V) To jab or prod", "(N) A push or nudge"],
"pole": ["(N) A long, slender rod", "(N) Either end of Earth’s axis"],
"police": ["(N) Law enforcement officers", "(V) To maintain order"],
"polish": ["(V) To make smooth or shiny", "(N) A substance for shining"],
"polite": ["(Adj) Courteous and respectful", "(Adj) Showing good manners"],
"politics": ["(N) Governmental affairs", "(N) Strategies for gaining power"],
"pond": ["(N) A small body of water", "(N) A still pool"],
"ponder": ["(V) To think deeply", "(V) To consider carefully"],
"pony": ["(N) A small horse", "(V) To pay (slang: pony up)"],
"pool": ["(N) A small body of water", "(N) A game played with cues"],
"poor": ["(Adj) Lacking money", "(Adj) Of low quality"],
"pop": ["(V) To make a quick, sharp sound", "(N) A carbonated drink"],
"pope": ["(N) The head of the Roman Catholic Church", "(N) A leader of great authority"],
"popular": ["(Adj) Liked by many", "(Adj) Common or widespread"],
"population": ["(N) The number of people in an area", "(N) A group of organisms"],
"porch": ["(N) A covered entrance", "(N) A veranda"],
"pork": ["(N) Meat from a pig", "(N) Government spending for local projects (informal)"],
"port": ["(N) A harbor for ships", "(N) The left side of a ship"],
"portion": ["(N) A part of something", "(V) To divide into shares"],
"portrait": ["(N) A picture of a person", "(N) A detailed description"],
"pose": ["(V) To assume a position", "(N) A posture or attitude"],
"position": ["(N) A place or location", "(N) A job or role"],
"positive": ["(Adj) Confident or optimistic", "(Adj) Greater than zero"],
"possess": ["(V) To own or control", "(V) To dominate mentally"],
"possible": ["(Adj) Able to happen", "(N) Something that may occur"],
"post": ["(N) A vertical support", "(N) Mail or a message"],
"postpone": ["(V) To delay", "(V) To put off until later"],
"pot": ["(N) A container for cooking", "(N) Marijuana (slang)"],
"potato": ["(N) A starchy vegetable", "(N) A tuber used as food"],
"pottery": ["(N) Objects made of clay", "(N) The craft of making ceramics"],
"pouch": ["(N) A small bag", "(N) A pocket-like space"],
"pound": ["(N) A unit of weight", "(V) To hit repeatedly"],
"pour": ["(V) To cause liquid to flow", "(V) To rain heavily"],
"poverty": ["(N) The state of being poor", "(N) Lack of resources"],
"powder": ["(N) Fine dry particles", "(V) To apply powder"],
"power": ["(N) The ability to act or influence", "(V) To supply with energy"],
"practical": ["(Adj) Useful and realistic", "(Adj) Concerned with action"],
"practically": ["(Adv) in a realistic or sensible manner", "(Adv) almost or nearly"],
"practice": ["(N) the act of doing something repeatedly to improve skill", "(V) to perform an activity regularly"],
"practiced": ["(Adj) skilled from repeated experience", "(Adj) done habitually"],
"practitioner": ["(N) a person actively engaged in a profession or activity"],
"pragmatic": ["(Adj) dealing with matters in a practical, realistic way"],
"pragmatism": ["(N) a practical approach to problems and affairs", "(N) the belief in focusing on results rather than theories"],
"pragmatist": ["(N) a person who deals with matters sensibly and realistically"],
"pragmatically": ["(Adv) in a practical or realistic manner"],
"prairie": ["(N) a large open area of grassland"],
"praise": ["(N) expression of approval or admiration", "(V) to express warm approval or admiration"],
"praiseworthy": ["(Adj) deserving approval or admiration"],
"praline": ["(N) a sweet confection made of nuts and sugar"],
"pram": ["(N) a baby carriage"],
"prance": ["(V) to move with high, springy steps", "(N) a lively, showy movement"],
"prank": ["(N) a playful trick or joke", "(V) to play a mischievous trick"],
"prankish": ["(Adj) inclined to play tricks", "(Adj) mischievously playful"],
"prankster": ["(N) a person who plays practical jokes"],
"pranky": ["(Adj) full of playful mischief"],
"prate": ["(V) to talk foolishly or at length"],
"prattle": ["(V) to speak in a childish or foolish way", "(N) trivial or childish talk"],
"prawn": ["(N) a small marine crustacean used as food"],
"pray": ["(V) to speak to a deity", "(V) to make an earnest request"],
"prayer": ["(N) a solemn request or expression of thanks to a deity"],
"preach": ["(V) to deliver a religious sermon", "(V) to advocate strongly for an idea"],
"preacher": ["(N) a person who delivers sermons"],
"preachy": ["(Adj) inclined to moralize excessively"],
"preadult": ["(N) a person not yet fully grown"],
"preadvise": ["(V) to inform beforehand"],
"prearrange": ["(V) to organize in advance"],
"prebend": ["(N) a stipend given to a clergy member"],
"prebendary": ["(N) a clergy member receiving a prebend"],
"prebook": ["(V) to reserve in advance"],
"precarious": ["(Adj) unstable or insecure", "(Adj) dependent on uncertain conditions"],
"precast": ["(Adj) formed or shaped beforehand"],
"precaution": ["(N) a measure taken to prevent harm"],
"precede": ["(V) to come before in order or time"],
"precedent": ["(N) an earlier event serving as an example"],
"precept": ["(N) a general rule or principle"],
"precess": ["(V) to move or rotate slowly in a circular manner"],
"precinct": ["(N) a district or area within defined boundaries"],
"precious": ["(Adj) of great value", "(Adj) cherished or beloved"],
"precipice": ["(N) a very steep cliff"],
"precise": ["(Adj) exact and accurate"],
"precision": ["(N) the quality of being exact"],
"preclude": ["(V) to prevent or make impossible"],
"preclusion": ["(N) the act of preventing or hindering", "(N) a legal rule barring a claim"],
"precocious": ["(Adj) unusually advanced in development", "(Adj) showing early maturity"],
"precocity": ["(N) early development or maturity", "(N) advanced ability at a young age"],
"preconceive": ["(V) to form an opinion beforehand", "(V) to imagine in advance"],
"preconception": ["(N) an opinion formed before evidence", "(N) a preconceived idea"],
"precondition": ["(N) a requirement beforehand", "(V) to prepare in advance"],
"preconduct": ["(V) to guide or manage beforehand"],
"preconscious": ["(Adj) existing just below the level of awareness"],
"preconstruct": ["(V) to build or assemble in advance"],
"preconstruction": ["(N) the process of planning or building beforehand"],
"precook": ["(V) to cook partly or entirely before final preparation"],
"precool": ["(V) to cool something in advance"],
"precursor": ["(N) something that comes before", "(N) a forerunner or predecessor"],
"precursory": ["(Adj) serving as a precursor", "(Adj) preceding something important"],
"predate": ["(V) to come before in time", "(V) to assign an earlier date"],
"predation": ["(N) the act of preying on others", "(N) exploitation or plundering"],
"predator": ["(N) an animal that hunts others", "(N) one who exploits others"],
"predatory": ["(Adj) seeking to exploit or victimize", "(Adj) relating to hunting prey"],
"predecease": ["(V) to die before another person"],
"predecessor": ["(N) one who came before", "(N) a former holder of a position"],
"predefine": ["(V) to set or determine in advance"],
"predestine": ["(V) to determine beforehand", "(V) to foreordain"],
"predestined": ["(Adj) determined in advance", "(Adj) fated to occur"],
"predestination": ["(N) the belief that events are predetermined", "(N) fate or destiny"],
"predetermine": ["(V) to decide in advance", "(V) to influence beforehand"],
"predetermined": ["(Adj) decided ahead of time", "(Adj) fixed or set in advance"],
"predicable": ["(Adj) able to be stated or affirmed", "(Adj) capable of being predicted"],
"predicate": ["(V) to base or establish on something", "(N) the part of a sentence containing the verb"],
"predication": ["(N) the act of affirming or declaring", "(N) a statement or assertion"],
"predict": ["(V) to foretell or forecast", "(V) to state as likely to happen"],
"predictable": ["(Adj) easy to foresee", "(Adj) unsurprising in outcome"],
"prediction": ["(N) a forecast or prophecy", "(N) an anticipated outcome"],
"predictable":["(Adj) able to be known in advance", "(Adj) behaving in a way that is expected"],
"predicted":["(Adj) stated or made known in advance", "(V) past tense of predict"],
"predicting":["(V) declaring or telling in advance", "(V) acting as a forewarning"],
"prediction":["(N) a statement made about the future", "(N) the act of forecasting"],
"predicter":["(N) someone who makes a prediction"],
"prediction algorithms":["(N) automated procedures for forecasting"],
"prediction error":["(N) the difference between a forecasted value and actual outcome"],
"prediction model":["(N) a formula or system used to estimate future outcomes"],
"prediction results":["(N) the outcome of an attempt to forecast future events"],
"predilection":["(N) a preference or special liking for something", "(N) a bias in favor of something"],
"predispose":["(V) to make someone inclined to a specific attitude or action", "(V) to make someone susceptible to a disease"],
"predisposed":["(Adj) inclined toward something beforehand", "(Adj) susceptible to a condition"],
"predisposition":["(N) a liability or tendency to suffer from a particular condition", "(N) an inclination"],
"predominance":["(N) the state of being greater in number or intensity", "(N) superiority"],
"predominant":["(Adj) being the strongest or main element"],
"predominate":["(V) to be the main element", "(V) to have control or influence"],
"preeminent":["(Adj) surpassing all others", "(Adj) distinguished in a particular field"],
"preeminently":["(Adv) to a preeminent degree", "(Adv) outstandingly"],
"pre-eminentness":["(N) the quality of being preeminent", "(N) superiority"],
"pre-emphasis":["(N) the boost of certain frequencies", "(N) emphasis"],
"pre-emphasize":["(V) to enhance certain frequencies", "(V) to give prior focus"],
"pre-empt":["(V) to acquire in advance", "(V) to take for oneself"],
"pre-emptible":["(Adj) able to be taken or acquired beforehand"],
"pre-emption":["(N) the act of preempting", "(N) prior seizure"],
"pre-emptioner":["(N) one who preempts", "(N) a settler who has right of purchase"],
"preen":["(V) to tidy feathers with a beak", "(V) to dress oneself carefully"],
"preemie":["(N) a baby born prematurely"],
"preemptory":["(Adj) not allowing refusal", "(Adj) final"],
"preen":["(V) to clean with a beak", "(V) to take pride in one's appearance"],
"pre-existent":["(Adj) existing before something else", "(Adj) having prior existence"],
"prefactor":["(N) a factor that precedes", "(N) a multiplier placed before a variable"],
"prefatory":["(Adj) serving as an introduction", "(Adj) preliminary"],
"prefect":["(N) a chief officer", "(N) a student monitor"],
"prefecture":["(N) a district under a prefect", "(N) an administrative area"],
"prefer":["(V) to choose over another", "(V) to hold in higher regard"],
"preferable":["(Adj) more desirable", "(Adj) worthier"],
"preference":["(N) the act of preferring", "(N) a partiality for something"],
"preferential":["(Adj) showing preference", "(Adj) giving advantage"],
"preferment":["(N) promotion to a higher office", "(N) advancement"],
"prefigure":["(V) to represent beforehand", "(V) to foreshadow"],
"prefix":["(N) a morpheme added to the front", "(V) to add at the beginning"],
"preform":["(V) to form beforehand", "(N) a preliminary shape"],
"preglacial":["(Adj) existing before a glacial period"],
"preheat":["(V) to heat beforehand", "(V) to warm up oven"],
"prehensile":["(Adj) adapted for grasping", "(Adj) capable of seizing"],
"prehension":["(N) the act of grasping", "(N) seizing with the hand"],
"prehistoric":["(Adj) relating to time before written history"],
"preignition":["(N) premature ignition in an engine"],
"prejudge":["(V) to judge beforehand", "(V) to form a premature opinion"],
"prejudgment":["(N) a premature judgment", "(N) bias"],
"prejudice":["(N) preconceived opinion", "(V) to cause partiality"],
"prejudicial":["(Adj) harmful", "(Adj) biased"],
"prelacy":["(N) the office of a prelate", "(N) church government by bishops"],
"prelate":["(N) a high-ranking church official"],
"prelect":["(V) to lecture", "(V) to read a discourse"],
"prelection":["(N) a lecture", "(N) a discourse"],
"preliminary":["(Adj) preceding main action", "(N) an introductory act"],
"prelude":["(N) an introductory event", "(V) to serve as a prelude"],
"prelusive":["(Adj) serving as a prelude", "(Adj) introductory"],
"prelusively": ["(Adv) In a prelusive manner; preliminarily.", "(Adv) As a prelude."],
"prelusorily": ["(Adv) In a prelusory or introductory manner.", "(Adv) Preliminarily."],
"prelusory": ["(Adj) Introductory.", "(Adj) Prelusive; preparatory."],
"prem": ["(N) Premium.", "(N) Premise; abbreviation often used in context."],
"premade": ["(Adj) Produced beforehand.", "(Adj) Ready-made."],
"pre-main-sequence": ["(Adj) Referring to a star that has not yet reached the main sequence.", "(Adj) An early stage of stellar evolution."],
"pre-makeready": ["(N) The preliminary process of setting up machinery.", "(N) Preparation before a production run."],
"premalignancy": ["(N) A condition that can or is likely to become malignant.", "(N) Precancerous state."],
"pre-man": ["(N) An ancestor of modern human beings.", "(N) Hominid prior to Homo sapiens."],
"premandibular": ["(Adj) Located before the mandible.", "(Adj) Situated in front of the jaw."],
"premanufacture": ["(N) Activities taking place before manufacturing.", "(N) Development phase prior to production."],
"Premarin": ["(N) A conjugated estrogen medication.", "(N) Hormone replacement therapy brand."],
"premarital": ["(Adj) Existing or occurring before marriage.", "(Adj) Pre-wedding."],
"premaritally": ["(Adv) In a manner relating to the time before marriage."],
"premarket": ["(Adj) Before a product or service is released to the market.", "(Adj) Preliminary marketing phase."],
"premarketing": ["(N) Promotional activities before official launch.", "(N) Pre-launch planning."],
"premarriage": ["(N) The period before marriage.", "(N) Pre-nuptial phase."],
"premature": ["(Adj) Occurring before the expected time.", "(Adj) Too early; premature birth."],
"premature beat": ["(N) An extra heartbeat, a form of arrhythmia.", "(N) Premature contraction."],
"premature birth": ["(N) Birth that takes place more than three weeks before the baby’s estimated due date.", "(N) Preterm birth."],
"premature contraction": ["(N) A cardiac contraction happening earlier than expected.", "(N) Ectopic beat."],
"premature death": ["(N) Death that occurs earlier than the average age of death.", "(N) Early mortality."],
"prematurely": ["(Adv) Before the proper time.", "(Adv) Early."],
"premaxilla": ["(N) A bone in the upper jaw of many vertebrates.", "(N) Premaxillary bone."],
"premaxillae": ["(N) Plural form of premaxilla.", "(N) Paired bones of the upper jaw."],
"premaxillary": ["(Adj) Relating to the premaxilla.", "(Adj) Situated in front of the maxilla."],
"premeal": ["(Adj) Occurring or eaten before a meal.", "(Adj) Pre-prandial."],
"premeasure": ["(V) To measure beforehand.", "(V) To estimate size early."],
"premed": ["(N) A student preparing for medical school.", "(N) Premedical curriculum."],
"premedical": ["(Adj) Relating to studies or training before medical school.", "(Adj) Preparatory for medicine."],
"premedically": ["(Adv) In a manner relating to premedical training."],
"premedicate": ["(V) To administer medication before a medical procedure.", "(V) Pre-treat with drugs."],
"premedication": ["(N) Medication given before a procedure.", "(N) Pre-surgery sedative."],
"premedieval": ["(Adj) Occurring before the Middle Ages.", "(Adj) Before the medieval period."],
"premeditate": ["(V) To think out or plan beforehand.", "(V) To intend in advance."],
"premeditated": ["(Adj) Planned in advance.", "(Adj) Intentional (usually of a crime)."],
"premeditatedly": ["(Adv) In a manner that was planned beforehand."],
"premeditatingly": ["(Adv) In a premeditated manner; thoughtfully; with prior planning", "0"],
"premeditatively": ["(Adv) In a premeditative manner; with premeditation; studiedly", "0"],
"premeditation": ["(N) The act of planning or plotting a crime or action beforehand", "(N) A thought or consideration of a matter before acting upon it"],
"premier": ["(Adj) First in importance, order, or position; leading", "(N) A prime minister or head of government"],
"premiere": ["(N) The first performance or showing of a play, film, or musical work", "(V) To give the first performance of a work"],
"premise": ["(N) A previous statement from which another is inferred; a proposition", "(V) To base an argument, theory, or undertaking on a prior statement"],
"premiss": ["(N) A premise, particularly in logic", "0"],
"premium": ["(N) An amount to be paid for an insurance policy", "(Adj) Of superior quality and higher price"],
"premonition": ["(N) A strong feeling that something is about to happen, especially something unpleasant", "(N) A warning in advance; forewarning"],
"premonitory": ["(Adj) Serving to warn beforehand; indicating a future event", "0"],
"premeditatedness": "the quality or state of being premeditatedly planned",
"premeditately": "in a premeditated manner; with premeditation",
"premeditates": "[(V) thinks about and revolves in the mind beforehand, (V) schemes or plans beforehand]",
"premeditating": "[(V) thinking about beforehand, (V) engaging in premeditation]",
"premeditation": "[(N) an act or instance of premeditating, (N) consideration or planning of an act beforehand that shows intent]",
"premeditatively": "[(ADV) in a premeditative manner, (ADV) with premeditation]",
"premeeting": "[(N) a meeting held before a main meeting, (V) to meet before a scheduled time]",
"premeiotic": "[(ADJ) occurring before meiosis]",
"premelted": "[(ADJ) already melted before a particular process]",
"premelting": "[(V) melting something beforehand]",
"premetallic":["(Adj) existing or occurring before the age of metals" , "(Adj) before the development of metallurgy"],
"premetamorphosis":["(N) the stage before a major change in form" , "(N) before metamorphosis"],
"premetrical":["(Adj) before the use of the metric system" , "(Adj) relating to a period before standardized measurement"],
"premial":["(Adj) relating to a premium or reward" , "(Adj) pre-emptive"],
"premidnight":["(Adj) occurring before twelve o'clock at night" , "(Adv) in the evening hours"],
"postmidnight" : [ "(adj) Occurring after midnight", "(adj) After midnight, but before dawn" ],
"predawn" : [ "(adj) Before dawn", "(n) The period immediately preceding dawn" ],
"predaylight" : [ "(adj) Before daylight", "(adj) Before the sun rises" ],
"premorning" : [ "(adj) Before morning", "(n) The early hours before dawn" ],
"preafternoon" : [ "(adj) Before the afternoon", "(adj) Occurring in the morning" ],
"midnightish" : [ "(adj) Resembling midnight", "(adj) Near midnight" ],
"predaytime" : [ "(adj) Before daytime", "(adj) During the night" ],
"prebedtime" : [ "(adj) Before bedtime", "(n) The evening hours" ],
"prenoon" : [ "(adj) Before noon", "(n) The morning" ],
"postcurfew" : [ "(adj) After a curfew", "(n) The time after designated restrictions" ],
"predusk" : [ "(adj) Before dusk", "(n) The period before twilight" ],
"overnight" : [ "(adv) During or throughout the night", "(adj) Occurring between dusk and dawn", "(adj) Complete before the next morning" ],
"antelucan" : [ "(adj) Before dawn", "(adj) Occurring in the postmidnight period", "(adj) At night, especially of secret assemblies" ],
"matutine" : [ "(adj) Of or relating to early morning", "(adj) That rises before the sun, as a star" ],
"wee hours" : [ "(n) The very early morning", "(n) The time following midnight, when most are asleep" ],
"eleventh-hour" : [ "(adj) Just before it is too late", "(adj) Last-minute" ],
"vespertine" : [ "(adj) Of or related to the evening", "(adj) Occurring in the evening" ],
"preprandial" : [ "(adj) Occurring before a meal", "(adj) Before dinner" ],
"postprandial" : [ "(adj) After a meal", "(adj) Especially after dinner" ],
"postprandially": "In a postprandial manner; after a meal; especially, after dinner.",
"postprostration": "The state or period following a prostration.",
"post-production": [
"The final stage in a production process, such as film or television editing",
"Of or relating to this stage"
],
"postpubescent": "After the onset of puberty",
"postpubertal": "After puberty",
"postpustular": "Occurring after the formation of pustules",
"postpyretic": "Occurring after a fever",
"postquarantine": "Following the quarantine period",
"post-racial": "A theoretical period or society where racial prejudice and discrimination no longer exist",
"postradication": "The process of removing something after it has taken root",
"postradioactive": "Occurring after a radioactive event",
"postramus": "The part of a structure following a ramus",
"postraphaean": "Behind the raphe, used in diatom studies",
"postrarefaction": "Following a period of reduction in density",
"postrate": "Variant of prostrate, or a state of exhaustion following an action",
"postreaction": "A reaction that occurs following a specific stimulus or event",
"postrecession": "Occurring after a period of economic recession",
"postreduction": "Following a reduction in size, quantity, or volume",
"postreflex": "A reflex that occurs after a primary reflex",
"postrenal": "Situated behind or after the kidney",
"postreproductive": "The period following the end of reproductive capability",
"postresurrection": "Occurring after a resurrection",
"postrhinoplasty": "Following a nose reconstruction surgery",
"postrider": "A rider who carries mail, often used in historical contexts",
"post-roman": "After the end of the Roman empire",
"postrorse": "Directed backward, or behind the main axis",
"postruminal": "Occurring after the rumen in animals",
"postsacral": "Located behind or after the sacrum",
"postsanction": "Authorization given after an action",
"postscarlatinal": "Occurring after scarlet fever",
"postschool": "After school hours or finishing school",
"postscript": "A sentence or phrase added to the end of a letter, often abbreviated as P.S.",
"postsynaptic": "Relating to the neuron that receives a signal from the previous neuron",
"post-sync": [
"To add sound to a film after it has been shot",
"Pertaining to post-synchronization"
],
"post-synchronization": "The process of adding sound to a film after filming.",
"postsylvian": "Located behind the sylvian fissure (or fissure of Sylvius) in the brain.",
"postsynapsis": "The phase occurring directly after the pairing of homologous chromosomes (synapsis).",
"post-systolic": "Occurring after the contraction phase (systole) of the heart.",
"postsynaptic density": [
"A proteinaceous, electron-dense specialization attached to the postsynaptic membrane",
"A site containing neurotransmitter receptors, scaffold proteins, and signaling molecules"
],
"postsynaptic membrane": "The membrane of the neuron or cell that bears receptors for neurotransmitter released into the synaptic cleft.",
"postsynaptic potential": [
"A temporary change in the electric polarization of the membrane of a postsynaptic cell",
"Can be excitatory (depolarization) or inhibitory (hyperpolarization)"
],
"postsynaptic cell": "The neuron or gland cell that receives a chemical signal from a presynaptic cell.",
"post-synaptic receptor": "Receptor proteins located on the membrane of the postsynaptic terminal.",
"posttax": "Remaining after taxes are paid.",
"postteen": "Describing the period immediately following teenage years.",
"posttemporal": "Relating to the area behind the temporal bone.",
"posttertiary": "Of, relating to, or being the geological time after the Tertiary period.",
"posttest": ["A test taken after a learning experience or instructional period.", "A test given to students after they have completed a unit of study."],
"posttesting": "The act of administering a posttest.",
"post-tibial": "Situated behind the tibia.",
"post time": "The scheduled time for the start of a race.",
"Post Toasties": "A brand of corn flakes produced by Post Consumer Brands.",
"post-tonic": "Occurring after a stressed syllable.",
"post town": "A town assigned by the post office for handling mail.",
"post township": "A township designated for post-office services.",
"post-transcriptional": "Occurring after transcription (RNA processing).",
"post-translation": "Occurring after protein translation.",
"post-translational": "Occurring after translation; typically referring to modifications of a protein.",

"post-translationally": "In a manner occurring after protein translation.",
"post-transcription": "The processes that occur after RNA transcription, such as splicing or editing.",
"post-transcriptional": "Occurring or taking place after transcription of DNA to RNA.",
"post-trauma": "Existing or occurring after a traumatic incident.",
"post-traumatic": "Occurring after a physical or emotional injury.",
"post-traumatic stress disorder": ["A mental health condition triggered by a terrifying event", "Characterized by flashbacks, nightmares, and severe anxiety."],
"post-treatment": "Following the completion of a medical or industrial treatment.",
"post-truth": "Relating to a situation in which objective facts are less influential than appeals to emotion.",
"post-tussive": "Occurring after a cough, often used to describe physical changes.",
"potability": "The quality of being safe to drink.",
"potable": "Safe for drinking; drinkable.",
"potableness": "the quality of being drinkable or potable",
"potage": "a thick soup or porridge",
"potager": "a kitchen garden",
"potale": "a mixture of water and ground meal for feeding cattle",
"potamian": "related to rivers",
"potash": [
    "potassium carbonate or hydroxide",
    "a potassium compound used in agriculture or industry"
],
"potash muriate": "potassium chloride",
"potassium": "a silver-white soft light metallic element that occurs abundantly in nature especially combined in minerals",
"potation": "the act of drinking; a drink, especially an alcoholic one",
"potatory": "of, relating to, or given to drinking",
"potawatami": "variant of potawatomi",
"potawatomi": ["a member of an American Indian people originally from the area around Green Bay, Wisconsin", "the Algonquian language of the Potawatomi people"],
"potawatomis": "plural of potawatomi",
"potbank": "a pottery factory, especially one with bottle ovens",
"potbanks": "plural of potbank",
"potbellied": ["having a protuberant belly", "having a rounded body"],
"potbellies": "plural of potbelly",
"potbelly": ["a protuberant belly", "a stomach that sticks out"],
"potboil": "to work at a low-level, routine job, typically in writing or art",
"potboiled": "simple past tense and past participle of potboil",
"potboiler": ["a literary or artistic work produced quickly and solely for money", "a mediocre work"],
"potboilers": "plural of potboiler",
"potboiling": "present participle of potboil",
"potboils": "third-person singular simple present of potboil",
"potbound": "having roots restricted by the size of the container",
"potboy": "a boy or man who works in a tavern or public house, serving drinks",
"potboys": "plural of potboy",
"potch": "to break or smash, especially in pottery contexts",
"potched": "past tense of potch",
"potcher": "a machine used in papermaking to beat rags",
"potcherman": "a person who works with a potcher",
"potchers": "plural of potcher",
"potches": "plural of potch",
"potching": "present participle of potch",
"pote": "to push or poke (dialectal)",
"potecaries": "plural of potecary (archaic)",
"potecary": "apothecary (archaic)",
"poted": "past tense of pote",
"poteen": "an illicitly distilled Irish whiskey",
"poteens": "plural of poteen",
"potence": "potential; power or force (archaic)",
"potences": "plural of potence",
"potencies": "plural of potency",
"potency": ["the power or authority to influence", "the strength of a medicine", "the ability of a male to copulate"],
"potent": ["having great power, influence, or effect", "strong or effective", "capable of sexual intercourse"],
"potentate": ["a monarch or ruler", "a person with great power"],
"potentates": "plural of potentate",
"potentia": "potentiality or power (Latin phrase)",
"potential": ["possible, as opposed to actual", "capable of being or becoming", "a latent quality that may be developed"],
"potentialities": "plural of potentiality",
"potentiality": "the state of being potential",
"potentialize": "to make potential; to give potential",
"potentialized": "past tense of potentialize",
"potentializes": "third-person singular present of potentialize",
"potentializing": "present participle of potentialize",
"potentially": "with potential",
"potentialness": "the state of having potential",
"potentials": "plural of potential",
"potentias": "plural of potentia",
"potentiate": "to increase the power or effect of a drug",
"potentiated": "past tense of potentiate",
"potentiates": "third-person singular present of potentiate",
"potentiating": "present participle of potentiate",
"potentiation": "the interaction of two or more drugs such that the total effect is greater than the sum of the individual effects",
"potentiations": "plural of potentiation",
"potentiator": "a substance that increases the effectiveness of another substance",
"potentiators": "plural of potentiator",
"potentilla": "a plant of the rose family, often with yellow flowers",
"potentillas": "plural of potentilla",
"potlatch": [
    "a ceremonial feast among Northwest Coast Indians",
    "a party where guests receive gifts"
],
"potlatching": "the act of holding a potlatch",
"potline": "a series of electrolytic cells used in aluminum smelting",
"potlines": "plural of potline",
"potluck": "a meal where everyone brings a dish to share",
"potlucks": "plural of potluck",
"potpies": "plural of potpie",
"potshot": "a random or easy shot, often aimed without careful aim",
"potshots": "plural of potshot",
"potsies": "plural of potsy, a game",
"pottage": "a thick soup or stew",
"pottages": "plural of pottage",
"potteen": "alternative spelling of poteen",
"potteens": "plural of potteen",
"potter": [
    "a person who makes pottery",
    "to move or act aimlessly"
],
"pottered": "past tense of potter",
"potterer": "one who potters",
"potterers": "plural of potterer",
"potteries": "places where pottery is made",
"pottering": "the act of moving aimlessly",
"potteringly": "in a pottering manner",
"potters": "plural of potter",
"pottery": [
    "ceramic ware made from clay",
    "the craft of making ceramic ware"
],
"pottier": "more potty (crazy or foolish)",
"potties": "plural of potty",
"pottiest": "most potty (crazy or foolish)",
"potting": [
    "the act of putting a plant in a pot",
    "the act of shooting"
],
"pottles": "plural of pottle",
"potzer": "a person who works in a clumsy way",
"potzer": "one who potzes; a trifler",
"potzers": "plural of potzer",
"pou sto": "a place to stand; a basis for action or argument",
"pouch": ["a small bag", "a pocket-like structure in an animal", "to pocket"],
"pouched": "having a pouch",
"pouched mole": "a burrowing mole with cheek pouches",
"pouched rat": "a rat with external cheek pouches",
"pouchful": "the amount a pouch can hold",
"pouchy": "resembling a pouch",
"poudrette": "a fertilizer made from dried and ground night soil",
"poudreuse": "a woman's dressing table",
"pouf": ["a upholstered stool", "a hair arrangement"],
"pouff": "a variant of pouf",
"pouffe": "a padded stool",
"pouh": "variant of pooh",
"pouilly-fuissé": "a white wine from the Burgundy region",
"pouilly-fumé": "a white wine from the Loire Valley",
"poujadism": "a movement of shopkeepers and small businesses",
"poujadist": "an adherent of poujadism",
"pouke": "a goblin or elf",
"poulaine": "a long-pointed shoe",
"poulard": "a fat, spayed hen",
"poularde": "a French term for a fat hen",
"poule": ["a hen", "a woman prostitute"],
"poulp": "an octopus",
"poulpe": "a cephalopod, usually an octopus",
"poult": "a young chicken or turkey",
"poulter": "a seller of poultry",
"poulterer": "a dealer in poultry",
"poultice": "a soft, moist mass of material, typically of plant material or flour, applied to the body to relieve soreness and inflammation",
"poultry": "domesticated birds",
"poultryman": "one who raises poultry",
"pounce": ["to spring or swoop upon", "a fine powder"],
"pounced": "sprinkled with pounce",
"pouncer": "one who pounces",
"pound": ["a unit of weight", "a place for stray animals", "to strike heavily"],
"poundage": "a tax based on the weight",
"poundal": "a unit of force",
"pounder": "something that pounds",
"pounding": "a heavy, repeating impact",
"pour": "to cause a liquid to flow",
"pourboire": "a tip or gratuity",
"pourparler": "an informal preliminary conference",
"pousse-café": "a liqueur cocktail",
"poussette": "a dance figure in which couples move around each other",
"pout": ["to push out the lips", "a sulky expression"],
"pouter": "a type of pigeon",
"poutine": "a dish of fries, cheese curds, and gravy",
"pouty": "inclined to pout",
"pow": "the sound of an explosion",
"powder": "fine particles",
"power": "the ability to do something",
"pox": "a viral disease",
"poxy": ["infected with pox", "contemptible or worthless"],
"poy": "a balancing pole used by ropedancers",
"poz": ["HIV positive", "an HIV positive person"],
"pozole": "a Mexican stew made with hominy",
"pozzolan": "a siliceous or siliceous and aluminous material which reacts with calcium hydroxide to form compounds possessing cementitious properties",
"praam": "a flat-bottomed boat; a pram",
"prabble": "a petty dispute; a brawl",
"practicable": "capable of being done, effected, or put into practice",
"practical": "designed or adapted for actual use; matter-of-fact or realistic",
"practice": "habitual or customary performance; the exercise of a profession",
"practitioner": "a person who practices a profession or art",
"praenomen": "the first or given name among the ancient Romans",
"praetor": "a magistrate of ancient Rome",
"praetorium": "the official residence of a Roman governor or commander",
"prairie": ["a large area of flat, grassy land in North America", "a treeless grassy plain"],
"prairie alligator": "A term used for the alligator snapping turtle or simply an alligator in a swampy prairie context",
"prairie apple": "A name for Psoralea esculenta, also known as the prairie turnip or breadroot",
"prairie bean": "A type of wild legume (Psoralea) found in the plains",
"prairie breaker": "A plow designed to turn over thick prairie sod",
"prairie chicken": "A mottled brown-and-white grouse (Tympanuchus cupido or T. pallidicinctus)",
"prairie clover": "A plant belonging to the genus Petalostemon (or Dalea)",
"prairie dog": "A burrowing rodent of the American grasslands",
"prairie falcon": "A North American falcon (Falco mexicanus) that is grayish-brown above",
"prairie fire": "A fire occurring in the vast grassland areas",
"prairie grouse": "Another term for the prairie chicken",
"prairie lily": "A plant (Mentzelia nuda) known as the sand lily",
"prairie oyster": "A cocktail consisting of a raw egg, Worcestershire sauce, and spices",
"prairie rattlesnake": "A rattlesnake (Crotalus viridis) of the western North American prairies",
"prairie rose": "A climbing rose (Rosa setigera), state flower of North Dakota",
"prairie schooner": "A covered wagon used by pioneers",
"prairie smoke": "A North American plant (Geum triflorum) with silky-plumed fruit",
"prairie soil": "A type of rich, black soil characteristic of temperate grasslands",
"prairie wolf": "Another name for the coyote",
"praise": ["the act of expressing approval or admiration", "to commend or express warm approval"],
"praiseworthy": "deserving praise or admiration",
"prance": "to move with high, springy steps",
"prank": "a mischievous act or trick",
"prate": "to talk foolishly or at length about something",
"prattle": "to chatter in a foolish or inconsequential way",
"prattled": "past tense and past participle of prattle; spoke foolishly or at length",
"prattlement": "the act of prattling; idle or childish talk",
"prattler": ["a person who talks at length about unimportant matters", "a babbler or chatterer"],
"prattles": "third-person singular present tense of prattle; talks in a childish manner",
"prattling": ["the act of talking in a foolish or simple-minded way", "chattering incesantly"],
"prattlingly": "in a prattling manner; talkatively",
"praxis": ["practice, as distinguished from theory", "accepted practice or custom"],
"pray": ["to ask for something earnestly", "to entreat or implore", "to address God or a deity"],
"prayer": ["a devout petition to a deity", "a formula of worship", "the act of praying"],
"prayerful": ["given to prayer", "devout", "reverent"],
"praying": "the act of addressing a deity or making a fervent request",
"pre": "a prefix occurring in loanwords from Latin, meaning before",
"preach": ["to deliver a sermon", "to proclaim or advocate", "to give moral advice"],
"preacher": ["a person who discourses publicly on religious subjects", "a sermonizer"],
"preachily": "in a preachy manner",
"preachiness": "the quality of being preachy",
"preaching": "the act of delivering a sermon",
"preachify": ["to preach at length", "to moralize"],
"preachment": ["a sermon, especially a tedious one", "a moralizing discourse"],
"preachy": ["given to preaching or moralizing",
"tending to preach", "tediously moralizing","given to tedious moralizing; sermonizing",
"given to sermonizing or moralizing in a tedious way",
"inclined to deliver sermons or moral lessons",
"inclined to preach; moralizing"],
"preacquaint": "to make acquainted beforehand",
"preacquaintance": ["the state of being acquainted beforehand", "prior knowledge"],
"preacquisition": "the act of acquiring something beforehand",
"preact": "to act or perform beforehand",
"preadamic": "relating to the period before Adam",
"preadamite": ["existing before Adam", "a person supposed to have lived before Adam"],
"preadapt": "to adapt beforehand",
"preadaptation": ["an adaptation in an organism that serves a new function", "the process of adapting beforehand"],
"preadaptive": "relating to preadaptation",
"preadipocyte": "a precursor cell to an adipocyte",
"preadjust": "to adjust beforehand",
"preadmission": ["the act of admitting beforehand", "relating to the process before admission"],
"preadmit": "to admit beforehand",
"preadmonish": "to admonish or warn beforehand",
"preadmonition": "a warning or forewarning given beforehand",
"preadolescence": "the period of life just before adolescence",
"preadolescent": ["a child between the ages of 10 and 12", "relating to the period before adolescence"],
"preadopt": "to adopt beforehand",
"preadult": ["not yet an adult", "an organism that is not yet sexually mature"],
"preaged": "aged beforehand",
"preagricultural": "existing or occurring before the development of agriculture",
"preakness": "a prestigious American horse race",
"preallot": "to allot or assign beforehand",
"preallotment": "the act of allotting beforehand",
"prealtar": "the area in front of an altar",
"prealter": "to alter or change beforehand",
"preambulate": "to walk before",
"preamble": ["an introductory statement", "a preliminary account or explanation"],
"preambulary": "of the nature of a preamble",
"preambulatory": "acting as a preamble or introduction",
"preamp": ["a preamplifier", "an electronic amplifier that prepares a signal"],
"preamplifier": "an amplifier that strengthens a weak signal before main amplification",
"preanaesthetic": "occurring before the administration of an anesthetic",
"preanal": "located in front of the anus",
"preanesthetic": "relating to the time before anesthesia",
"preannounce": "to announce beforehand",
"preantiseptic": "occurring before the use of antiseptics",
"preapply": "to apply beforehand",
"preappoint": "to appoint beforehand",
"preapprove": "to approve beforehand",
"prearm": "to arm beforehand",
"prearmed": "armed in advance",
"prearming": "the act of arming beforehand",
"prearms": "plural of prearm",
"prearrange": ["to arrange in advance", "to plan beforehand"],
"prearranged": ["arranged in advance", "planned beforehand"],
"prearrangement": ["an act of arranging in advance", "a prior arrangement"],
"prearranger": "one who arranges beforehand",
"prearranges": "present tense third-person singular of prearrange",
"prearranging": "present participle of prearrange",
"prearray": "to array beforehand",
"prearrest": "occurring before an arrest",
"preascent": "an ascent made before a main ascent",
"preascertain": "to ascertain beforehand",
"preascertained": "ascertained in advance",
"preascription": "a prescription made in advance",
"preassemble": "to assemble beforehand",
"preassembled": "assembled in advance",
"preassemblies": "plural of preassembly",
"preassembly": "preliminary assembly of parts",
"preassign": "to assign beforehand",
"preassigned": "assigned in advance",
"preassignment": "a prior assignment",
"preassigns": "present tense third-person singular of preassign",
"preassist": "to assist in advance",
"preassociated": "associated beforehand",
"preassociation": "a prior association",
"preassume": "to assume beforehand",
"preassumed": "assumed in advance",
"preassumption": "an assumption made in advance",
"preassure": "to assure beforehand",
"preasthetic": "pertaining to a time before aesthetics",
"preastrict": "to bind beforehand",
"preastriction": "a binding in advance",
"preattach": "to attach beforehand",
"preattached": "attached in advance",
"preattachment": "a prior attachment",
"preattack": "an attack made before a main attack",
"preattempt": "to attempt beforehand",
"preattention": "attention given in advance",
"preattune": "to attune beforehand",
"preaudience": "a preliminary audience",
"preaudit": "an audit conducted beforehand",
"preauditing": "the process of conducting a preaudit",
"preaudits": "plural of preaudit",
"preaugment": "to augment beforehand",
"preauthorization": "an authorization given in advance",
"preauthorized": "authorized beforehand",
"preavail": "to avail beforehand",
"preaverage": "to calculate an average beforehand",
"preavoid": "to avoid beforehand",
"preavoidance": "a prior avoidance",
"preawake": "to wake beforehand",
"preawaken": "to awaken in advance",
"preawarded": "awarded beforehand",
"preaxis": "situated before an axis",
"prebaby": "pertaining to the period before a baby",
"prebachelor": "pertaining to the period before bachelorhood",
"prebaconian": "before Francis Bacon",
"prebacteria": "microorganisms preceding true bacteria",
"prebacterial": "relating to prebacteria",
"prebad": "before a bad event",
"prebalance": "to balance beforehand",
"prebalanced": "balanced in advance",
"prebalancing": "the act of balancing beforehand",
"preballot": "a vote taken before the official ballot",
"prebanquet": "a gathering held before a banquet",
"prebarbaric": "before the barbaric age",
"prebarbarous": "before the barbarous age",
"prebase": "to base beforehand",
"prebased": "based in advance",
"prebasic": "pertaining to a primary or initial stage",
"prebasin": "situated before a basin",
"prebattle": "occurring before a battle",
"prebeam": "to beam beforehand",
"prebeat": "a beat before a main beat",
"prebeatify": "to beatify beforehand",
"prebecome": "to become beforehand",
"prebed": "to bed beforehand",
"prebeetle": "before the age of beetles",
"prebegin": "to begin beforehand",
"prebeginning": "a start before the main start",
"prebehold": "to behold beforehand",
"prebeliever": "one who believed beforehand",
"prebellic": "occurring before a war",
"prebelligerent": "existing before a war",
"prebend": "the stipend of a canon",
"prebendal": "relating to a prebend",
"prebendary": "a clergyman holding a prebend",
"prebendaries": "plural of prebendary",
"prebendalism": "the system of prebends",
"prebends": "plural of prebend",
"prebent": "bent beforehand",
"prebeset": "to beset beforehand",
"prebetray": "to betray beforehand",
"prebetter": "to make better beforehand",
"prebeyond": "situated before a further point",
"prebias": "a bias existing before a study",
"prebiblical": "before the time of the Bible",
"prebid": "to bid beforehand",
"prebidder": "one who bids beforehand",
"prebidding": "the act of bidding beforehand",
"prebirth": "existing before birth",
"prebite": "a bite before a meal",
"prebitter": "to make bitter beforehand",
"prebiotic": ["of, relating to, or being chemical or environmental precursors of the origin of life", "existing or occurring before the origin of life"],
"prebuild": "to build beforehand",
"precalculation": "a calculation made in advance",
"precarity": "the state of being precarious or insecure",
"precancel": ["to cancel a stamp before it is used", "a postage stamp canceled in advance"],
"precaution": ["a measure taken in advance to prevent harm", "caution employed beforehand"],
"precede": ["to come before in time", "to be earlier than", "to exist before"],
"precedent": ["an earlier event or action that is regarded as an example or guide", "preceding in time, order, or importance"],
"precentor": ["a person who leads a church choir or congregation in singing"],
"precept": ["a general rule intended to regulate behavior or thought", "a command or principle"],
"precinct": ["a district of a city or town for police purposes", "a voting district", "an enclosed or fenced area"],
"precinct captain": "a political party official who organizes voters in a specific district",
"precinctive": "relating to a precinct or limited district",
"precincts": "the grounds or area immediately surrounding a building",
"preciosity": "excessive refinement or fastidiousness in language or art",
"precious": "of high price or great value",
"precious metal": "a rare, naturally occurring metallic chemical element of high economic value, such as gold or silver",
"precious stone": "a highly prized gem",
"preciously": "in a manner showing extreme refinement",
"preciousness": "the quality of being valuable or delicate",
"precipice": "a very steep rock face or cliff",
"precipitable": "able to be precipitated",
"precipitance": "the quality of being hasty or rash",
"precipitancy": "a rash, impetuous haste",
"precipitant": "a substance that causes a precipitate to form",
"precipitate": ["to cause a substance to be deposited in solid form from a solution", "to bring about abruptly", "rash or impulsive"],
"precipitation": ["the action of precipitating", "rain, snow, sleet, or hail", "a solid substance separated from a solution"],
"precipitator": "a device for precipitating particles from a gas",
"precipitous": ["extremely steep", "rash or impulsive", "done with great haste"],
"precipitously": "in a steep or headlong manner",
"preciput": "a portion of an estate taken by one heir before dividing the rest",
"precis": "a summary or abstract of a text or speech",
"precise": ["marked by exactness and accuracy", "sharply defined", "strict"],
"precisely": ["in an exact or accurate manner", "exactly", "quite so"],
"preciseness": "the quality of being precise",
"precision": "the quality of being accurate and exact",
"preclude": "to prevent from happening",
"preclusion": "the act of preventing",
"preclusive": "serving to preclude or prevent",
"precocious": ["having developed certain abilities at an earlier age than usual", "mature"],
"precociously": "in a manner showing early development",
"precociousness": "the quality of being precocious",
"precocity": "precocious development",
"precognition": "knowledge of a future event",
"precognitive": "relating to precognition",
"preconceive": "to form an opinion before full knowledge",
"preconceived": "formed beforehand",
"preconception": "a preconceived idea or prejudice",
"preconcert": "to arrange beforehand",
"preconcerted": "arranged in advance",
"precondition": "a condition that must be fulfilled beforehand",
"precontract": "a contract made before another",
"precordia": "the region of the chest over the heart",
"precordial": "relating to the precordia",
"precursor": "a person or thing that comes before another",
"precursorily": "in a precursor manner",
"precursory": "preceding or hinting at",
"precut": "cut beforehand, as in lumber",
"predate": ["to exist or occur at a date earlier than", "to mark with an earlier date"],
"predation": "the preying of one animal on others",
"predator": "an animal that naturally preys on others",
"predatory": ["seeking to exploit others", "relating to preying on other animals"],
"predatrix": "a female predator",
"predecease": "to die before another person",
"predecessor": "a person who held a job before the current holder",
"predecessors": "the people who came before in time",
"predefine": "to define beforehand",
"predefined": "already defined",
"predestinarian": "one who believes in predestination",
"predestinate": "to determine beforehand",
"predestination": "the divine foreordaining of all that will happen",
"predestine": "to decree beforehand",
"predestined": "determined in advance",
"predetermination": "the act of determining beforehand",
"predetermine": "to decide in advance",
"predetermined": "decided beforehand",
"predicability": "the capability of being predicated",
"predicable": "that which can be affirmed or predicated",
"predicament": "a difficult or unpleasant situation",
"predicamental": "relating to a predicament",
"predicant": "a preaching friar",
"predicate": ["the part of a sentence that modifies the subject", "to affirm or declare"],
"predication": "an affirmation or assertion",
"predicative": "serving to predicate",
"predict": "to say that an event will happen in the future",
"predictability": "the quality of being predictable",
"predictable": "able to be predicted",
"predictably": "in a way that is expected",
"prediction": "a statement about the future",
"predictive": "relating to prediction",
"predictor": "a person who predicts",
"predigest": "to digest beforehand",
"predigestion": "the act of predigesting",
"predilection": "a preference or special liking for something",
"predispose": "to make someone inclined to a specific attitude",
"predisposed": "inclined towards something",
"predisposition": "a tendency or inclination",
"predominance": "the state of being superior in number or power",
"predominant": "present as the strongest or main element",
"predominantly": "mainly or for the most part",
"predominate": "to be the strongest or main element",
"predomination": "the act of predominating",
"pre-eminent": "surpassing all others",
"pre-eminence": "the state of being pre-eminent",
"pre-eminently": "above all",
"preen": "to straighten and clean feathers with a beak",
"preener": "one who preens",
"pre-existent": "existing beforehand",
"pre-existence": "the state of existing before or earlier than something else",
"pre-existent": ["existing before", "existing in a former state or previous to something else"],
"preexist": "to exist beforehand or prior to a certain point in time",
"preexistence": "the state of having existed previously",
"preexistencist": "one who believes in the preexistence of the soul",
"preexistency": "the state of pre-existing",
"pre-existent": "existing before",
"pre-existentiary": "relating to a former existence",
"pre-existerian": "one who holds to pre-existence",
"pre-existimation": "a prejudgment; a prior estimation",
"pre-existing": "existing previously or before something",
"pre-existing condition": "a medical condition that a person has before a new health insurance policy starts",
"pre-experimental": "relating to research design lacking a control group",
"pre-expose": "to expose beforehand, as in film photography",
"pre-factor": "a factor that appears before another",
"prefab": "manufactured in standard sizes to be shipped and assembled elsewhere",
"prefabricate": ["produce synthetically or stereotypically", "to manufacture sections of a building beforehand"],
"prefabrication": "the manufacture of sections of a building at the factory",
"preface": ["a short introductory essay preceding the text of a book", "to furnish with a preface"],
"prefaded": "having been given a faded appearance by artificial means",
"prefatorial": "serving as an introduction or preface",
"prefatory": "serving as an introduction or preface",
"prefect": "a chief officer or chief magistrate",
"prefectural": "of or relating to a prefecture",
"prefecture": "the district administered by a prefect",
"prefectship": "the office or position of a prefect",
"prefer": ["like better; value more highly", "to present or submit for consideration"],
"preferable": "more desirable than another",
"preferably": "more readily or willingly",
"preference": ["the right or chance to choose", "a feeling of liking or wanting one person or thing more than another"],
"preference shares": "stock whose holders are guaranteed priority in the payment of dividends",
"preferent": "preferred above all others and treated with partiality",
"preferential": "showing favor or partiality",
"preferentially": "in a preferential manner",
"preferment": "the act of liking one thing more than another",
"preferred": "more desirable than another",
"preferred shares": "stock whose holders are guaranteed priority",
"preferred stock": "stock whose holders are guaranteed priority",
"prefiguration": "the act of providing vague advance indications",
"prefigurative": "indistinctly prophetic",
"prefigure": ["indicate by signs", "be an early indication of"],
"prefigurement": "a prefiguring; an omen",
"prefix": ["an affix that is added in front of the word", "to attach a prefix to"],
"prefixation": "formation of a word by means of a prefix",
"prefixing": "the act of adding a prefix",
"prefixion": "the act of prefixing",
"preflight": ["happening before a flight", "to check an aircraft before flight"],
"preform": ["form or shape beforehand", "to determine the shape of beforehand"],
"preformation": ["a theory that an individual develops by simple enlargement of a tiny fully formed organism", "the act of preforming"],
"preformationist": "an adherent to the theory of preformation",
"preformat": "to format beforehand",
"prefrontal": "anterior to a frontal structure",
"prefrontal cortex": "the brain region related to decision-making, personality, and behavior",
"prefrontal leucotomy": "surgical interruption of nerve tracts to and from the frontal lobe",
"prefrontal lobe": "the brain region related to decision-making, personality, and behavior",
"prefrontal lobotomy": "surgical interruption of nerve tracts",
"prefreeze": "to freeze before a certain process",
"pregame": "occurring before a game",
"preglacial": "occurring before the glacial period",
"pregracial": "occurring before the era of grace",
"pregravid": "before pregnancy",
"pregrowths": "growths that appear beforehand",
"preguy": "a guide for a pre-preparatory process",
"preguiding": "guiding beforehand",
"prehardens": "hardens beforehand",
"preharvest": "occurring before the harvest",
"preheat": ["heat beforehand", "to warm up an oven"],
"preheater": "a device for heating something beforehand",
"preheating": "the process of heating beforehand",
"prehensile": "adapted for grasping especially by wrapping around an object",
"prehension": "the act of gripping something firmly with the hands",
"prehensor": "the anterior pair of legs of a centipede modified to seize prey",
"prehuman": "existing before the appearance of human beings",
"prehumans": "prehuman creatures",
"preimposes": "imposes beforehand",
"preimposed": "imposed beforehand",
"preinforms": "informs beforehand",
"preinvites": "invites beforehand",
"preinvited": "invited beforehand",
"prejudge": "judge beforehand, especially without sufficient evidence",
"prejudged": "judged beforehand",
"prejudgement": "a judgment reached before the evidence is available",
"prejudger": "one who judges beforehand",
"prejudges": "judges beforehand",
"prejudging": "the act of judging beforehand",
"prejudgment": "a judgment reached before the evidence is available",
"prejudiced": "partiality preventing objective consideration of an issue",
"prejudices": "partialities preventing objective consideration",
"prejudice": "a partiality preventing objective consideration of an issue",
"prejudicial": "detrimental; causing prejudice",
"prejudgmental": "forming a judgment too soon",
"preknowledge": "knowledge of an event before it occurs",
"prelaunch": "happening before a launch",
"prelaw": "pertaining to studies before law school",
"prelect": "to read a lecture or discourse",
"prelection": "a lecture or reading",
"prelector": "a lecturer",
"preliminary": ["an action that comes before", "leading up to a main occurrence"],
"prelude": "an introduction to a musical piece or something that comes before an event",
"preludial": "serving as a prelude",
"preluder": "one who plays a prelude",
"preluding": "acting as a prelude",
"prelusive": "serving as an introduction",
"prelusory": "prelusive",
"premarital": "occurring before marriage",
"premarket": "existing before the market opens",
"premature": ["too soon or too hasty", "born before the full term"],
"prematurity": "the quality of being premature",
"premaxilla": "a bone in the upper jaw",
"premaxillary": "relating to the premaxilla",
"premed": "a course of study to prepare for medical school",
"premedicate": "to medicate beforehand",
"premeditated": "planned or plotted in advance",
"premeditation": "consideration, pondering, or planning an action beforehand",
"premeds": "premedical students",
"premenstrual": "occurring before menstruation",
"premenstrually": "in a premenstrual manner",
"premenstruation": "the time before menstruation",
"premillenarian": "one who believes in a literal millennium",
"premillennial": "existing before the millennium",
"premonish": "to warn beforehand",
"premonition": ["a feeling of evil to come", "a forewarning"],
"premonitory": "serving to warn beforehand",
"premonstrant": "a member of the Premonstratensian order",
"premorbid": "existing before the occurrence of a disease",
"premorse": "appearing as if bitten off at the end",
"premotion": "a previous motion",
"premove": "to move beforehand",
"premovement": "The act of moving beforehand; a preliminary movement",
"premultiplication": "The act of multiplying by a matrix or factor on the left",
"premultiply": ["To multiply a matrix on the left side", "To multiply before another operation"],
"premundane": "Existing before the creation of the world",
"premune": "To protect or immunize in advance",
"premunite": "To fortify or strengthen beforehand",
"premunition": "A state of resistance to infection, established by a previous infection",
"premonition": "A feeling of anticipation of or anxiety over a future event",
"premonitory": "Serving to warn beforehand",
"premortal": "Existing before death",
"premorse": "Appearing as if bitten off at the end",
"premorbid": "Occurring before the onset of a disease",
"premolar": "A tooth situated between the canine and the molars",
"premonitor": "One who, or that which, gives premonition.",
"premonitorily": "In a premonitory manner; by way of warning.",
"premonitory": ["Giving premonition", "Serving to warn beforehand", "Ominous or foreboding"],
"premonsoon": "The period or season immediately before the monsoon.",
"premonstrant": "One who indicates or shows beforehand.",
"premonstrate": "To show or point out beforehand.",
"premonstratensian": "A member of an order of regular canons founded at Prémontré in 1120.",
"premorbid": "Occurring before the development of a disease.",
"premotor": "Relating to the cortex of the brain anterior to the motor area.",
"premultiplication": "The act of multiplying a matrix by another from the left.",
"premultiply": "To multiply a matrix by another from the left.",
"prenatal": "Existing or occurring before birth.",
"prenatally": "Before birth.",
"pre-need": "Arranged or purchased before death, as in insurance or funeral services.",
"prenominal": "Occurring before a noun; relating to a title.",
"prenominally": "in a prenominal manner; before a noun",
"prenominate": ["to name in advance", "nominated before"],
"prenomination": "the act of naming beforehand",
"prenoon": "the time before noon",
"prenote": "to note beforehand",
"prenotification": "a notification given beforehand",
"prenotify": "to notify or announce beforehand",
"prenotion": "a notion or presumption formed beforehand",
"prent": "variant of prentice; to apprentice",
"prentice": "an apprentice",
"prenticeship": "the state or period of being an apprentice",
"prenubile": "before the age of marriage",
"prenuclear": "before the existence of nuclear weapons or technology",
"prenumber": "to number or count beforehand",
"prenup": "a prenuptial agreement",
"prenuptial": "occurring before marriage",
"prenzie": "variant of princely (archaic)",
"preobtain": "to obtain beforehand",
"preoccupancy": "the act of taking possession beforehand",
"preoccupant": "that preoccupies",
"preoccupate": ["to take possession of before another", "to preoccupy"],
"preoccupatio": "latin root word for anticipation",
"preoccupation": ["the state of being engrossed", "the act of occupying something before someone else", "an idea that occupies the mind"],
"preoccupied": ["absorbed in thought", "having one's attention taken up by thoughts", "previously taken or filled"],
"preoccupiedly": "in a preoccupied manner",
"preoccupiedness": "the state of being preoccupied",
"preoccupies": ["third-person singular simple present of preoccupy", "takes up the attention of beforehand"],
"preoccupy": ["to engage the attention of beforehand", "to take possession of before someone else"],
"preoccupying": ["present participle of preoccupy", "monopolizing attention"],
"preopinion": "a previous opinion; prejudice (archaic)",
"preoption": "a prior choice or right of choice",
"preordain": ["to ordain or decree beforehand", "to predetermine"],
"preordained": "set or decreed beforehand",
"preordination": "the act of preordaining",
"prep": ["preparation (informal)", "to prepare"],
"preparation": ["the act of making ready", "a state of being prepared"],
"preparative": "serving to prepare; preparatory",
"preparatory": "Serving or designed to prepare; introductory.",
"preparatory school": "A school that prepares students for college or university.",
"preparatory to": ["In preparation for", "In anticipation of"],
"preparatory work": "Preliminary work done before a main task.",
"preparatorily": "In a preparatory manner.",
"preparatory sketch": "A preliminary drawing or study for a larger work.",
"preparatory drawing": "A drawing made in preparation for a final artwork.",
"prepatellar": "Situated in front of the patella.",
"prepay": ["To pay in advance", "To pay for something before it is received"],
"prepayment": ["The act of paying in advance", "A payment made in advance"],
"prepayphone": "A telephone that requires payment before use.",
"prepense": "Premeditated; considered beforehand.",
"preponderance": ["The quality or fact of being greater in number, quantity, or importance", "Superiority in power or influence"],
"preponderant": "Superior in power, weight, or numbers.",
"preponderantly": "In a preponderant manner.",
"preponderate": ["To be greater in number, weight, or power", "To exceed in influence"],
"preponderating": "Exceeding in power or influence.",
"preposition": "A word governing, and usually preceding, a noun or pronoun and expressing a relation to another word.",
"prepositional": "Relating to or consisting of a preposition.",
"prepositive": "Placed before; having the character of a prefix.",
"prepositor": "A school prefect.",
"prepossess": ["To preoccupy the mind of someone", "To make a favorable impression"],
"prepossessed": "Preoccupied or prejudiced.",
"prepossessing": "Attractive or appealing.",
"prepossession": ["A preconceived opinion or prejudice", "The state of being prepossessed"],
"preposterous": "Contrary to reason or common sense; utterly absurd.",
"preposterously": "In a preposterous manner.",
"preposterousness": "The quality of being preposterous.",
"prepotence": "The quality of being superior in power or influence.",
"prepotency": "Superior power or influence.",
"prepotent": "Having great or supreme power.",
"prepotently": "In a prepotent manner; with superior power, force, or influence",
"prepotential": "Having or exhibiting prepotence",
"prepped": "Prepared; made ready",
"prepper": ["A person who prepares for a disaster or emergency", "A person who prepares something"],
"preppie": ["A student at an expensive private school", "A person who dresses in a style associated with preparatory school students"],
"preppies": "Plural of preppie",
"preppily": "In a preppy manner",
"preppiness": "The quality or state of being preppy",
"prepping": "The act or process of making something ready",
"preppy": ["Of, relating to, or characteristic of a student or graduate of a preparatory school", "A style of clothing"],
"preprandial": "Taking place before dinner",
"prepreference": "A preference that is established beforehand",
"prepreg": ["A reinforcing fabric which has been pre-impregnated with a resin system", "Short for pre-impregnated"],
"preprepared": "Prepared in advance",
"prepresidential": "Before becoming president",
"prepress": "The process of preparing material for printing",
"preprice": "To mark a price on something before it is sold",
"preprimary": "Occurring before a primary election",
"preprint": "A version of a scientific paper or other document that has not yet been published in a peer-reviewed journal",
"preprocess": "To process data before the main processing occurs",
"preprocessor": "A program that prepares data for another program",
"preproduction": "The work done on a product, especially a film or play, before full-scale production begins",
"preprofessional": "of or relating to the period of training before entering a profession",
"preprogram": "to program in advance",
"preprogrammed": "programmed or planned ahead of time",
"preprogramming": "the act or process of planning or programming something in advance",
"preproinsulin": "a precursor of proinsulin",
"preprophase": "the stage before mitosis or meiosis in a cell cycle",
"preprotein": "a protein synthesized with a signal sequence that is cleaved during secretion",
"preprocess": "to process data before the main processing takes place",
"preprocessed": "processed beforehand",
"preprocesses": "performs preliminary processing on data",
"preprocessing": ["the initial processing of data", "actions taken before main production"],
"preprocessor": "a program that prepares input for another program",
"pre-production": ["planning and preparation before filming", "the stage before actual production begins"],
"preproduction": "a synonym for pre-production",
"preproduction model": "a prototype manufactured to test production processes",
"preproduction trial": "a trial run of manufacturing to test functionality",
"prepsychedelic": "relating to the period before the psychedelic movement",
"prepsychotic": "occurring before the onset of psychosis",
"prepuberal": "relating to the time before puberty",
"prepubertal": "alternative spelling of prepuberal",
"prepuberty": "the period immediately before puberty",
"prepubescence": "the period of growing up just before puberty",
"prepubescent": "a person in the stage before puberty",
"prepubis": "the anterior part of the pubic bone",
"prepublication": "occurring or produced before publication",
"prepublish": "to publish something before its official release",
"prepuce": "a fold of skin covering the glans penis or clitoris",
"prepueblo": "related to the period before the Pueblo culture",
"prepulse": "a pulse that precedes a main pulse",
"prepunch": "to punch or perforate in advance",
"prepunctual": "occurring or arriving before the scheduled time",
"prepupa": "the larval stage immediately before the pupa",
"prepupal": "relating to the prepupa stage",
"prepurchase": "to purchase something in advance",
"preputial": "relating to the prepuce",
"prequalify": "to qualify or certify in advance",
"prequel": "a literary or cinematic work that precedes a previous work",
"prerace": "occurring before a race",
"preradio": "occurring before the era of radio",
"prereading": "activities done before reading a text",
"prerecession": "occurring before a recession",
"prerecord": "to record in advance",
"prerecorded": "recorded before broadcasting or use",
"prerectal": "situated in front of the rectum",
"prereform": "relating to the period before a reform",
"preregister": "to register in advance",
"preregistration": "the act of registering beforehand",
"prerehearsal": "occurring before a formal rehearsal",
"prerelease": ["of or relating to a period prior to an official release", "something released before an official or scheduled date"],
"prereleased": "released on a limited basis before the date fixed for general release",
"prerelease center": "a facility for housing convicts before their final release",
"prerelease program": "a program designed to help prisoners reintegrate into society before their release date",
"prereleasing": "to release a product, film, or software before its general release date",
"prereligious": "relating to a time or condition before the existence of religion",
"preremote": "a term for an action or device occurring before a remote event",
"prerenal": "situated or occurring in front of the kidney",
"prereproductive": "relating to an age or period before an organism is capable of reproduction",
"prerept": "an archaic form, usually a verb, meaning to take beforehand",
"prereption": "the act of seizing or taking beforehand",
"prerequire": "to require or demand something beforehand",
"prerequired": "previously required or stipulated",
"prerequisite": "something that is needed or obligatory in advance",
"preresolve": "to resolve or determine something beforehand",
"prerest": "the state of resting or being prepared before an action",
"preretire": "to prepare for retirement before it officially happens",
"preretirement": "the period just before one officially retires from work",
"prereview": "a review or assessment done prior to a formal review",
"prerevisionist": "relating to a period before the revisionist movement",
"prerevolution": "the period existing before a revolution",
"prerevolutionary": "relating to a time before a political or social revolution",
"prerinse": "to rinse something before the main washing process",
"presage": "a sign or warning that something (typically bad) will happen",
"presale": "the sale of something before it is officially available to the public",
"presales": ["Before a product is sold", "Sales activities before purchase decision"],
"presalt layer": "A geologic layer below a salt deposit",
"presanctification": "The act of consecrating the Eucharistic elements at a previous Mass",
"presanctified": ["(of the Eucharistic elements) consecrated at a previous Mass", "An adjective form of presanctify"],
"presanctify": "To sanctify or consecrate beforehand",
"presartorial": "Before the time of tailoring or before something is tailored",
"presay": "To say or predict beforehand",
"presbycusis": "Age-related hearing loss",
"presbyope": "A person suffering from presbyopia",
"presbyopia": "Farsightedness caused by loss of elasticity of the lens of the eye, occurring typically in middle and old age",
"presbyopic": "Relating to or affected by presbyopia",
"presbyter": ["An elder or minister in the Christian church", "A presbyterian"],
"presbyteral": "Relating to a presbyter or to the order of presbyters",
"presbyterate": ["The office or order of a presbyter", "The body of presbyters"],
"presbyterial": "Relating to a presbyter or presbytery",
"presbyterian": ["A member of a Presbyterian church", "Relating to a church government by presbyters"],
"presbyterianism": "The system of church government by presbyters",
"presbytery": ["A body of elders in a Presbyterian church", "A district in the Methodist Church", "The part of a church choir reserved for the clergy"],
"presc": "Abbreviation for prescription",
"prescapular": "Situated in front of the scapula",
"prescient": "Having or showing knowledge of events before they take place",
"prescience": "Foreknowledge of events",
"prescind": "To cut off; to abstract or disregard",
"prescind from": "To leave out of consideration",
"prescript": ["An ordinance or decree", "A prescription"],
"prescriptible": "Capable of being prescribed",
"prescription": ["An instruction written by a medical practitioner", "A prescribed remedy", "The action of establishing something as a rule", "A right acquired by long usage"],
"prescriptive": ["Relating to or imposing a rule or method", "Based on long usage or custom"],
"prescriptivism": "The attitude of enforcing a prescriptive rule",
"preselect": "To select in advance",
"preselection": "The act of selecting in advance",
"presell": ["To sell or promote something before it is officially released", "To make a sale before a product is finished"],
"preselling": "The action of selling something before it is formally offered",
"presenile": "Occurring before the onset of old age",
"presenility": "The state of being presenile",
"presence": ["The state of being in a particular place", "The impressive manner or appearance of a person", "A ghost or spirit"],
"presence of mind": "The ability to remain calm and take quick action in a difficult situation",
"presential": "Relating to presence",
"presentiment": "A feeling that something bad is about to happen",
"preservable": "Capable of being preserved",
"preservation": "The act of keeping something safe or in its original state",
"preservative": "A substance used to prevent decomposition or fermentation",
"preserve": ["To keep safe from harm", "To maintain something in its original state", "To treat food to prevent decay"],
"preserver": "A person or thing that preserves",
"preses": "A chairman or president",
"preside": ["To be in the position of authority at a meeting", "To exercise control or influence"],
"presidency": ["The office of a president", "The period of a president's term"],
"president": ["The elected head of a republican state", "The head of an organization", "The head of a college"],
"presidential": "Relating to a president",
"presidiary": "Relating to a garrison",
"presidio": "A fortified military settlement",
"presidium": "A standing committee having administrative power",
"press": ["To apply force to something", "To move in a specific direction", "A machine for printing", "Newspapers and journalists"],
"press agent": "A person employed to get publicity for a person or organization",
"press conference": "An interview given to journalists",
"press release": "An official statement issued to newspapers",
"pressroom": "A room where printing presses are located",
"pressure": ["The continuous physical force exerted on an object", "Mental stress", "The action of influencing someone"],
"pressure group": "An organized group that tries to influence public policy",
"pressure vessel": "A container designed to hold gases or liquids at a pressure different from the ambient pressure",
"pressurize": "To maintain normal atmospheric pressure inside an aircraft or cabin",
"prestige": ["Widespread respect and admiration", "The reputation of a person or organization"],
"prestigeful": "Having a high level of prestige",
"prestidigitation": "Sleight of hand",
"prestidigitator": "A magician or conjuror",
"prestigeous": "Relating to prestige",
"presto": "In a quick tempo",
"prestore": "A system for storing data before it is processed",
"presubmission": "Before the submission of a document",
"presuppose": "To require as a precondition",
"presupposition": "A tacit assumption",
"presurmise": "A previous surmise",
"presurvey": "A preliminary survey",
"presurveyed": "Surveyed beforehand",
"presynapsis": "The area before a synapse",
"presynaptic": "Situated before a synapse",
"presystole": "The time immediately before the systole",
"presystolic": "Occurring before the systole",
"pret": ["Ready, prepared", "A slang term for a pret-a-porter clothing line"],
"preta": "A hungry ghost in Buddhist theology",
"pretape": "To record audio or video in advance",
"pretarsus": "The distal-most segment of the insect leg",
"pretax": "Occurring or calculated before taxes are deducted",
"pretaxate": "To tax beforehand",
"pretaxation": "The act of taxing in advance",
"pretaxed": "Taxed before distribution or receipt",
"preteen": "A child between the ages of 10 and 12",
"pretender": "One who lays claim to a title or throne",
"pretense": "An attempt to make something false appear true",
"pretension": "A claim or the assertion of a claim to something",
"pretentious": "Attempting to impress by affecting greater importance",
"preter": "A prefix meaning beyond, past, or more than",
"preterite": "A tense of verbs denoting a completed action in the past",
"preternatural": "Beyond what is normal or natural",
"pretext": "A reason given in justification of a course of action that is not the real reason",
"pretzel": "A crisp biscuit baked in a knot or stick shape",
"pretzled": "Twisted or bent out of shape",
"preunion": "A prior union",
"preuniversity": "Relating to the period before university education",
"preurban": "Existing or occurring before the development of a city or urban area",
"preussen": "German name for Prussia",
"preux-chevalier": "A gallant or brave knight",
"prevalence": ["The fact or condition of being prevalent", "Common occurrence"],
"prevalent": ["Widespread in a particular area at a particular time", "Common"],
"prevaricate": ["To speak or act in an evasive way", "To avoid telling the truth"],
"prevenient": ["going before", "preceding", "anticipating", "hindering"],
"prevenient grace": "grace that precedes human response to God",
"preveniently": "in a prevenient manner",
"prevening": "archaic or obsolete form of preceding",
"prevent": ["to hinder or stop from happening", "to keep from doing something", "to render impossible by advance action"],
"preventability": "the quality of being preventable",
"preventable": ["capable of being prevented", "avoidable"],
"preventative": ["preventing or slowing the course of an illness or disease", "a precautionary measure"],
"preventatively": "in a preventative manner",
"prevention": ["the act of hindering or preventing", "measures taken to avoid an event"],
"preventional": "of or relating to prevention",
"preventive": ["serving to prevent or hinder", "a prophylactic"],
"preventively": "in a preventive manner",
"preventor": "one who or that which prevents",
"preventorium": "an institution for treating people who are exposed to disease",
"prevertebral": "located in front of a vertebra",
"prevesical": "Situated in front of the urinary bladder",
"prevesical space": "A potential space located between the bladder and the pubic symphysis",
"previable": "A fetus that is not yet capable of surviving outside the uterus",
"previable period": "The timeframe before a fetus is considered viable",
"previant": "A variant form of spelling, often archaic or non-standard",
"pre-victorian": "Relating to the period before the reign of Queen Victoria (before 1837)",
"previde": "Archaic: to foresee or provide for",
"previdence": "Archaic: foresight or providence",
"preview": ["An inspection or viewing of something before it is made public", "To view or show something in advance"],
"previewed": "Past tense of preview: seen beforehand",
"previewing": "Present participle of preview: viewing beforehand",
"previous": ["Existing or occurring before in time or order", "Prior; former"],
"previously": "At a previous or earlier time",
"prey": ["an animal hunted or caught for food", "a person who is the aim of an attack", "to feed on or hunt for"],
"prey on": ["to hunt or seize food by killing other animals", "to take advantage of or exploit someone", "to weigh heavily on the mind"],
"prey upon": "to seize and devour prey, to victimize another or others",
"preyer": "one who, or that which, preys",
"preying": ["the act of hunting or seizing for food", "profiting from in an exploitatory manner"],
"preyful": "serving to prey; predatory",
"prez": "a president",
"prezzies": "presents or gifts",
"prezzo": "a price",
"prezygapophysis": "a zygapophysis directed forward",
"prezygotic": "occurring or existing before the completion of fertilization",
"prezonular": "located in front of the zonule of Zinn",
"prezonal": "situated anterior to the pelvic girdle",
"prezone": ["to establish the zone into which a property will fall under zoning", "a prozone (immunology)"],
"prezoea": "a larval stage of some crustaceans",
"prezygapophysial": "relating to the prezygapophysis (articular process of a vertebra)",
"prezygapophysis": "the forward articular process of a vertebra",
"prezygapophyses": "plural of prezygapophysis, articular processes on the anterior end of a vertebra",
"prezygapophysis": [
    "an anterior articular process of a vertebra",
    "a bony projection that articulates with the postzygapophysis of the preceding vertebra"
],
"priapic": [
    "of, relating to, or resembling a phallus",
    "phallic",
    "characterized by a preoccupation with male sexuality or virility"
],
"priapism": [
    "a persistent and painful erection of the penis",
    "a medical condition in which the penis remains erect for an extended time"
],
"price": [
    "the amount of money expected or required for a thing",
    "the cost at which something is obtained",
    "value or worth"
],
"priceless": [
    "having a value beyond any price",
    "invaluable",
    "very amusing or absurd"
],
"pricelessly": "in a way that is too valuable to be priced",
"pricelessness": "the quality or state of being priceless",
"price list": "a list of prices for goods or services",
"pricey": ["expensive", "costly", "high-priced"],
"price-fix": "to conspire to set prices at a certain level",
"prich": "a prig; a person who is strict about moral behavior",
"prick": ["a small hole made by a sharp point", "to pierce slightly", "a sting"],
"prickle": ["a small sharp-pointed spine", "to sting or tingle"],
"prickly": ["having prickles", "easily annoyed"],
"prickly heat": "an itchy rash caused by trapped sweat",
"prickly pear": "a cactus with edible fruits",
"prick-me-dainty": "a pretentious or over-refined person",
"prick-post": "an upright timber in a building frame",
"prick-song": "musical music written down or pricked",
"prick-wheel": "a tool for making a series of holes",
"pride": ["a feeling of deep pleasure", "a group of lions", "to take satisfaction in"],
"prideful": "full of pride; haughty",
"pridefully": "in a proud manner",
"pridefulness": "the quality of being prideful",
"prideland": "a region of pride",
"prider": "one who takes pride",
"prides": "plural of pride",
"pride-stock": "the source of one's pride",
"pridie": "the day before (Latin)",
"priding": "taking pride in",
"pridingly": "in a manner of taking pride",
"pridnestrovie": "a region in eastern europe",
"prie": "a rare variant of pry",
"prie-dieu": ["a desk for prayer", "a kneeling chair"],
"pried": "past tense of pry",
"prier": "one who pries or investigates",
"priers": "plural of prier",
"pries": ["investigates or inquires closely", "plural of prie"],
"priest": ["a person authorized to perform sacred rituals", "a minister of a church"],
"priestal": "relating to a priest",
"priestcraft": ["the policy of priests", "the craft of a priest"],
"priestdom": "the state or influence of priests",
"priestess": "a female priest",
"priesthood": ["the office of a priest", "the body of priests"],
"priest": [
    "a person whose office it is to perform religious rites and ceremonies",
    "a clergyman in certain churches",
    "a minister of a church",
    "a person who acts as a mediator between God and humans"
],
"priest-hole": "a small, concealed room used to hide priests during persecution",
"priest-ridden": "dominated by the influence of priests",
"priestcraft": "the policy or practices of priests, often in a derogatory sense",
"priesthood": [
    "the office or position of a priest",
    "the body of priests collectively",
    "the state or condition of being a priest"
],
"priestly": [
    "of, relating to, or befitting a priest",
    "characteristic of or suitable for a priest"
],
"priestliness": "the quality or state of being priestly",
"priestess": "a female priest",
"priestesshood": "the office or position of a priestess",
"priestfish": "a type of fish",
"priesthead": "the office or rank of a priest",
"priestial": "relating to a priest",
"priestianity": "a derogatory term for a religion centered on priestly authority",
"priestin": "to admit to the priesthood",
"priestish": "having characteristics of a priest",
"priestism": "the system or influence of a priesthood",
"priestless": "without a priest",
"priestlet": "a young or minor priest",
"priestery": "a body of priests, often in a disparaging sense",
"priestlike": "resembling a priest",
"priestly": [
    "of, relating to, or befitting a priest",
    "characteristic of or suitable for a priest"
],
"priesthood": [
    "the office or position of a priest",
    "the body of priests collectively",
    "the state or condition of being a priest"
],
"priestly": [
    "of, relating to, or befitting a priest",
    "characteristic of or suitable for a priest"
],
"priests": "plural form of priest",
"prig": "a person who displays or demands of others pointlessly precise conformity",
"priggish": "acting like a prig",
"priggishness": "the quality of being priggish",
"priggism": "the quality or state of being a prig",
"priggy": ["priggish", "conceited or pedantic"],
"prilep": "a city in North Macedonia",
"prill": ["a small aggregate or globule of a material", "a pellet or solid globule of a substance formed by the congealing of a liquid during an industrial process"],
"prilled": "converted (a material) into a granular free-flowing form",
"prilling": "the process of creating a prill",
"prim": ["stiffly formal and precise", "neat and trim"],
"primacy": ["the state of being first in order", "the office or position of a primate"],
"prima donna": ["a principal female singer in an opera", "a vain or temperamental person"],
"prima donna assoluta": "a prima donna of the highest rank, specifically one who is undisputed leader of a company",
"prima donnaish": ["behaving like a prima donna", "temperamental", "self-important"],
"prima donna v": "to act in a temperamental or demanding manner",
"prima facie": ["based on the first impression", "accepted as correct until proved otherwise", "at first sight"],
"prima facie case": "evidence that is sufficient to raise a presumption of fact or establish a fact unless rebutted",
"prima fronte": "at first sight; on the face of it",
"primage": ["a payment to the master of a ship for loading", "an extra charge on freight"],
"primal": ["essential", "fundamental", "first in time"],
"primal scene": ["a child's observation of parental intercourse", "a traumatic childhood experience"],
"primal scream": ["a loud, involuntary shriek used in psychotherapy to release repressed trauma"],
"primary": ["first in importance", "earliest in time", "primary school"],
"primary accent": "the strongest stress on a syllable in a word",
"primary care": ["health care provided by a medical professional", "basic, non-specialized health services"],
"primary color": ["a color that cannot be created by mixing others", "red, yellow, blue"],
"primary election": ["a preliminary election to appoint delegates", "a party nomination vote"],
"primary school": "a school for young children, usually from ages 5 to 11",
"prime": ["the highest level or stage", "a prime number", "most important"],
"prime minister": "the head of government in some countries",
"primitive": ["belonging to the first ages", "very simple or basic"],
"prince": "the son of a king or queen",
"princess": "the daughter of a king or queen",
"principal": ["the person in charge of a school", "main or most important"],
"principle": "a basic truth or rule",
"print": ["to produce letters or images on paper", "a mark left by pressing"],
"prior": "existing or coming before in time",
"prison": "a place where people are kept as punishment",
"privacy": "the state of being away from public view",
"private": ["for a particular person or group", "not public"],
"prize": "something won in a contest",
"probable": "likely to happen or be true",
"problem": "a question or situation that needs to be solved",
"proceed": "to go forward or continue",
"process": "a series of actions done to make something",
"produce": "to make or create something",
"product": "something that is made or grown",
"production": "the act of making or growing something",
"profession": "a job that requires special training",
"professor": "a teacher at a college or university",
"profile": ["a side view of a face", "a short description of someone"],
"profit": "money made from selling something",
"program": ["a plan of things to do", "a television show", "instructions for a computer"],
"progress": "moving forward to a higher or better state",
"project": "a planned task or activity",
"promise": "a statement that you will do something",
"promote": ["to help something grow or succeed", "to move to a higher job"],
"pronounce": "to make the sound of a word",
"proof": "something that shows something is true",
"proper": "right or correct for a situation",
"property": ["something that is owned", "a quality of a thing"],
"proportion": "the size or amount of a part compared to the whole",
"propose": "to suggest a plan",
"protect": "to keep safe from harm",
"protein": "a substance in food needed for growth",
"proud": ["feeling good about something you did", "having high self-respect"],
"prove": "to show that something is true",
"provide": "to give something needed",
"public": "open to everyone",
"publish": "to make a book or magazine available",
"pull": "to use force to move something toward you",
"pump": "a machine for moving liquids or gases",
"punch": ["to hit with a fist", "a hole made in paper"],
"punctual": "on time",
"punctuation": "marks used in writing to separate sentences",
"punish": "to make someone suffer for doing wrong",
"pupil": ["a student", "the black center of the eye"],
"purchase": "to buy something",
"pure": "not mixed with anything else",
"purple": "a color between red and blue",
"purpose": "the reason for doing something",
"purse": "a small bag for money",
"pursue": "to follow or chase",
"push": "to use force to move something away",
"put": "to place something in a position",
"putamen": "the outer part of the lentiform nucleus in the brain",
"putamina": "plural of putamen",
"putangitangi": "the paradise duck of New Zealand",
"putative": ["commonly accepted", "supposed", "reputed"],
"putative marriage": "a marriage considered valid by one or both parties but which is legally null",
"putcheon": "a type of pottery kiln",
"putcher": "a basket for catching salmon",
"putea": "plural of puteal",
"puteal": "a curb or covering for a well",
"puteli": "a small boat used on the Ganges",
"putid": ["decayed", "rotten", "base"],
"putin": "a small fish",
"putlog": "a horizontal cross-piece supporting a scaffold",
"putman": "variant of putlog",
"putoff": "an excuse or evasion",
"putonghua": "the standard language of the People's Republic of China",
"putout": ["a dismissal in baseball", "something published or produced"],
"putrajaya": "the administrative center of Malaysia",
"putrefaction": "the process of decay or rotting in a body or other organic matter",
"putrefactive": "causing or relating to putrefaction",
"putrefiable": "liable to rot or decompose",
"putrefy": ["to cause to decay", "to rot"],
"putrescence": "the state of being putrescent",
"putrescent": "rotting",
"putrescine": "a toxic base produced by decaying flesh",
"putrescible": "capable of decomposing",
"putrid": ["decaying", "rotten", "smelly"],
"putsch": "a plotted revolt or coup",
"putt": ["a gentle strike of a golf ball", "to hit a ball gently"],
"puttee": "a strip of cloth wrapped around the leg",
"putter": ["a golf club", "to move or act aimlessly"],
"putting": "the action of hitting a golf ball or placing a shot",
"putty": ["a dough-like mixture of whiting and linseed oil used to fix glass panes or fill cracks", "a soft, pliable material", "a light brownish-gray color","a paste used for sealing glass", "to fill with putty"],
"putty in someone's hands": "a person who is easily influenced or manipulated",
"putty knife": "a spatula used to apply putty",
"putty powder": "a powder, such as tin oxide, used for polishing metal or glass",
"puttying": "the act of applying putty",
"puttylike": "resembling putty in texture or consistency",
"puttyroot": "an orchid with large leaves that appear in autumn",
"putumayo": "a department in southern Colombia",
"puture": "an ancient customary right to demand food and lodging",
"putz": "to fix, mend, or fool around",
"puva": "a type of light therapy used to treat skin conditions",
'puvis de chavannes' : 'Pierre Cécile (1824–98), French mural painter' ,
'puy' : 'a small volcanic cone or hill, particularly in the Auvergne region of France' ,
'puy de dôme' : 'a large lava dome in the Chaîne des Puys volcanic region in central France' ,
'puy de sancy' : 'the highest mountain in the Massif Central of France' ,
'puy lentil' : 'a small dark green lentil from the Auvergne region of France' ,
'puyallup' : 'a city in Washington state, USA, known for its annual agricultural fair' ,
'puyi' : 'the final emperor of China, reigning from 1908 to 1912' ,
'puzzel' : 'archaic or alternative spelling of puzzle' ,
'puzzle' : [ 'a game, toy, or problem designed to test ingenuity or knowledge' , 'to bewilder or confuse' ] ,
'puzzle box' : 'a box requiring a hidden mechanism to open' ,
'puzzle jug' : 'a type of ceramic jug with a perforated neck and a trick spout' ,
'puzzle out' : 'to solve or understand something through careful thought' ,
'puzzled' : 'feeling or showing confusion or bewilderment' ,
'puzzleheaded' : 'confused, muddled, or unable to think clearly' ,
'puzzlement' : 'a state of confusion or bewilderment' ,
'puzzler' : 'a person who is confused, or a difficult question' ,
'puzzling' : 'difficult to understand or explain' ,
'puzzolana' : 'a volcanic ash or artificial substance that sets under water',
"puzzolan" : ["Alternative form of pozzolana", "A type of volcanic ash used for mortar or for cement which sets under water"],
"puzzolana" : "A variant of pozzuolana [A porous variety of volcanic tuff or ash used in making hydraulic cement]",
"puzzolano" : "A type of volcanic ash [Similar to pozzolana]",
"pv" : ["photovoltaic", "personally valuable", "present value"],
"pv cell" : "A cell that converts light directly into electricity",
"pva" : "Polyvinyl alcohol or Polyvinyl acetate",
"pvc" : "Polyvinyl chloride",
"pwt" : "pennyweight",
"px" : "please exchange [military slang]",
"pxt" : "pinxit [he/she painted it]",
"py": ["A combining form used like a prefix meaning “pus.”", "A variant of pyo- before a vowel.", "A monetary unit of Myanmar, equal to 1/100 of a kyat."],
"py-": "Combining form meaning pus",
"pya": ["A monetary unit of Myanmar worth one hundredth of a kyat", "An aluminum coin of Myanmar (Burma), the 100th part of a kyat"],
"pyaemia": ["Variant of pyaemia", "Condition of having pus in the blood"],
"pyal": ["A combining form meaning pus", "A person who is lazy"],
"pycn": ["Combining form meaning thick, dense, or compact"],
"pycno-": ["Combining form meaning thick or dense"],
"pycnometer": "A device used to measure the density of a liquid",
"pyelitis": "Inflammation of the pelvis of the kidney",
"pyelogram": "An X-ray of the kidney and ureter",
"pyemia": "Pyaemia; blood poisoning by pus-forming bacteria",
"pygarg": "A type of antelope",
"pygmy": ["A person of very small stature", "A small animal or plant"],
"pyjama": ["A loose-fitting garment for sleeping", "A two-piece suit for lounging"],
"pylon": "A tall structure used for supporting electrical cables or as a marker",
"pyo-": "Combining form meaning pus",
"pyoid": "Resembling or having the nature of pus",
"pyramid": ["A monumental structure with a square or triangular base and sloping sides", "A figure with a triangular base and sloping sides"],
"pyre": "A heap of combustible material, especially one for burning a corpse",
"pyrexia": "Fever; an elevation of body temperature",
"pyrites": "A brass-yellow mineral, iron disulfide",
"pyrogen": "A substance that produces fever",
"pyrology": "The study of fire",
"pyrolysis": "The decomposition of materials by heat",
"pyromania": "An obsessive desire to set fire to things",
"pyrotechnic": ["Relating to fireworks", "A spectacular display"],
"pyrotechnical": "of or relating to fireworks or the art of making them",
"pyrotechnically": "in a manner relating to fireworks or brilliant displays",
"pyrotechnician": ["a person skilled in the art of making or discharging fireworks", "a person who operates pyrotechnic devices"],
"pyrotechnics": ["the art or science of making or using fireworks", "a display of fireworks", "a brilliant or sensational display, as of rhetoric or musicianship"],
"pyrotechnist": "a person skilled in pyrotechnics",
"pyrotechny": ["the art of making fireworks", "the art of using fire for producing flashes, smoke, or brilliant effects", "a display of fireworks"],
"pyrotherapy": "the treatment of disease by raising the body temperature",
"pyrothonide": "a substance produced by the distillation of organic materials, formerly used for its cauterizing properties",
"pyrotic": "a substance that causes burns; caustic",
"pyrrhic": ["a victory won at too great a cost to have been worthwhile", "a metrical foot consisting of two short syllables"],
"pyrrhonic": ["skeptical", "relating to the ancient Greek philosopher Pyrrho or his philosophy of skepticism"],
"pyrrhonism": ["the skepticism of Pyrrho", "complete and total doubt"],
"pyrrhonist": "a person who practices the skepticism of Pyrrho",
'pyrrhonistic': 'adjective. Relating to or characteristic of the Greek philosopher Pyrrho\'s teachings on scepticism, especially the suspension of judgment in the pursuit of wisdom and happiness.',
'pyrrhotine': 'A mineral, magnetic pyrites.',
'pyrrhula': 'A genus of birds including the bullfinches.',
'pythia': 'The priestess of Apollo at Delphi who transmitted the oracles.',
'pythian': 'Relating to Delphi, the priestess Pythia, or the Pythian games.',
'pythiad': 'The interval of time between the Pythian Games of Ancient Greece: either four or eight years, depending on the historical period.',
'python': 'A large, nonvenomous snake that kills by constriction.',
'pythoness': 'The priestess of Apollo at Delphi; a woman who delivers oracles or foretells the future.',
'pythonic': 'Relating to a python or pythoness; prophetic, oracular.',
'pythonism': 'The art of predicting events after the manner of the priestess of Apollo at Delphi; equivocal prophesying.',
'pythonist': 'A person who predicts events, a fortune teller.',
'pythium': 'A genus of parasitic water molds that cause root rot.',
"pythogenic": "originating from putrefaction or decay",
"python": ["a large nonvenomous snake", "a person who has a soothsaying spirit", "a high-level programming language"],
"pythonesque": "suggestive of or reminiscent of the style of the comedy troupe Monty Python",
"pythoness": ["a woman believed to be possessed by a soothsaying spirit", "a female soothsayer or prophetess"],
"pythonic": "of or relating to a python",
"pythonist": "a person who practices pythoness-like divination",
"pythonomorpha": "a suborder of fossil reptiles resembling both snakes and lizards",
"pythons": "plural of python",
"pythura": "a genus of snakes",
"pyuria": "the presence of pus in the urine",
"pyx" : ["a container for the reserved host", "a box used in a mint for deposit of sample coins"],
"pyxidate" : ["Having a capsule that opens by a lid","having the form of a box"],
"pyxidicula" : "a small box or pyxis",
"pyxidium" : ["a seed capsule that splits open so that the top comes off like the lid of a box""A dehiscent, dry fruit whose upper portion splits off as a lid"],
"pyxie" : "a creeping evergreen plant native to the eastern U.S.",
"pyxis" : ["a small box or case", "a seed capsule that opens transversely"],
"pyxos" : "the boxwood",
"pyx chest" : "A chest in a mint in which specimen coins are placed to await assay",
"pyxes" : "Plural form of pyx",
"pyxidanthera" : "A genus of trailing evergreen shrubs",
"pyxides" : "Plural form of pyxis",
"pyxidia" : "Plural form of pyxidium",
"pyxidium" : "the dry fruit of such plants as the plantain: a capsule whose upper part falls off when mature so that the seeds are released",
"pyxie" : "a small, trailing evergreen shrub (Pyxidanthera barbulata) of the pine barrens of New Jersey",
"pyxis" : [ "a small box or casket, especially one used in classical antiquity", "a capsule whose lid falls off in one piece, as in the plantain", "a small box for the consecrated host" ],
"pyxis (constellation)" : "a small constellation in the southern sky, known as the Mariner's Compass",
"pyy" : "a peptide tyrosine tyrosine, a peptide found in the gastrointestinal tract and brain",
"pyzhik" : "a young reindeer, or the fur from such an animal",
"qadi" : "a judge in a Muslim court",
"qaeda" : "a radical Sunni Muslim organization dedicated to the elimination of a Western presence in Arab countries",
"qat" : "a shrub, Catha edulis, of Arabia and North Africa, whose leaves are chewed or used as a tea for their stimulant effects",
"qats": ["plural of qat", "leaves of an Arabian shrub used as a stimulant"],
"qatabanian": "of or relating to an ancient South Arabian kingdom",
"qatari": "a native or inhabitant of Qatar",
"qataris": "plural of qatari",
"qatsiecc": "a term related to the concept of koyaanisqatsi",
"qatsip": "a variant spelling in some databases related to qats",
"qau": ["4-letter words", "qaur", "tqau", "wqau"],
"qaid": "a local chieftain or magistrate in Muslim countries",
"qaimaqam": "a deputy governor in the Ottoman Empire",
"qanat": "a system of underground tunnels for irrigation",
"qapik": "a monetary unit of Azerbaijan",
"qasida": "an Arabic panegyric poem",
"qawwali": "a form of Sufi devotional music",
"qazi": "a Muslim judge who interprets Sharia law",
"qindar": "an Albanian monetary unit",
"qintar": "a variant of qindar",
"qiviut": "the wool of the musk ox",
"qoph": "the nineteenth letter of the Hebrew alphabet",
"qwerty": "the standard layout of English-language typewriters",
"qintar": ["a unit of currency in Albania", "1/100 of a lek"],
"qua": "in the capacity of",
"suq": "a marketplace",
'tranq' : ['short for tranquilizer', 'the street name of the sedative drug xylazine', 'to tranquilize a person or an animal'],
'tranq dope' : 'a combination drug created when the veterinary sedative, xylazine, is mixed with fentanyl',
'tranquil' : ['free from commotion or disturbance', 'calm', 'quiet'],
'tranquilize' : ['to make calm, serene, or tranquil', 'to depress the central nervous system of', 'to render unconscious or sleepy with a drug'],
'tranquilizer' : ['a drug that lowers anxiety and induces calmness', 'a medicinal agent used to reduce tension or fear'],
'tranquillity' : 'the quality or state of being tranquil',
'transact' : ['to carry on business', 'to manage or conduct', 'to prosecute negotiations'],
'transcend' : ['to rise above or go beyond the normal limits of', 'to outdo or exceed in intensity or power'],
'transcription' : ['the act of writing down or converting spoken words into text', 'the process of transferring data'],
'tranqns' : 'plural of the informal word tranqn, a variant of tranquilizer',
'tranqed' : 'past tense of the verb tranq, meaning having been sedated',
'tranqing' : 'present participle of tranq: the act of administering a sedative or tranquilizer, typically from a distance',
'tranquil' : [ 'free from disturbance; calm', 'quiet; peaceful; serene' , 'unruffled; placid; restful' , 'not agitated or disturbed' ] ,
'tranquilised' : 'variant of tranquilized; calmed or sedated using a tranquilizer',
'tranquiliser' : 'a drug that reduces anxiety, tension, or inhibition; a sedative',
'tranquilises' : 'third-person singular present of tranquilise: to make calm or quiet',
'tranquility' : [ 'the quality or state of being tranquil; calm' , 'freedom from disturbance or turmoil' ] ,
"transactinide": "any of the chemical elements with atomic numbers greater than 89",
"transaction": [
    "the act of transacting or the fact of being transacted",
    "an instance or process of transacting something",
    "a business agreement or exchange",
    "the published records of the proceedings of a learned society"
],
"transactional": "of or relating to the act of conducting business",
"transaction cost": "a cost incurred in making an economic exchange",
"transaction details": "specific information regarding a business deal or financial exchange",
"transaction fee": "a sum of money charged to allowed a specific, typically financial, action",
"transaction processing": "the gathering and preparation of raw materials or data in a business context",
"transaction report": "a document showing a record of a completed transaction",
"transaction tax": "a tax applied to specific transactions rather than assets or income",
"transact": "to carry on or conduct business, negotiations, or activities",
"transalpine": "situated on the other side of the Alps, typically from an Italian perspective",
"transatlantic": "crossing the Atlantic Ocean; situated beyond the Atlantic",
"transceiver": "a device that can both transmit and receive communications",
"transcend": "to go beyond the limits of; exceed or surpass",
"transcendent": "surpassing all others; superior; existing apart from the material world",
"transcendental": "relating to a spiritual realm; in philosophy, beyond empirical experience",
"transconductance": "the electrical characteristic relating the current in one electrode to the voltage on another",
"transcribe": "to write or type out a copy of; to arrange music for a different instrument",
"transcript": "an official written or printed copy of words, usually spoken",
"transcription": "the process of making a written or printed copy of something"
'trans' : [ 'a prefix meaning across, beyond, or through' , 'informal: a transgender person' ] ,
"transact": "conduct business",
"transaction": ["conducting business within or between groups", "an instance of buying or selling"],
"transalpine": "situated beyond the Alps",
"transatlantic": "spanning or crossing the Atlantic Ocean",
"transcalent": "allowing heat to pass through",
"transcend": ["to rise above or go beyond limits", "to exceed"],
"transcontinental": "spanning one of the large landmasses of the earth",
"transcribe": ["to write or type in full", "to translate or change format"],
"transduct": "to convert energy from one form to another",
"transect": ["to cut across or divide", "a cross section"],
"transept": "the part of a church that crosses the nave",
"transfat": ["an unsaturated fatty acid partially hydrogenated", "used in foods to increase shelf life"],
"transfer": ["move from one place to another", "carry across"],
"transfix": "render motionless because of surprise, terror, or awe",
"transform": ["to change in form or shape or appearance", "a qualitative change"],
"transfusion": ["transfer of blood or other fluids into a vein", "a giving or imparting"],
"transgress": ["to violate a law or a duty or moral principle", "to go beyond a boundary"],
"transience": ["the state of lasting a very short time", "constantly changing"],
"transit": ["a going across", "a passage or journey", "to move through"],
"transitory": "lasting a very short time",
"translate": ["rendering in another language with the same meaning", "carrying across"],
"transliterate": "to represent letters or words in another alphabet",
"translucent": "allowing light to pass through diffusely",
"transmit": ["send from one person or place to another", "to pass on"],
"transmogrify": "to change thoroughly, especially in a funny or shocking way",
"transmute": ["to change from one form or state to another", "alter physical nature"],
"transparent": ["able to be seen through with clarity", "obvious"],
"transpire": ["to come about, happen, or occur", "to give off vapor"],
"transplant": ["to move from one place to another", "to replant", "to graft tissue"],
"transport": ["to carry or move from one place to another", "a means of carriage"],
"transpose": "to change the relative order of things",
"transsexual": "a person who has undergone or is undergoing sex reassignment",
"transude": "to pass through a membrane, often regarding fluids",
"transvestite": "a person who wears clothes associated with the opposite sex",
"transverse": "extending or lying across",
"trave": "a beam",
"travesty": "an absurd or crude representation of something",
"travestied": "disguised, burlesqued, or parodied",
"travesties": ["plural of travesty", "grotesque or debased likenesses or imitations"],
"travestying": "making a travesty of",
"travis": "a male given name",
"travois": "a type of sled formerly used by Plains Indians, consisting of two trailing poles",
"trawl": ["to fish with a net that is dragged along the sea bottom", "to search through something"],
"trawler": "a fishing boat that uses a trawl net",
"trawl line": "a long fishing line with many hooks",
"tray": ["an open receptacle with a flat bottom and low sides", "a flat surface for holding items"],
"tray agriculture": "a method of growing plants in shallow trays",
"tray table": "a small table designed for holding a tray",
"trayf": "non-kosher food",
"trazodone": "an antidepressant drug",
"treacle": ["a British term for molasses", "cloying sentimentality"],
"tread": ["to walk on, in, or along", "the top surface of a step", "the part of a tire that touches the ground"],
"tread a measure": "to dance",
"tread carefully": ["to proceed with delicacy or tact", "to take care to avoid mistakes"],
"treadboard": "a board that forms the tread of a stair",
"treaded": "provided with a tread",
"treading": ["the act of walking or stepping", "the act of pressing with the feet"],
"treadle": "a lever pressed by the foot to drive a machine",
"treadless": "having no tread",
"treadmill": ["a device used for threshing or pumping, operated by a person or animal walking on a moving belt", "a monotonous or tedious routine"],
"treads": ["plural form of tread", "third-person singular present tense of tread"],
"treadwheel": "a wheel turned by the weight of people or animals treading on steps around its edge",
"treason": ["the crime of betraying one's country", "the betrayal of a trust or confidence"],
"treasonable": "involving or guilty of treason",
"treasonous": "having the character of treason",
"treasonously": "in a manner involving betrayal of one's country or trust",
"treasonousness": "the quality or state of being treasonous",
"treasonist": ["a person who commits treason", "a traitor"],
"treasure": ["wealth in the form of money, jewels, or precious metals", "a highly valued person or thing"],
"treasurer": "a person appointed to administer or manage the financial assets of a group",
"treasury": ["a place where treasure is kept", "the funds or revenue of a government or institution"],
"treat": ["to behave toward or deal with in a certain way", "to provide food, drink, or entertainment at one's own expense"],
"treatise": "a written work dealing formally and systematically with a subject",
"treatment": ["the manner in which someone or something is dealt with", "medical care given to a patient for an illness or injury"],
"treaty": "a formally concluded and ratified agreement between countries",
"treble": ["multiplied by three", "having three parts", "a high-pitched voice or sound"]
"trebled": "multiplied by three; increased threefold",
"trebles": ["the highest part in musical composition", "plural of treble"],
"treblet": "a small treble part or item",
"trebling": "the act of increasing threefold",
"trebly": "in a threefold manner; three times",
"trebuchet": "a medieval siege engine for hurling heavy stones",
"trecentist": "an artist or writer of the 14th century (Italian trecento)",
"trecento": "the 14th century in Italian art and literature",
"tredecillion": "the number represented as one followed by 42 zeros",
"tree": ["a woody perennial plant", "a graph data structure with no cycles"],
"treed": "surrounded or caught by trees; driven up a tree",
"treehopper": "a hemipterous insect known for jumping",
"treeing": "driving a hunted animal up a tree",
"treeless": "lacking trees",
"treelike": "resembling a tree in shape or structure",
"treen": "items made of wood",
"treenail": "a wooden pin used for fastening timber",
"treetops": "the topmost branches of trees",
"treeware": "a document or publication printed on paper",
"treewax": "a wax secreted by certain trees",
"tref": ["not kosher", "unfit to eat according to Jewish dietary laws"],
"trefla": "variation of tref",
"trefah": "alternative spelling of tref",
"trefoil": ["a plant of the pea family with three-lobed leaves", "an ornamental tracery design with three lobes"],
"tregetour": "a magician or juggler in medieval literature",
"treggings": "a hybrid garment combining trousers and leggings",
"trehala": "a sugary substance produced by a beetle larva",
"trehalose": "a sugar found in fungi and bacteria",
"treillage": "a trellis or lattice framework for supporting vines",
"trek": ["a long arduous journey", "to travel slowly or with difficulty"],
"trekked": "past tense of trek",
"trekker": "a person who takes part in a long, difficult journey",
"trellis": "a framework of light wooden or metal bars used as a support for fruit trees or climbing plants",
"trellised": "provided with or supported by a trellis",
"trema": "a small evergreen tree of the tropics",
"trematode": "a parasitic flatworm",
"tremble": ["to shake involuntarily", "a quivering motion"],
"tremendous": "very great in amount, scale, or intensity",
"tremolo": "a wavering effect in a musical sound",
"tremor": "an involuntary quivering movement",
"tremors": ["plural form of tremor", "uncontrollable shakiness of the body"],
"tremulant": ["quivering or shaking", "a tremolo stop on an organ"],
"tremulate": "to tremble or quiver",
"tremulous": ["characterized by trembling, as from fear, nervousness, or weakness", "timid or fearful", "vibratory or shaking"],
"tremulously": "in a trembling or shaky manner",
"tremulousness": "the quality or state of being tremulous",
"trenail": "a wooden peg used to fasten timbers or planks",
"trench": ["a long, narrow ditch", "a deep furrow in the ground"],
"trenchancy": "the quality of being sharp, keen, or incisive",
"trenchant": ["keen, sharp, or incisive", "forceful and effective"],
"trenchcoat": "a waterproofed, loose-fitting double-breasted raincoat",
'trenchancy' : 'The quality or state of being trenchant, or forceful and clear',
'trenchant' : ['Having a sharp edge; keen', 'Sharply perceptive; penetrating', 'Forceful and effective in expressing ideas'],
'trencher' : ['A wooden platter for serving food', 'One who trenches or cuts'],
'trencherman' : 'A person with a specified manner of eating, often a large eater',
'trend' : ['A general direction in which something is developing or changing', 'A fashion or style'],
'trendsetter' : 'A person who leads the way in fashion or ideas',
'trendy' : 'Very fashionable or up to date',
'trepan' : 'A saw used by surgeons for removing a circular disk of bone from the skull',
"trepanning" : ["the action or process of perforating the skull with a trepan", "an early form of surgical cranial surgery"],
"trepanning-elevator" : "a surgical instrument used in the process of trepanning",
"trepan saw" : "a saw designed for cutting circular holes in the skull",
"trephination" : ["the surgical procedure in which a hole is drilled in the skull and a circular piece of bone removed", "the act of boring a hole in the skull to relieve pressure"],
"trephine" : ["a surgical instrument with a cylindrical blade used to remove a circular section of tissue", "to drill a hole in the skull using a trephine"],
"trephined" : "of or relating to a skull that has been operated on with a trephine",
"trephiner" : "one who performs the operation of trephining",
"trephining" : "the act or process of using a trephine to create a hole in the skull",
"trepid" : "fearful, nervous, or trembling",
"trepidancy" : "a state of alarm, nervousness, or trepidation",
"trepidant" : "trembling, fearful, or hesitant",
"trepidation" : ["nervous fear or anxiety", "a tremulous motion"],
"tres" : "the Spanish word for the number three, sometimes used in specialized vocabularies",
"trespass" : ["a violation of law or moral duty", "to enter another's land without permission"],
"trespassed" : "past tense of trespass; to have entered land unlawfully",
"trespasser" : "one who goes upon the premises of another without permission",
"trespassing" : "the act of entering land unlawfully or violating a moral duty",
"tress": "a lock of hair",
"trestle": ["a braced framework", "a sawhorse"],
"trestle bridge": "a bridge composed of a series of short spans supported by trusses",
"trestle table": "a table supported by trestles",
"trestlework": "a structure or viaduct made of trestles",
"triad": ["a union of three", "a chord of three tones", "a grouping of three related things"],
"trial": ["a formal examination of evidence in a court of law", "a test of performance", "a source of annoyance"],
"triangle": ["a polygon with three angles and three sides", "a musical instrument", "a set of three people or things"],
"tribe": ["a social division in a traditional society", "a large group of people with a common interest"],
"tribulation": ["a state of great trouble", "a severe affliction"],
"tribromomethane": "a colorless liquid haloform, CHBr3, used in synthesis and as a solvent",
"tribulate": "to oppress or afflict",
"tribulation": [
    "great trouble or suffering",
    "a trying experience"
],
"tribunal": [
    "a court or forum of justice",
    "a seat or bench for a judge or magistrate",
    "a committee appointed to adjudicate in a particular matter"
],
"tribute": [
    "a gift, testimonial, or compliment given as due or deserved",
    "a tax or imposition paid by one state to another in acknowledgment of submission",
    "evidence or sign of something"
],
"trice": "a very short time; an instant",
"trick": [
    "(N) a cunning or skillful act intended to deceive or amuse",
    "(N) an effective method or technique for achieving something",
    "(V) to deceive or outwit someone"
],
"trickle": "(V) to flow or fall in a thin, slow stream",
"trickle-down": "(ADJ) relating to the idea that benefits provided to the wealthy or powerful will eventually benefit others indirectly",
"tricky": [
    "(ADJ) requiring care or skill because it is difficult or awkward",
    "(ADJ) likely to deceive or outsmart"
],
"tricolor": "(ADJ) having three colors",
"tricycle": "(N) a vehicle with three wheels, typically ridden by young children",
"trident": "(N) a three-pronged spear",
"trifle": [
    "(N) something of little value or importance",
    "(V) to treat someone or something without seriousness or respect"
],
"trifling": "(ADJ) trivial or unimportant",
"trigger": [
    "(N) a small device that releases a mechanism, especially on a firearm",
    "(V) to cause something to begin or happen suddenly"
],
"trill": [
    "(N) a rapid alternation between two adjacent musical notes",
    "(V) to produce a quavering or warbling sound"
],
"trilogy": "(N) a series of three related works, usually books or films",
"trim": [
    "(V) to cut away excess to make neat or tidy",
    "(ADJ) neat and well-proportioned",
    "(N) decorative additions or edging"
],
"trimmer": "(N) a tool used for cutting or shaping something, especially hair or plants",
"trinket": "(N) a small ornament or item of little monetary value",
"trio": "(N) a group of three people or things",
"trip": [
    "(N) a journey or excursion",
    "(V) to stumble or lose balance",
    "(V) to cause someone to fall by catching their foot"
],
"tripe": "(N) the edible stomach lining of certain animals",
"triple": [
    "(ADJ) consisting of three parts or elements",
    "(V) to increase something threefold"
],
"triplet": "(N) one of three children or animals born at the same time",
"triumph": [
    "(N) a great victory or achievement",
    "(V) to achieve victory or success"
],
"triumphant": "(ADJ) feeling or expressing joy after a victory",
"trivet": "(N) a small metal stand used to support hot dishes",
"trivial": "(ADJ) of little value or importance",
"trivia": "(N) details or information that are considered unimportant",
"troll": [
    "(N) a mythical creature often depicted as large and ugly",
    "(V) to deliberately provoke or annoy others online"
],
"trolley": "(N) a wheeled cart used for transporting items",
"trombone": "(N) a brass musical instrument with a sliding tube",
"troop": [
    "(N) a group of soldiers",
    "(V) to move or march as a group"
],
"trophy": "(N) an award given as a symbol of victory or achievement",
"tropic": "(N) either of the two lines of latitude marking the northernmost and southernmost points of the sun’s direct rays",
"tropical": "(ADJ) relating to or characteristic of the tropics",
"trot": [
    "(V) to move at a pace faster than a walk but slower than a run",
    "(N) a gait between walking and running"
],
"trough": "(N) a long, narrow container used to hold food or water for animals",
"trounce": "(V) to defeat decisively",
"troupe": "(N) a group of performers, especially actors or dancers",
"trousers": "(N) a garment covering the legs from waist to ankles",
"trout": "(N) a freshwater fish commonly found in streams and rivers",
"trowel": "(N) a small hand tool used for digging or spreading mortar",
"truancy": "(N) the act of staying away from school without permission",
"truant": "(N) a student who stays away from school without permission",
"truce": "(N) an agreement to stop fighting for a period of time",
"truck": "(N) a large motor vehicle used for transporting goods",
"truckle": "(V) to act in a subservient or overly obedient way",
"trudge": "(V) to walk slowly and with heavy steps due to exhaustion or harsh conditions",
"true": "(ADJ) in accordance with fact or reality",
"truffle": "(N) an edible fungus highly valued as a delicacy",
"trumpet": [
    "(N) a brass musical instrument with a bright, penetrating tone",
    "(V) to proclaim or announce loudly"
],
"truncate": "(V) to shorten something by cutting off the end",
"trunk": [
    "(N) the main woody stem of a tree",
    "(N) a large, sturdy storage box",
    "(N) the main body of something"
],
"trust": [
    "(N) firm belief in the reliability or truth of someone or something",
    "(V) to rely on or believe in someone or something"
],
"trustee": "(N) a person who holds responsibility for managing property or assets for others",
"trustworthy": "(ADJ) deserving of trust; reliable",
"truth": "(N) the quality or state of being in accordance with fact or reality",
"try": [
    "(V) to attempt to do or accomplish something",
    "(N) an effort or attempt"
],
"tub": "(N) a wide, open container used for washing or storage",
"tuba": "(N) a large brass musical instrument with a deep tone",
"tubby": "(ADJ) slightly fat or plump in a rounded way",
"tube": "(N) a hollow cylinder used to convey or contain something",
"tuck": [
    "(V) to push or fold something into a snug position",
    "(N) a fold or pleat in fabric"
],
"tuft": "(N) a small bunch of hair, feathers, or fibers held together at the base",
"tug": [
    "(V) to pull something sharply or with effort",
    "(N) a strong pull"
],
"tuition": "(N) the fee paid for instruction, especially at a school or college",
"tulip": "(N) a brightly colored spring flower with a cup-shaped bloom",
"tumble": [
    "(V) to fall suddenly and clumsily",
    "(N) a sudden fall"
],
"tummy": "(N) an informal term for the stomach or belly",
"tumor": "(N) an abnormal growth of tissue in the body",
"tune": [
    "(N) a melody or musical composition",
    "(V) to adjust something for proper functioning or harmony"
],
"tunic": "(N) a loose garment, typically reaching to the knees",
"tunnel": "(N) an underground or enclosed passage",
"turban": "(N) a head covering made by winding cloth around the head",
turbine": "(N) a machine in which a wheel or rotor is made to revolve by a fast-moving flow of water, steam, gas, or air",
"turbulent": "(ADJ) characterized by conflict, disorder, or confusion",
"turf": [
    "(N) grass and the surface layer of earth held together by its roots",
    "(N) an area regarded as someone's territory"
],
"turgid": "(ADJ) swollen or distended; also overly complex or pompous in style",
"turkey": "(N) a large bird native to North America, often domesticated for food",
"turmeric": "(N) a yellow spice made from the root of a plant, used in cooking and dyeing",
"turn": [
    "(V) to move or cause to move in a circular direction",
    "(N) an action or opportunity to do something"
],
"turncoat": "(N) a person who switches allegiance or loyalty",
"turnip": "(N) a round root vegetable with white flesh",
"turnout": [
    "(N) the number of people who attend or participate",
    "(N) a place where vehicles can pull off the road"
],
"turnover": [
    "(N) the rate at which employees leave and are replaced",
    "(N) the amount of business done in a given period"
],
"turnstile": "(N) a mechanical gate that allows one person through at a time",
"turquoise": "(N) a blue-green mineral used as a gemstone",
"turret": "(N) a small tower on a building or castle",
"turtle": "(N) a reptile with a bony or leathery shell",
"tusk": "(N) a long, pointed tooth that sticks out of the mouth of certain animals",
"tussle": [
    "(N) a vigorous struggle or scuffle",
    "(V) to engage in a physical or verbal struggle"
],
"tutor": [
    "(N) a private teacher",
    "(V) to teach or instruct individually"
],
"tutu": "(N) a short, stiff skirt worn by ballet dancers",
"tuxedo": "(N) a formal suit for men, typically worn at evening events",
"twang": [
    "(N) a sharp vibrating sound, especially from a plucked string",
    "(V) to produce such a sound"
],
"tweak": [
    "(V) to make a small adjustment",
    "(N) a minor improvement or modification"
],
"tweed": "(N) a rough, woolen fabric, often with a twill weave",
"tweet": [
    "(N) a short message posted on a social media platform",
    "(V) to post such a message"
],
"tweezers": "(N) a small tool used for picking up or pulling out small objects",
"twilight": "(N) the soft light in the sky after sunset or before sunrise",
"twill": "(N) a type of fabric weave with diagonal lines",
"twin": "(N) one of two children or animals born at the same time",
"twine": "(N) strong string made of two or more strands twisted together",
"twirl": [
    "(V) to spin quickly",
    "(N) a quick spinning movement"
],
"twist": [
    "(V) to rotate or bend out of shape",
    "(N) a change in direction or unexpected development"
],
"twister": "(N) a tornado; also a word game involving tongue-twisters",
"twit": "(N) an informal term for a foolish or silly person",
"twitch": [
    "(V) to make a small, sudden movement",
    "(N) a brief, involuntary muscle movement"
],
"twitter": [
    "(N) a series of light, high-pitched sounds",
    "(V) to make such sounds"
],
"twofold": "(ADJ) having two parts; double",
"tycoon": "(N) a wealthy and powerful businessperson",
"tying": "(N) the act of fastening or securing with a knot or tie",
"tyke": "(N) a small child; sometimes a mischievous one",
"tympani": "(N) large kettledrums used in orchestras",
"type": [
    "(N) a category or class of things with common characteristics",
    "(V) to write using a keyboard"
],
"typeface": "(N) a particular design of printed letters and characters",
"typical": "(ADJ) showing the characteristics of a particular type or group",
"typify": "(V) to represent or symbolize something",
"typist": "(N) a person who types, especially as a job",
"typo": "(N) a typographical error",
"typhoon": "(N) a tropical cyclone occurring in the western Pacific",
"tyranny": "(N) cruel or oppressive government or rule",
"tyrant": "(N) a ruler who exercises power in a harsh or oppressive way",
"tyro": "(N) a beginner or novice",
"ubiquitous": "(ADJ) present, appearing, or found everywhere",
"udder": "(N) the mammary gland of female cattle and some other mammals",
"ugly": "(ADJ) unpleasant or unattractive in appearance",
"ulcer": "(N) an open sore on an internal or external surface of the body",
"ulterior": "(ADJ) existing beyond what is openly stated; hidden",
"ultimate": "(ADJ) final or most extreme",
"ultimatum": "(N) a final demand whose rejection may lead to consequences",
"ultra": "(ADJ) extremely; going beyond the usual limits",
"ultrasonic": "(ADJ) relating to sound waves above the range of human hearing",
"ultraviolet": "(ADJ) relating to electromagnetic waves beyond the violet end of the visible spectrum",
"umber": "(N) a natural brown earth pigment",
"umbilical": "(ADJ) relating to the umbilical cord or its function",
"umbrella": "(N) a device used for protection against rain or sunlight",
"umpire": [
    "(N) an official who enforces rules in sports such as baseball or tennis",
    "(V) to act as such an official"
],
"umpteen": "(ADJ) an indefinitely large number of something",
"unabashed": "(ADJ) not embarrassed or ashamed",
"unanimous": "(ADJ) fully in agreement; with no dissent",
"unarmed": "(ADJ) not carrying weapons",
"unaware": "(ADJ) not knowing or conscious of something",
"unbalanced": [
    "(ADJ) not evenly distributed or stable",
    "(ADJ) emotionally unstable"
],
"unbearable": "(ADJ) too painful, unpleasant, or difficult to endure",
"unbecoming": "(ADJ) not fitting or appropriate; improper",
"unbiased": "(ADJ) fair and impartial",
"uncanny": "(ADJ) strange or mysterious in an unsettling way",
"uncertain": "(ADJ) not sure; lacking confidence or clarity",
"uncharted": "(ADJ) not mapped or explored",
"uncle": "(N) the brother of one’s parent or the husband of one’s aunt",
"uncouth": "(ADJ) lacking good manners, refinement, or grace",
"undaunted": "(ADJ) not discouraged by difficulty or danger",
"undeniable": "(ADJ) unquestionably true or certain",
"undergo": "(V) to experience or endure something",
"underlie": "(V) to be the cause or basis of something",
"underline": [
    "(V) to draw a line beneath text",
    "(V) to emphasize or stress something"
],
"underling": "(N) a subordinate or someone of lower rank",
"undermine": "(V) to weaken or damage something gradually",
"underpass": "(N) a road or walkway that passes beneath another road",
"underpin": "(V) to support or strengthen the foundation of something",
"underscore": [
    "(V) to emphasize",
    "(N) a line drawn beneath text"
],
"understand": "(V) to grasp the meaning or significance of something",
"understudy": "(N) an actor who learns another’s role to serve as a substitute",
"undulate": "(V) to move with a smooth, wave-like motion",
"unduly": "(ADV) to an excessive or unwarranted degree",
"uneasy": "(ADJ) feeling anxious, worried, or uncomfortable",
"unearth": "(V) to dig up or discover something hidden",
"unequal": "(ADJ) not the same in quantity, size, or value",
"unequivocal": "(ADJ) leaving no doubt; unambiguous",
"unethical": "(ADJ) not morally correct",
"uneven": "(ADJ) not level, smooth, or equal",
"unexpected": "(ADJ) not anticipated or predicted",
"unfailing": "(ADJ) reliable; always effective",
"unfair": "(ADJ) not just or impartial",
"unfathomable": "(ADJ) impossible to understand or measure fully",
"unfeeling": "(ADJ) lacking emotion or sympathy",
"unfit": "(ADJ) not suitable or not in good physical condition",
"unfold": [
    "(V) to open or spread out something folded",
    "(V) to reveal or develop over time"
],
"unforeseen": "(ADJ) not predicted or anticipated",
"unfortunate": "(ADJ) unlucky or regrettable",
"unfurl": "(V) to spread out or open something that was rolled or folded",
"ungainly": "(ADJ) awkward or clumsy in movement",
"ungodly": [
    "(ADJ) wicked or immoral",
    "(ADJ) extremely unreasonable (as in time or amount)"
],
"ungrateful": "(ADJ) not showing appreciation or thanks",
"unguarded": "(ADJ) unprotected; also candid or without caution",
"unharmed": "(ADJ) not injured or damaged",
"unhealthy": "(ADJ) not in good health; harmful",
"unheard": "(ADJ) not listened to or not known about",
"unhinged": "(ADJ) mentally unstable or disturbed",
"unholy": "(ADJ) wicked or shocking; also not sacred",
"unicorn": "(N) a mythical horse-like creature with a single horn",
"unify": "(V) to bring together or make into a whole",
"union": [
    "(N) the act of joining together",
    "(N) an organization formed by workers to protect their rights"
],
"unique": "(ADJ) being the only one of its kind; unlike anything else",
"unison": "(N) simultaneous performance or utterance of action or speech",
"unit": "(N) a single, complete thing that is part of a larger whole",
"unite": "(V) to come together for a common purpose",
"unity": "(N) the state of being joined or united as a whole",
"universal": "(ADJ) applicable to all cases; widespread",
"universe": "(N) all existing matter, space, and energy as a whole",
"university": "(N) an institution of higher learning offering degrees",
"unjust": "(ADJ) not based on fairness or justice",
"unkempt": "(ADJ) messy or untidy in appearance",
"unknown": "(ADJ) not known or familiar",
"unlawful": "(ADJ) not permitted by law",
"unleash": "(V) to release or set free something powerful",
"unlikely": "(ADJ) not expected to happen; improbable",
"unload": "(V) to remove cargo or burdens from something",
"unlock": "(V) to open or release by removing a lock",
"unlucky": "(ADJ) having or bringing bad luck",
"unmistakable": "(ADJ) clear; impossible to confuse with something else",
"unnatural": "(ADJ) contrary to what is normal or expected",
"unnecessary": "(ADJ) not needed or required",
"unnerve": "(V) to make someone lose courage or confidence",
"unnoticed": "(ADJ) not seen or observed",
"unpack": "(V) to remove items from a container or suitcase",
"unpleasant": "(ADJ) causing discomfort or annoyance",
"unpopular": "(ADJ) not liked by many people",
"unravel": [
    "(V) to untangle or separate threads",
    "(V) to solve or explain something complicated"
],
"unreal": "(ADJ) strange or fantastic; not resembling reality",
"unrest": "(N) a state of dissatisfaction or disturbance",
"unruly": "(ADJ) difficult to control; disorderly",
"unsafe": "(ADJ) not secure or free from danger",
"unsaid": "(ADJ) not spoken aloud though implied or understood",
"unsavory": "(ADJ) unpleasant, disagreeable, or morally questionable",
"unscathed": "(ADJ) unharmed or undamaged",
"unseen": "(ADJ) not seen or noticed",
"unsettle": "(V) to disturb or make anxious",
"unshaken": "(ADJ) firm and unwavering; not disturbed",
"unskilled": "(ADJ) lacking special training or ability",
"unsound": [
    "(ADJ) not based on reliable reasoning",
    "(ADJ) in poor physical condition"
],
"unstable": "(ADJ) prone to change or collapse; not steady",
"unsteady": "(ADJ) shaky or not firm",
"unstoppable": "(ADJ) impossible to prevent or halt",
"unsung": "(ADJ) not celebrated or praised despite deserving recognition",
"unsure": "(ADJ) lacking confidence or certainty",
"untamed": "(ADJ) wild; not domesticated or controlled",
"untangle": "(V) to free something from knots or complications",
"untenable": "(ADJ) not able to be defended or justified",
"untidy": "(ADJ) messy or not neat",
"untie": "(V) to loosen or undo a knot",
"until": "(PREP) up to the time or point that something happens",
"untimely": "(ADJ) occurring at an unsuitable or premature time",
"untold": "(ADJ) too great or numerous to be counted or measured",
"untouchable": "(ADJ) impossible to affect or defeat",
"untoward": "(ADJ) unexpected and inappropriate; troublesome",
"untrue": "(ADJ) not in accordance with fact; false",
"unused": "(ADJ) not used or not yet put into service",
"unusual": "(ADJ) not common or ordinary; remarkable",
"unveil": "(V) to reveal or make known for the first time",
"unwary": "(ADJ) not cautious; unaware of possible dangers",
"unwelcome": "(ADJ) not gladly received; unwanted",
"unwell": "(ADJ) not feeling healthy; ill",
"unwell": "(adj) not in good health; ill"
"unwholesome": "(adj) detrimental to physical or moral well-being"
"unwieldy": ["(adj) difficult to carry or move because of size or shape", "(adj) hard to manage or control"]
"unwilling": "(adj) reluctant or not ready to do something"
"unwind": ["(v) to relax after stress or tension", "(v) to undo or loosen something that is wound up"]
"unwise": "(adj) lacking good judgment; imprudent"
"unwitting": ["(adj) not aware of the full facts", "(adj) done unintentionally; accidental"]
"unwomanly": "(adj) not characteristic of a woman; unfeminine"
"unworkable": "(adj) not able to be put into practice or to function successfully"
"unworldly": ["(adj) not concerned with material values or ordinary life", "(adj) naive or inexperienced"]
"unworthy": "(adj) not deserving respect, attention, or affection"
"unwound": ["(v) past tense of unwind", "(adj) relaxed or freed from tension"]
"unwritten": ["(adj) not recorded in writing", "(adj) understood or implied without being stated"]
"unyielding": ["(adj) not giving way to pressure; firm or inflexible", "(adj) resolute and determined"]
"upbeat": ["(adj) cheerful and optimistic", "(n) an unaccented beat preceding the first beat of a bar"]
"upbraid": "(v) to scold or criticize severely"
"upbringing": "(n) the treatment and instruction received by a child from its parents"
"upcoming": "(adj) about to happen; forthcoming"
"update": ["(v) to make something more modern or current", "(n) a new version or improved form of something"]
"upgrade": ["(v) to raise something to a higher standard", "(n) an improved version or level"]
"upheaval": "(n) a violent or sudden change or disruption"
"uphold": ["(v) to maintain or support", "(v) to confirm or sustain a decision or principle"]
"uplift": ["(v) to raise morally, spiritually, or physically", "(n) an improvement in mood or spirit"]
"upload": ["(v) to transfer data from one system to another", "(n) the act of transferring data"]
"upmost": "(adj) of the highest importance; supreme"
"upon": "(prep) on; immediately after"
"uppermost": "(adj) highest in position or rank"
"upright": ["(adj) vertical; erect", "(adj) morally correct; honest"]
"uprising": "(n) an act of resistance or rebellion; a revolt"
"uproar": "(n) a loud and impassioned noise or disturbance"
"uproot": ["(v) to pull something out of the ground", "(v) to remove or displace from a home or environment"]
"upscale": "(adj) high quality; intended for affluent consumers"
"upset": ["(v) to disturb or distress", "(n) an unexpected result or defeat", "(adj) emotionally disturbed"]
"upshot": "(n) the final or eventual outcome of a discussion or situation"
"upside": "(n) the positive aspect of something"
"upstage": ["(v) to draw attention away from someone", "(adj) situated toward the back of a stage"]
"upstanding": "(adj) honest and respectable"
"upstart": ["(n) a person who has risen suddenly in rank or importance", "(adj) newly successful and arrogant"]
"upstream": ["(adv) against the current of a stream", "(adj) situated toward the source of a river"]
"uptake": ["(n) the action of taking up or absorbing something", "(n) understanding or comprehension"]
"uptight": "(adj) anxious or tense"
"uptown": ["(adv) toward or in the residential part of a city", "(adj) relating to an affluent area"]
"upturn": ["(n) an improvement or upward trend", "(v) to turn something upward"]
"upward": ["(adv) toward a higher place or level", "(adj) moving or directed toward a higher position"]
"upwards": "(adv) toward a higher place or level; in an increasing direction"
"uranium": "(n) a heavy radioactive metallic element used as fuel in nuclear reactors"
"urban": "(adj) relating to a city or town"
"urbane": "(adj) courteous and refined in manner"
"urbanize": "(v) to make or become more urban"
"urchin": ["(n) a mischievous child", "(n) a small sea creature with spines"]
"urge": ["(v) to strongly encourage or persuade", "(n) a strong desire or impulse"]
"urgent": "(adj) requiring immediate action or attention"
"urgency": "(n) importance requiring swift action"
"urinal": "(n) a fixture for urination, typically in a public restroom"
"urn": "(n) a tall, rounded vase, often with a stem and base"
"usage": ["(n) the way in which a word or phrase is used", "(n) the action of using something"]
"useful": "(adj) able to be used advantageously"
"useless": "(adj) not achieving or incapable of achieving any useful result"
"user": "(n) a person who uses or operates something"
"usual": "(adj) customary or expected"
"usually": "(adv) under normal conditions; most of the time"
"utensil": "(n) a tool or container used for practical purposes, especially in a kitchen"
"utility": ["(n) the state of being useful", "(n) a public service such as water or electricity"]
"utilize": "(v) to make practical and effective use of something"
"utmost": ["(adj) greatest or most extreme", "(n) the greatest possible amount or degree"]
"utopia": "(n) an imagined perfect society or place"
"utopian": "(adj) modeled on or aiming for a perfect society"
"utter": ["(v) to speak or pronounce", "(adj) complete; absolute"]
"utterance": "(n) a spoken word, statement, or vocal sound"
"utterly": "(adv) completely or absolutely"
"vacant": ["(adj) empty; not occupied", "(adj) showing no intelligence or interest"]
"vacate": "(v) to leave a place that was previously occupied"
"vacation": ["(n) a period of time spent away from work or home for rest or recreation", "(v) to take a holiday"]
"vaccinate": "(v) to administer a vaccine to protect against disease"
"vaccine": "(n) a substance used to stimulate the production of antibodies and provide immunity"
"vacillate": "(v) to waver between different opinions or actions"
"vacuum": ["(n) a space entirely devoid of matter", "(v) to clean with a vacuum cleaner"]
"vague": "(adj) unclear or indefinite in meaning or expression"
"vain": ["(adj) having an excessively high opinion of oneself", "(adj) producing no result; useless"]
"valid": "(adj) legally or logically sound"
"validate": "(v) to confirm the truth or accuracy of something"
"valiant": "(adj) showing courage or determination"
"valor": "(n) great courage in the face of danger"
"value": ["(n) the worth of something", "(v) to estimate or appreciate worth"]
"valve": "(n) a device controlling the passage of fluid through a pipe"
"vampire": "(n) a mythical being that drinks the blood of the living"
"van": "(n) a medium-sized motor vehicle used for transporting goods or people"
"vanish": "(v) to disappear suddenly and completely"
"vanity": ["(n) excessive pride in appearance or achievements", "(n) a dressing table"]
"vantage": "(n) a place or position affording a good view"
"vapor": "(n) a substance diffused or suspended in the air, especially one normally liquid or solid"
"variable": ["(adj) not consistent or having a fixed pattern", "(n) an element that can change"]
"variation": "(n) a change or slight difference in condition or amount"
"variety": "(n) the quality or state of being different or diverse"
"various": "(adj) of different kinds; several"
"vary": "(v) to differ or change"
"vast": "(adj) of very great extent or quantity"
"vault": ["(n) an arched structure forming a ceiling or roof", "(n) a secure room for storing valuables", "(v) to leap or jump over something"]
"vector": "(n) a quantity with both magnitude and direction"
"vegetable": "(n) a plant or part of a plant used as food"
"vehicle": "(n) a means of transporting people or goods"
"veil": ["(n) a piece of fine material worn to protect or conceal the face", "(v) to cover or conceal"]
"vein": "(n) a blood vessel carrying blood toward the heart"
"velocity": "(n) the speed of something in a given direction"
"velvet": "(n) a soft fabric with a dense pile"
"vendor": "(n) a person or company offering something for sale"
"vengeance": "(n) punishment inflicted in retaliation for an injury or offense"
"venom": "(n) a poisonous substance secreted by animals such as snakes"
"venture": ["(n) a risky or daring journey or undertaking", "(v) to undertake a risky course of action"]
"verbal": "(adj) relating to or in the form of words"
"verdict": "(n) a decision on a disputed issue in a court of law"
"verify": "(v) to confirm the truth or accuracy of something"
"versatile": "(adj) able to adapt or be adapted to many functions or activities"
"version": "(n) a particular form of something differing in certain respects"
"vertical": "(adj) at right angles to the horizon"
"very": "(adv) to a high degree"
"vessel": ["(n) a ship or large boat", "(n) a container for holding liquids", "(n) a tube in the body that carries fluids"]
"veteran": ["(n) a person with long experience in a field", "(n) a former member of the armed forces"]
"veto": "(n) a constitutional right to reject a decision or proposal", "(v) to reject or prohibit"
"viable": "(adj) capable of working successfully"
"vibrate": "(v) to move continuously and rapidly back and forth"
"vicar": "(n) a representative or deputy of a bishop or parish priest"
"vice": ["(n) immoral or wicked behavior", "(n) a tool for holding an object firmly in place"]
"victim": "(n) a person harmed, injured, or killed as a result of a crime or accident"
"victory": "(n) an act of defeating an enemy or opponent"
"video": "(n) the recording, reproducing, or broadcasting of moving visual images"
"view": ["(n) the ability to see something", "(v) to look at or consider"]
"vigilant": "(adj) keeping careful watch for possible danger or difficulties"
"vigorous": "(adj) strong, healthy, and full of energy"
"village": "(n) a group of houses and associated buildings in a rural area"
"villain": "(n) a character whose evil actions are important to the plot"
"vine": "(n) a climbing or trailing woody-stemmed plant"
"vintage": ["(adj) denoting something of high quality from the past", "(n) the year or place in which wine was produced"]
"violin": "(n) a string instrument played with a bow"
"virtual": "(adj) existing or occurring on computers or the internet"
"virtue": "(n) behavior showing high moral standards"
"virus": "(n) a microscopic infectious agent that replicates only inside living cells"
"visible": "(adj) able to be seen"
"vision": ["(n) the faculty of sight", "(n) the ability to think about or plan the future with imagination"]
"visit": ["(v) to go to see someone or someplace", "(n) an act of going to see someone or someplace"]
"visual": "(adj) relating to seeing or sight"
"vital": ["(adj) absolutely necessary or essential", "(adj) full of energy; lively"]
"vivid": "(adj) producing strong, clear images in the mind"
"vocal": "(adj) relating to the voice", "(n) a part of a musical performance sung by a voice"]
"vocation": "(n) a strong feeling of suitability for a particular career or occupation"
"voice": ["(n) the sound produced in a person's larynx", "(v) to express in words"]
"void": ["(adj) completely empty", "(n) a large empty space", "(v) to declare invalid"]
"volatile": "(adj) liable to change rapidly and unpredictably"
"volume": ["(n) the amount of space occupied by something", "(n) a book forming part of a series", "(n) the degree of loudness"]
"volunteer": ["(n) a person who freely offers to take part in something", "(v) to offer to do something willingly"]
"vote": ["(n) a formal indication of a choice", "(v) to express a choice or opinion"]
"vow": ["(n) a solemn promise", "(v) to make a solemn promise"]
"voyage": ["(n) a long journey involving travel by sea or in space", "(v) to travel on a long journey"]
"vulgar": "(adj) lacking sophistication or good taste; unrefined"
"vulnerable": "(adj) susceptible to physical or emotional harm"
"vulture": "(n) a large bird of prey feeding chiefly on carrion"
"vying": "(v) competing eagerly with someone to achieve something"
"wade": "(v) to walk through water or another substance that impedes movement"
"waffle": ["(n) a crisp cake made from batter", "(v) to speak or write evasively"]
"wage": ["(n) a fixed regular payment for work", "(v) to carry on or engage in a conflict or campaign"]
"wagon": "(n) a four-wheeled vehicle for transporting goods"
"waist": "(n) the part of the body between the ribs and hips"
"wait": ["(v) to stay where one is until a particular time or event", "(n) a period of waiting"]
"wake": ["(v) to stop sleeping", "(n) a vigil held beside the body of someone who has died"]
"walk": ["(v) to move at a regular pace by lifting and setting down each foot", "(n) an act of traveling on foot"]
"wall": "(n) a continuous vertical structure that encloses or divides an area"
"wander": ["(v) to move about aimlessly", "(n) an act of traveling without a fixed course"]
"want": ["(v) to desire something", "(n) a lack or deficiency of something"]
"war": ["(n) a state of armed conflict between different nations or groups", "(v) to engage in conflict"]
"warm": ["(adj) of or at a fairly high temperature", "(v) to make or become warm"]
"warn": "(v) to inform someone of possible danger or trouble"
"warp": ["(v) to become bent or twisted out of shape", "(n) a distortion or deviation"]
"warrant": ["(n) a document authorizing police to make an arrest or search", "(v) to justify or necessitate"]
"warrior": "(n) a brave or experienced soldier or fighter"
"wash": ["(v) to clean with water", "(n) an act of washing"]
"waste": ["(v) to use carelessly or without purpose", "(n) unwanted or unusable material"]
"watch": ["(v) to look at or observe attentively", "(n) a small timepiece worn on the wrist"]
"water": ["(n) a colorless, transparent liquid essential for life", "(v) to pour or sprinkle water on something"]
"wave": ["(n) a long body of water curling into an arched form", "(v) to move one's hand to signal or greet"]
"wax": ["(n) a sticky yellowish substance secreted by bees", "(v) to polish or coat with wax"]
"way": ["(n) a method, style, or manner of doing something", "(n) a road or path"]
"weak": "(adj) lacking physical strength or energy"
"wealth": "(n) an abundance of valuable possessions or money"
"weapon": "(n) a thing designed or used for inflicting bodily harm or damage"
"wear": ["(v) to have clothing on one's body", "(n) damage caused by use"]
"weather": ["(n) the state of the atmosphere at a place and time", "(v) to withstand or endure"]
"weave": ["(v) to form fabric by interlacing threads", "(n) a pattern or structure formed by weaving"]
"wedding": "(n) a marriage ceremony"
"week": "(n) a period of seven days"
"weep": "(v) to shed tears"
"weigh": ["(v) to measure the weight of something", "(v) to consider carefully"]
"weight": "(n) the measure of how heavy something is"
"welcome": ["(v) to greet someone gladly", "(n) an instance of greeting someone"]
"welfare": "(n) the health, happiness, and fortunes of a person or group"
"well": ["(adv) in a good or satisfactory way", "(n) a deep hole from which water is drawn"]
"west": "(n) the direction toward the point where the sun sets"
"wet": ["(adj) covered or saturated with water", "(v) to make something wet"]
"whale": "(n) a very large marine mammal"
"what": "(pron) asking for information specifying something"
"wheel": "(n) a circular object that revolves on an axle", "(v) to push or pull something on wheels"]
"when": "(adv) at what time"
"where": "(adv) in or to what place"
"which": "(pron) asking for information specifying one or more items"
"while": ["(conj) during the time that", "(n) a period of time"]
"whisper": ["(v) to speak very softly", "(n) a soft or confidential utterance"]
"white": "(adj) of the color of milk or fresh snow"
"whole": "(adj) all of; entire"
"why": "(adv) for what reason or purpose"
"wide": "(adj) of great or more than average width"
"wild": ["(adj) living or growing in the natural environment", "(n) an uncultivated or uninhabited region"]
"will": ["(v) expressing the future tense", "(n) a legal document expressing wishes after death"]
"win": ["(v) to be successful or victorious", "(n) a victory"]
"wind": ["(n) the natural movement of air", "(v) to twist or coil"]
"window": "(n) an opening in a wall or roof fitted with glass"
"wine": "(n) an alcoholic drink made from fermented grapes"
"wing": ["(n) a part of a bird or aircraft used for flying", "(v) to travel quickly"]
"winter": "(n) the coldest season of the year"
"wipe": ["(v) to clean or dry by rubbing", "(n) an act of wiping"]
"wire": "(n) a thin, flexible strand of metal"
"wisdom": "(n) the quality of having experience, knowledge, and good judgment"
"wish": ["(v) to desire something", "(n) a hope or desire for something"]
"with": "(prep) accompanied by"
"withdraw": "(v) to remove or take away something"
"within": "(prep) inside or not beyond"
"without": "(prep) in the absence of"
"witness": ["(n) a person who sees an event", "(v) to see an event happen"]
"wolf": "(n) a wild carnivorous mammal related to the dog"
"woman": "(n) an adult human female"
"wonder": ["(n) a feeling of amazement", "(v) to desire to know something"]
"wood": "(n) the hard fibrous material forming the trunk of trees"
"wool": "(n) the soft, curly hair forming the coat of sheep"
"word": "(n) a single distinct meaningful element of speech or writing"
"work": ["(v) to perform a task or duty", "(n) activity involving mental or physical effort"]
"world": "(n) the earth, together with all its countries and peoples"
"worry": ["(v) to feel anxious or troubled", "(n) a state of anxiety"]
"worship": ["(v) to show reverence and adoration for a deity", "(n) the feeling or expression of reverence"]
"worth": ["(n) the value equivalent to that of someone or something", "(adj) equivalent in value to"]
"worthy": "(adj) deserving respect or attention"
"wound": ["(n) an injury to living tissue", "(v) to inflict an injury"]
"wrap": ["(v) to cover or enclose in paper or soft material", "(n) a covering or garment"]
"wreck": ["(n) the destruction of a ship or vehicle", "(v) to destroy or severely damage"]
"wrestle": ["(v) to grapple with an opponent", "(n) a physical struggle"]
"wretched": "(adj) in a very unhappy or unfortunate state"
"wrinkle": ["(n) a small line or fold in something", "(v) to make or become wrinkled"]
"wrist": "(n) the joint connecting the hand with the forearm"
"write": "(v) to mark letters or words on a surface"
"writer": "(n) a person who writes books, stories, or articles"
"writing": "(n) the activity or skill of composing text"
"wrong": ["(adj) not correct or true", "(n) an unjust or dishonest act"]
"yard": "(n) a unit of linear measure equal to three feet", "(n) an area of land next to a building"]
"year": "(n) the time taken by the earth to make one revolution around the sun"
"yellow": "(adj) of the color between green and orange", "(n) the color yellow"]
"yes": "(adv) used to give an affirmative response"
"yesterday": "(n) the day before today"
"yet": "(adv) up to the present time; still"
"yield": ["(v) to produce or provide", "(v) to give way under pressure", "(n) the full amount produced"]
"young": "(adj) having lived or existed for only a short time"
"youth": "(n) the period between childhood and adult age"
"zeal": "(n) great energy or enthusiasm in pursuit of a cause"
"zealous": "(adj) showing great energy or enthusiasm"
"zebra": "(n) an African wild horse with black-and-white stripes"
"zenith": "(n) the time at which something is most powerful or successful"
"zero": ["(n) the figure 0", "(n) a point on a scale representing nothing"]
"zest": ["(n) great enthusiasm and energy", "(n) the outer colored part of citrus fruit peel"]
"zigzag": ["(n) a line or course having sharp turns", "(v) to move in sharp turns"]
"zip": ["(v) to fasten with a zipper", "(n) a device for fastening clothing or bags"]
"zone": "(n) an area or stretch of land having a particular characteristic"
"zoo": "(n) a facility where animals are kept for public display"
"zoom": ["(v) to move or travel quickly", "(v) to adjust the focus of a camera to make an image larger or smaller"]
}
def bootlife(starting_bucks=0):
    def child_probability(age):
        if age<18:return 0.0
        if age<=35:return 1.0
        if age<=60:return max(0.2,1.0-(age-35)*0.03)
        if age<=75:return 0.05
        return 0.01
    def child_event():
        if "Children" not in relationships or not relationships["Children"]:return
        if random.random()>0.20:return
        child=random.choice(relationships["Children"])
        name=child["name"];age=child["age"]
        if age<=3:events=[f"{name} giggles at you for no reason.",f"{name} learns a new word and proudly says it to you.",f"{name} hands you a toy and wants to play.",f"{name} toddles over and hugs your leg."]
        elif age<=7:events=[f"{name} shows you a drawing they made.",f"{name} asks you to read them a story.",f"{name} excitedly tells you about a bug they found.",f"{name} wants to play a simple game with you."]
        elif age<=12:events=[f"{name} asks you a curious question about the world.",f"{name} wants help with a small school project.",f"{name} tells you about a new friend they made.",f"{name} shares something funny that happened today."]
        elif age<=17:events=[f"{name} asks for advice about something on their mind.",f"{name} talks to you about their hobbies.",f"{name} shares a goal they’re excited about.",f"{name} wants to hang out and chat for a bit."]
        else:events=[f"{name} checks in to see how you're doing.",f"{name} shares some news from their day.",f"{name} asks if you want to spend some time together.",f"{name} tells you they appreciate you."]
        print("\n👶 Child Event:");print(random.choice(events))
    def menu_future_family():
        print("\n🏡 FUTURE FAMILY")
        print("1) Think about settling down")
        print("2) Talk about the future")
        print("3) Imagine a home together")
        print("4) Ask to marry")
        print("5) Have a child")
        print("6) Check long-term compatibility")
        print("7) Return")
        choice=input("> ").strip()
        if "Love" not in relationships or not relationships["Love"]:
            print("You are currently single.")
            return
        person=relationships["Love"]
        points=relationships.get("LovePoints",0)
        trait=relationships.get("LoveTrait","unknown")
        comp=relationships.get("LoveCompatibility",50)
        if choice=="1":
            print("You think about who you want to settle down with...");print(f"{person} crosses your mind.")
            if points>15:print("You feel like your bond is strong.")
            elif points>5:print("You feel hopeful about the connection.")
            else:print("You’re not sure yet, but you’re curious.")
        elif choice=="2":
            print(f"You talk with {person} about the future.")
            if trait in ["thoughtful","quiet"]:
                print(f"{person} listens carefully and shares a calm, steady vision.");relationships["LovePoints"]+=2
            elif trait in ["energetic","outgoing"]:
                print(f"{person} gets excited and starts imagining fun possibilities.");relationships["LovePoints"]+=3
            else:
                print(f"{person} shares a few ideas and seems happy to talk.");relationships["LovePoints"]+=1
        elif choice=="3":
            print(f"You and {person} imagine what a future home might be like.")
            home=random.choice(["a cozy apartment full of plants","a small house with a bright backyard","a modern place with lots of tech","a quiet home near a park","a colorful place full of art"])
            print(f"You picture {home}.");relationships["LovePoints"]+=2
        elif choice=="4":
            print(f"You ask {person} if they'd like to marry you someday.")
            success_chance=(comp+points)/200
            if random.random()<success_chance:
                print(f"{person} happily agrees!")
                print("\nChoose a honeymoon location:")
                print("1) Cloud City (100 Gunch Coins)")
                print("2) Byte Beach (75 Gunch Coins)")
                print("3) Kernel Canyon (50 Gunch Coins)")
                loc_choice=input("> ").strip()
                locations={"1":("Cloud City",100),"2":("Byte Beach",75),"3":("Kernel Canyon",50)}
                if loc_choice in locations:
                    loc,cost=locations[loc_choice]
                    if gunch_coins>=cost:
                        gunch_coins-=cost
                        print(f"You and {person} go to {loc} for your honeymoon!");print("It’s a wonderful trip full of memories.");relationships["LovePoints"]+=5;happiness+=5
                    else:print("You don't have enough Gunch Coins for that honeymoon.")
                else:print("Invalid choice, but the engagement still stands!")
            else:
                print(f"{person} says they need more time to think about it.");relationships["LovePoints"]-=1
        elif choice=="5":
            prob=child_probability(age)
            if prob<=0:
                print("You're not at a stage in life where this makes sense.");return
            print(f"You and {person} talk about having a child.")
            if random.random()<prob:
                baby_name=random.choice(["Sam","Charlie","Morgan","Avery","Jamie","Sky","Robin"])
                print(f"You decide to welcome a child into your life named {baby_name}!")
                relationships.setdefault("Children",[]).append({"name":baby_name,"age":0})
                relationships["LovePoints"]+=4;happiness+=4
            else:print("You both decide it's not the right time right now.")
        elif choice=="6":
            print(f"Your long-term compatibility with {person} is {comp}%.")
            if comp>=80:print("You two seem like a great long-term match.")
            elif comp>=60:print("You have a lot of potential together.")
            elif comp>=40:print("You get along, but you may need to understand each other better.")
            else:print("You might have different long-term goals.")
        elif choice=="7":return
        else:print(f"{choice} is invalid.")    def menu_love():
        print("\n❤️ LOVE")
        print("1) Look for someone to talk to")
        print("2) Go on a friendly hangout")
        print("3) Check your connections")
        print("4) Pass a note to someone (unavailable)")
        print("5) Ask them out")
        print("6) Return")
        choice=input("> ").strip()
        if "Love" not in relationships:
            relationships["Love"] = None
        if "LovePoints" not in relationships:
            relationships["LovePoints"] = 0
        if "LoveTrait" not in relationships:
            relationships["LoveTrait"] = None
        if "LoveCompatibility" not in relationships:
            relationships["LoveCompatibility"] = 0
        if "LoveLastTalk" not in relationships:
            relationships["LoveLastTalk"] = age
        if choice == "1":
            print("You go to the library to find someone to talk to.")
            time.sleep(random.random())
            if random.random() > 0.4:
                print("The library is open and you walk in.")
                person = random.choice(["Alex", "Jordan", "Taylor", "Riley", "Casey"])
                trait = random.choice(LOVE_TRAITS)
                print(f"You meet {person}. They seem {trait}. You two talk for a bit.")
                relationships["Love"] = person
                relationships["LoveTrait"] = trait
                relationships["LovePoints"] = 5
                relationships["LoveCompatibility"] = random.randint(40, 100)
                relationships["LoveLastTalk"] = age
            else:
                print("The library is closed already. You'll need to try again tomorrow.")
        elif choice == "2":
            if relationships["Love"]:
                person = relationships["Love"]
                comp = relationships["LoveCompatibility"]
                print(f"You invite {person} to hang out.")
                success_chance = comp / 100
                if random.random() < success_chance:
                    print(f"You and {person} have a fun, friendly time together.")
                    relationships["LovePoints"] += 3
                    happiness += 2
                else:
                    print(f"{person} was busy today.")
    
                relationships["LoveLastTalk"] = age
            else:
                print("You don't have anyone to hang out with yet.")
        elif choice == "3":
            if relationships["Love"]:
                print(f"You are currently talking to: {relationships['Love']}")
                print(f"Trait: {relationships['LoveTrait']}")
                print(f"Connection strength: {relationships['LovePoints']}")
                print(f"Compatibility: {relationships['LoveCompatibility']}%")
            else:
                print("You haven't met anyone yet.")
        elif choice == "5":
            if relationships["Love"]:
                person = relationships["Love"]
                points = relationships["LovePoints"]
                comp = relationships["LoveCompatibility"]
                print(f"You decide to ask {person} if they'd like to spend more time together.")
                success_chance = (comp + points) / 200
                if random.random() < success_chance:
                    print(f"{person} smiles and says they'd like that!")
                    relationships["LovePoints"] += 4
                    happiness += 3
                else:
                    print(f"{person} seems unsure and says maybe another time.")
                    relationships["LovePoints"] -= 1
                    stability -= 1
                relationships["LoveLastTalk"] = age
            else:
                print("You haven't met anyone yet.")
        elif choice == "6":
            return    
        else:
            print("That option isn't ready yet.")
    def menu_mischief():
        print("\n😈 MISCHIEF")
        print("1) Pickpocket")
        print("2) GTA")
        print("3) Sneak around")
        print("4) Prank someone")
        print("5) Return")
        choice=input("> ").strip()
        if choice == "1":
            print("You try to pick someone's pocket - but the game crashes!")
        elif choice == "2":
            print("You try to steal a luxury car - but the game crashes!")
        elif choice == "3":
            print("You attempt to be sneaky - but get caught before heading out the door")
        elif choice == "4":
            print("You try to prank someone - but they notice it and carefully get by it...")
        elif choice == "5":
            return
        else:
            print(f"You tried to input {choice} - but it's invalid!")
    def life_event():
        nonlocal health,happiness,stability,gunch_coins
        if life_stage=="Child":
            events=[
                ("You made a new friend at school.",0,+6,0),
                ("You had a fun day at recess.",0,+4,0),
                ("You scraped your knee.",-3,-1,0),
                ("You learned something cool in class.",0,+3,+2)
            ]
        elif life_stage=="Teen":
            events=[
                ("You joined a club at school.",0,+5,+2),
                ("You had a rough day socially.",0,-4,0),
                ("You aced a test!",0,+6,+4),
                ("You stayed up too late texting.",-4,-2,-1)
            ]
        else:
            events=[
                ("You had a productive day.",0,+4,+3),
                ("You felt stressed today.",0,-3,-2),
                ("You found a little money on the ground.",0,+2,0),
                ("You learned a new skill online.",0,+5,+3)
            ]
        event,dh,dhap,dstab=random.choice(events)
        print(f"✨ Life Event: {event}")
        health+=dh
        happiness+=dhap
        stability+=dstab
    milestones=[]
    def add_milestone(text):
        milestones.append(text)
        print(f"🏅 Milestone reached: {text}")
    def update_life_stage():
        nonlocal life_stage
        if age<13:
            life_stage="Child"
        elif age<18:
            life_stage="Teen"
        else:
            life_stage="Adult"
    life_stage="Child"
    age=0
    health=100
    happiness=100
    stability=100
    alive=True
    gunch_coins=50
    gunch_bucks=starting_bucks
    job=None
    inventory=[]
    parents={"Mother":random.choice(["Ava","Mia","Lily","Emma","Sofia"]), "Father":random.choice(["Noah","Liam","Ethan","Mason","Logan"])}
    siblings=[]
    if random.random()<0.5:
        siblings.append(random.choice(["Alex","Jordan","Taylor","Sam","Riley"]))
    relationships={"Parents": parents, "Siblings": siblings, "Friends": [], "Love": []}
    print("🟢 BootLife initialized.")
    print("A new life begins.\n")
    def show_stats():
        print(f"\n📊 STATUS — Age: {age}")
        print(f"Health:       {health}")
        print(f"Happiness:    {happiness}")
        print(f"Stability:    {stability}")
        print(f"Job:          {job if job else 'Unemployed'}")
        print(f"Gunch Coins:  {gunch_coins}")
        print(f"Gunch Bucks:  {gunch_bucks}")
        print(f"Inventory:    {inventory if inventory else 'None'}")
        print(f'RELATIONSHIPS:\n{random.choice([re.sub("{|\[|}|\]","",pprint.pformat(relationships, indent = 4)).replace(":"," - ").replace("    ", "|___"),"I don't wanna",re.sub(r"\[|\]","",str(random.sample(list(string.ascii_letters+random.choice([string.ascii_digits, math.ceil(int(string.ascii_digits))/random.randint(1,10), string.ascii_digits]))))).replace(", "," ")])}')
    def random_event():
        nonlocal health,happiness,stability
        events=[("You had a really good day.",+5,+8,+3),("You felt a bit off today.",-5,-3,-2),("You found something interesting online.",+3,+5,0),("You stayed up too late.",-7,-4,-3),("You learned something cool.",+2,+6,+4)]
        event,dh,dhap,dstab=random.choice(events)
        print(f"\n⚡ EVENT: {event}")
        health+=dh
        happiness+=dhap
        stability+=dstab
    def check_alive():
        nonlocal alive
        if health<=0 or stability<=0:
            print("\n🔴 GAME OVER — Your life has ended.")
            alive=False
        elif happiness<=0:
            print("\n🟡 You became too unhappy to continue.")
            alive=False
    def menu_actions():
        nonlocal health,happiness,stability,inventory,gunch_coins
        print("\n🛠 ACTIONS")
        print("1) Go for a walk")
        print("2) Play a game")
        print("3) Learn something new")
        print("4) Clean your room")
        print("5) Chat online")
        print("6) Buy something")
        print("7) Work on a hobby")
        print("8) Return")
        choice=input("> ").strip()
        if choice=="1":
            print("🚶 You took a walk.")
            health+=5
            happiness+=3
        elif choice=="2":
            if gunch_coins<5:
                print("Not enough Gunch Coins.")
                return
            gunch_coins-=5
            print("🎮 You played a game.")
            happiness+=7
        elif choice=="3":
            print("📘 You learned something new.")
            stability+=5
        elif choice=="4":
            print("🧹 You cleaned your room.")
            health+=3
            stability+=2
        elif choice=="5":
            print("💬 You chatted online.")
            q = random.random() 
            if q <= 0.01:
                print("You couldn't connect to the Internet. 😭")
                happiness -= 20
            
            elif q <= 0.40:
                print("You were bullied online. ☹")
                happiness -= 10
            
            elif q <= 0.80:
                print("You are invited to a strangers' house")
                if random.choice([True,False]):
                    print("You have a lot of fun and candy. Nothing bad happens!")
                    happiness += 20
                    health -= 7
                else:
                    print("They hold you for a 25000 gunch coin ransom")
                    health = 1
            
            elif q <= 0.90:
                print("you meet a new person who gives you 20 gunch coins")
                gunch_coins += 20
            
            else:
                friend = random.choice(["Bob",'Joe',"Steve","Adam","Mike","Ava","Kate","Kyle", "Jimmy III"])
                print(f"You make a new friend - {friend} - online! 😄")
                happiness += 6
                relationships["Friends"].append(friend)
        elif choice=="6":
            items=[("Sticker Pack",10),("Cool Hat",20),("LED Keychain",15),("Notebook",12),("Snack",5)]
            print("\n🛒 SHOP")
            for i,(item,cost) in enumerate(items,1):
                print(f"{i}) {item} — {cost} coins")
            choice2=input("> ").strip()
            if not choice2.isdigit() or not (1<=int(choice2)<=len(items)):
                print("Invalid choice.")
                return
            item,cost=items[int(choice2)-1]
            if gunch_coins<cost:
                print("Not enough coins.")
                return
            gunch_coins-=cost
            inventory.append(item)
            print(f"You bought a {item}.")
        elif choice=="7":
            print("🎨 You worked on a hobby.")
            happiness+=5
            if random.random()<0.25:
                craft=random.choice(["Drawing","Origami","Bracelet","Mini Sculpture"])
                print(f"✨ You made a {craft}!")
                inventory.append(craft)
    def menu_job():
        nonlocal job,gunch_coins
        print("\n💼 JOBS")
        print("1) Background Service (10 coins/year)")
        print("2) UI Thread (12 coins/year)")
        print("3) Kernel Assistant (15 coins/year)")
        print("4) Quit job")
        print("5) Return")
        choice=input("> ").strip()
        if choice=="1":
            job="Background Service"
            print("You are now a Background Service.")
        elif choice=="2":
            job="UI Thread"
            print("You are now a UI Thread.")
        elif choice=="3":
            job="Kernel Assistant"
            print("You are now a Kernel Assistant.")
        elif choice=="4":
            print("You quit your job.")
            job=None
    def menu_relationships():
        print("\n🤝 RELATIONSHIPS")
        print("1) Meet someone new")
        print("2) Interact with someone")
        print("3) Return")
        choice=input("> ").strip()
        if choice=="1":
            name=random.choice(["Alex","Jordan","Taylor","Sam","Riley"])
            relationships[name]=50
            print(f"You met {name}.")
        elif choice=="2":
            if not relationships:
                print("You don't know anyone yet.")
                return
            print("Choose someone:")
            for i,name in enumerate(relationships.keys(),1):
                print(f"{i}) {name} ({relationships[name]})")
            idx=int(input("> "))-1
            name=list(relationships.keys())[idx]
            print(f"You spent time with {name}.")
            relationships[name]+=random.randint(-5,10)
    def menu_family():
        print("\n🏠 FAMILY")
        print("1) Talk to your parents")
        print("2) Talk to a sibling")
        print("3) Ask for advice")
        print("4) Return")
        choice=input("> ").strip()
        if choice=="1":
            parent=random.choice(["Mother","Father"])
            print(f"You talked with your {parent}.")
        elif choice=="2":
            if not siblings:
                print("You have no siblings.")
                return
            sib=random.choice(siblings)
            print(f"You talked with {sib}.")
        elif choice=="3":
            print("Your family gave you some advice.")
        elif choice == "4":
            return
    def menu_inventory():
        print("\n📦 MY STUFF")
        if not inventory:
            print("You have nothing.")
        else:
            for item in inventory:
                print(f"- {item}")
    def menu_money():
        nonlocal gunch_coins,gunch_bucks
        print("\n💰 MONEY MENU")
        print("1) Exchange Gunch Bucks → Gunch Coins")
        print("2) View balances")
        print("3) Return")
        choice=input("> ").strip()
        if choice=="1":
            print("\nExchange rate: 1 Gunch Buck → 25 Gunch Coins")
            print(f"You have {gunch_bucks} Gunch Bucks.")
            amount=input("How many bucks do you want to exchange? ").strip()
            if not amount.isdigit():
                print("Invalid amount.")
                return
            amount=int(amount)
            if amount<=0 or amount>gunch_bucks:
                print("You don't have that many.")
                return
            gunch_bucks-=amount
            gained=amount*25
            gunch_coins+=gained
            print(f"💱 Exchanged {amount} Gunch Bucks for {gained} Gunch Coins.")
        elif choice=="2":
            print(f"\nGunch Coins: {gunch_coins}")
            print(f"Gunch Bucks: {gunch_bucks}")
    while alive:
        print("\n====================")
        print(f" AGE {age} — MAIN MENU")
        print("====================")
        print("1) Age up")
        print("2) Actions")
        print("3) Job")
        print("4) Relationships")
        print("5) Family")
        print("6) My Stuff")
        print("7) Stats")
        print("8) Money")
        print("8.5) Milestones")
        print("9) Exit game")
        print("10) Mischief (13+)")
        print("11) Love (16+)")
        print("12) Future Family (18+)")
        print("13) Something Else That We Won't Reveal")
        choice=input("> ").strip()
        if choice=="1":
            age+=1
            if "Children" in relationships:
                for c in relationships["Children"]:
                    c["age"]+=1
            child_event()
            if age==1:
                add_milestone("Your first birthday!")
            if age==5:
                add_milestone("Started school")
            if age==10:
                add_milestone("Entered middle school")
            if age==13:
                add_milestone("Became a teenager")
            if age==16:
                add_milestone("Got your first part-time job opportunity")
            if age==18:
                add_milestone("Became an adult")
            if age==21:
                add_milestone("Entered full adulthood")
            update_life_stage()
            print(f"\n📅 You aged to {age}.")
            random_event()
            life_event()
            if job=="Background Service":
                gunch_coins+=10
            elif job=="UI Thread":
                gunch_coins+=12
            elif job=="Kernel Assistant":
                gunch_coins+=15
            check_alive()
        elif choice=="2":
            menu_actions()
        elif choice=="3":
            menu_job()
        elif choice=="4":
            menu_relationships()
        elif choice=="5":
            menu_family()
        elif choice=="6":
            menu_inventory()
        elif choice=="7":
            show_stats()
        elif choice=="8":
            menu_money()
        elif choice=="9":
            print("Exiting BootLife.")
            break
        elif choice=="8.5":
            print("\n🏅 MILESTONES")
            if not milestones:
                print("You haven't reached any milestones yet.")
            else:
                for m in milestones:
                    print(f"- {m}")
        elif choice=="10":
            if age<13:
                print("You are too young for this menu.")
            else:
                menu_mischief()
        
        elif choice=="11":
            if age<16:
                print("You are too young to date.")
            else:
                menu_love()
        
        elif choice=="12":
            if age<18:
                print("You are too young to start a family.")
            else:
                menu_future_family()
    print("\nThanks for playing BootLife.")
    return gunch_bucks
def random_groups():
    y = input("How many people?").strip()
    try:
        y = int(y)
        for i in range(y):
            person = input("Enter name - ")
            group_peeps.append(person)
        try:
            Num_per_group = int(input(f"How many people per group? people: {len(group_peeps)}"))
            try:
                groups = math.ceil(len(group_peeps)/Num_per_group)
            except ZeroDivisionError:
                print("That isn't possible - setting the number per group to 3")
                Num_per_group=3
            m=groups
            for l in range(groups):
                for _ in range(m):
                    print(f"GROUP {l+1}: ")
                    peep = random.choice(group_peeps)
                    group_peeps.remove(peep)
                print("\nGROUP FINISHED")
            except ValueError:
                print("That isn't an integer!")
    except ValueError:
        print(f"{y} is not an integer!")
def print_alt(*args, **kwargs):
    args_str = " ".join([str(arg) for arg in args])
    kwargs_str = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    printf(f"\033[{random.randint(31,36)}m \033[{random.randint(40,46)}m {args_str} \033[0m {kwargs_str}")
while True:
  i = input("WORD: (or type q to quit)")
  if i != 'q':
    print(i)
  else:
    print(i, "BYE!")
    break
def microshell():
    depth = 0
    while True:
        cmd = input(f"Micro[{depth}]> ").strip().lower()
        track_command_wrapper()
        if cmd == "exit": break
        if cmd == "up": depth += 1
        elif cmd == "down": depth -= 1
        elif cmd == "depth": print(depth)
        elif cmd == "zero": depth = 0
        elif cmd=="crash": 
            try:
                int("OK")
            except ValueError:
                print("Crashed")
                return
        elif cmd=="negative": depth = -1
def novel():
    if not novel_installed:
        print("novel: module not installed.")
        return
    unique = len(novel_cmd_counts)
    ratio = unique / novel_total_cmds if novel_total_cmds else 0
    score = max(0, min(17, int(round(ratio * 17))))
    if score <= 4:
        freshness = "low"
    elif score <= 11:
        freshness = "moderate"
    else:
        freshness = "high"
    if score <= 5:
        drift = "static"
    elif score <= 12:
        drift = "stable"
    else:
        drift = "erratic"
    rare = min(novel_cmd_counts, key=lambda c: novel_cmd_counts[c]) if novel_cmd_counts else "N/A"
    print(f"Novelty Index: {score}/17")
    print(f"Freshness: {freshness}")
    print(f"Drift: {drift}")
    print(f"Rare: {rare}")
def track_command_wrapper():
    try:
        track_command(command)
    except NameError:
        pass
    try:
        track_command(cmd)
    except NameError:
        pass
    try:
        track_command(mod)
    except NameError:
        pass
    try:
        track_command(dcmd)
    except NameError:
        pass
    try:
        track_command(note)
    except NameError:
        pass
    try:
        track_command(game)
    except NameError:
        pass
    try:
        track_command(scmd)
    except NameError:
        pass
    try:
        track_command(cre8or_cmd)
    except NameError:
        pass
def track_command(cmd):
    global novel_total_cmds, novel_cmd_counts, novel_last_new_cmd
    if not novel_installed:
        return
    novel_total_cmds += 1
    if cmd not in novel_cmd_counts:
        novel_cmd_counts[cmd] = 0
        novel_last_new_cmd = cmd
    novel_cmd_counts[cmd] += 1
def install_novel():
    global novel_installed, novel_total_cmds, novel_cmd_counts, novel_last_new_cmd
    novel_installed = True
    novel_total_cmds = 0
    novel_cmd_counts = {}
    novel_last_new_cmd = None
    print("novel: command novelty tracking enabled.")
def coreshell():
    cstat_max = 100
    while True:
        cmd=input("`Core> ").strip().lower()
        track_command_wrapper()
        if cmd=="integrity":
            try:
                cstat=random.randint(0,cstat_max)
            except ValueError:
                cstat = 1
            print(f"Core Integrity: {cstat}")
            cstat_max-=cstat
        elif cmd=="tension":
            print(str(random.randint(1,27000000))+' Lb/4DSp (Pounds per 4D space)')
        elif cmd=="stablity":
            print(random.choice(["STABLE","UNSTABLE","CHECK BACK LATER"]))
        elif cmd=="exit":
            break
        elif cmd=="pulse":
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
            if cstat_max > 37:
                for i in range(random.randint(1,cstat_max)):
                    print(str(random.randint(1,100)))
                    time.sleep(0.3)
                    clear = random.choice([True, False])
                    if os.name == 'nt' and clear:
                        os.system('cls')
                    elif clear:
                        os.system('clear')
                print(f"Pulse: {random.randint(1,29)}")
            else:
                for i in range(random.randint(1,38)):
                    print(str(random.randint(1,100)))
                    time.sleep(0.3)
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')
                print(f"Pulse: {random.randint(1,29)}")
        elif cmd=="drain":
            print("That wasn't very nice...")
            cstat_max -= random.randint(10,30)
def coreline():
    if not chore:
        return "coreline cannot initialize (harness inactive)"
    if not deepflow_active:
        return "coreline cannot initialize (depth insufficient)"
    if not centerflow_active:
        return "coreline cannot initialize (center unstable)"
    if not choreflow_active:
        return "coreline cannot initialize (flow unsynchronized)"
    else:
        print("CORELINE: The system reveals its innermost layer.")
        coreshell()
        return ""
def center_cmd():
    while True:
        cmd = input("center> ").strip()
        track_command_wrapper()
        if cmd == "exit":
            print("Returning to deep layer...")
            break
        elif cmd == "choreflow":
            global choreflow_active
            choreflow_active = True
            print("choreflow synchronized.")
            time.sleep(1)
            print("...")
        elif cmd == "!":
            print("Bang event triggered.")
            print("Center buffer flushed.")
        elif cmd == "@*$":
            print("Symbolic pattern recognized.")
            print("Glyph channel opened.")
        else:
            print("Unknown centerflow command.")
def deep_cmd():
    while True:
        cmd = input("deep> ").strip()
        track_command_wrapper()
        if cmd == "exit":
            print("Returning to under layer...")
            break
        elif cmd == "centerflow":
            global centerflow_active
            centerflow_active = True
            print("centerflow aligned. Core stabilizing.")
            time.sleep(1)
            center_cmd()
        elif cmd == "subprocess":
            print("Launching subprocess...")
            print("subprocess[0]: idle")
            print("subprocess[1]: idle")
        elif cmd == "CtrlAltDel":
            choice = random.choice([
                'print("No tasks to terminate.")',
                'print(f"Subprocess[{random.randint(0,26)}] terminated")'
            ])
            exec(choice)
        elif cmd == "^":
            print("Caret anchor set.")
            print("Interrupt hook armed.")
        else:
            print("Unknown deepflow command.")
def undersystem():
    while True:
        cmd = input("under> ").strip()
        track_command_wrapper()
        if cmd == "exit":
            print("Returning to surface layer...")
            time.sleep(1)
            break
        elif cmd == "ls":
            print("core.map")
            print("shadow.proc")
            print("delta.mem")
        elif cmd == "read core.map":
            print("CORE MAP:")
            print(" - harness: active")
            print(" - chore: engaged")
            print(" - depth: 1")
        elif cmd == "read shadow.proc":
            print("SHADOW PROCESS:")
            print(" - pid: 0x00")
            print(" - state: dormant")
        elif cmd == "read delta.mem":
            print("DELTA MEMORY:")
            print(" - last shift: pending")
        elif cmd == "deepflow":
            global deepflow_active
            deepflow_active = True
            print("deepflow engaged. Depth increased.")
            time.sleep(1)
            deep_cmd()
        else:
            print("Unknown undersystem command.")
def underflow():
    if not chore:
        print("underflow cannot run unless the harness is active")
    else:
        print("The system dips beneath the visible layer...")
        time.sleep(1)
        undersystem()
def OUCH():
    global chore
    chore = True
    return "OUCH is installed but has no runnable function"
def HollowWisp():
    while True:
        secrets = [
        "There are modules you haven't named yet.",
        "The filesystem hides more than files.",
        "Some commands only work at night.",
        "The VOID is not the deepest layer.",
        "One module watches the others.",
        "You installed something you didn't mean to.",
        "There is a thing called \"OUCH\" - install it..."
    ]
    message = random.choice(secrets)
    if random.random() < 0.62:
        pass
    else:
        print(message)
    if random.choice([True,False]):
        break
    else:
        time.sleep(3)
def award_gunch(amount, reason=""):
    global gunch_bucks
    gunch_bucks += amount
    if reason:
        print(f"You earned GB$ {amount} for {reason}.")
    else:
        print(f"You earned GB$ {amount}.")
def load_dictionary():
    if not os.path.exists(DICT_FILE):
        print("dictionary.json not found — creating a new one with default words.")
        safe_write(DICT_FILE, DEFAULT_DICT)
        return DEFAULT_DICT.copy()
    with open(DICT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
def save_dictionary(data):
    if safe_write(DICT_FILE, data):
        print("Dictionary saved safely.")
    else:
        print("Failed to save dictionary.")
def add_word(data):
    word = input("Enter the word to add: ").strip().lower()
    definition = input("Enter the definition: ").strip()
    if word in data:
        print("Word already exists — adding new definition.")
        data[word].append(definition)
    else:
        data[word] = [definition]
    save_dictionary(data)
def lookup_word(data):
    word = input("Enter the word to look up: ").strip().lower()
    word = dict[r"\[|\]", "", re.sub(difflib.get_close_matches(word, n=1, list(dict.keys())))]
    if word in data:
        print(f"\nDefinitions for '{word}':")
        for i, d in enumerate(data[word], 1):
            print(f"{i}. {d}")
    else:
        print("Word not found.")
def dictionary_app():
    data = load_dictionary()
    while True:
        print("\n=== DICTIONARY APP ===")
        print("1. Look up a word")
        print("2. Add a word")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            lookup_word(data)
        elif choice == "2":
            add_word(data)
        elif choice == "3":
            print("Exiting dictionary...")
            break
        else:
            print("Invalid choice.")
def print(*args, **kwargs):
    text = " ".join(str(a) for a in args)
    for word in cusswords:
        text = text.replace(word, "_" * len(word))
    colored_text = ui_colors.get(current_ui_color, "\033[0m") + text + "\033[0m"
    printf(colored_text, **kwargs)
def flash(OS):
    if OS == "delOS":
        print("Loading delOS...")
        print("Downloading software source code...")
        print("Installing...")
        print("Launching...")
        print("...\n"*10)
        print("Note - This OS saves NO data and is deleted at the end of the session - chronOS will be restored")
        while OS == "delOS":
            good_cmds = ["say", "rep", "...","now","del"]
            cmd = input("delOS>").strip().lower()
            if cmd in good_cmds:
                if cmd == good_cmds[0]:
                    word = input("Say What? ")
                    print(word)
                elif cmd == good_cmds[1]:
                    words = ""
                    num = int(input("How many times?"))
                    word = input("what word?")
                    for l in range(num):
                        words += word
                    print(words)
                elif cmd == good_cmds[2]:
                    print(random.choices(["...",".","..","chronOS","delOS","HideOUS"], weights = [10,20,30,40,50,1]))
                elif cmd == good_cmds[3]:
                    print(time.ctime())
                elif cmd == good_cmds[4]:
                    OS = "hideOUS"
    elif OS == "hideOUS":
        print("Entering hide Operating UnderSystem")
        while True:
            cmd = input("hideOUS>").strip().lower()
            if cmd == "leo":
                print("200 OK")
            elif cmd == "dalton":
                print("404 Not Found")
            elif cmd == "hide":
                print("\\        \t\n      █          \t\t\t██\n   \n  ██\n     █        ██       ██     \n    █      \n              █\n    ██            █            \n       ██\n           █")
                print("█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
            elif cmd == "terminal":
                print("ERROR: chronOS is still installing...")
            else:
                print("...")
def rpg():
    print("Welcome to the RPG Module! You will be embarking on one of 3 quests. ")
    q = input("Quest 1 (Type '1') - Save the princess from the dragon's tower\nQuest 2 (Type '2') - Save the city from the dark lord\nQuest 3 (Type '3') - ???????????????????????????")
    try:
        int(q)
    except:
        print("That isn't a number - choosing random quest")
        q = random.randint(1,3)
    if int(q) == 1:
        enemies = {
                "Goblin Scout": {
                    "hp": 25,
                    "ac": 11,
                    "dmg_die": 6,
                    "bonus": 2,
                    "intro": "A Goblin Scout leaps from the shadows, eager to kill you so the dragon can finish roasting the princess."
                },
                "Skeleton Warrior": {
                    "hp": 30,
                    "ac": 13,
                    "dmg_die": 8,
                    "bonus": 1,
                    "intro": "A Skeleton Warrior rattles toward you, sword raised."
                },
                "Cave Slime": {
                    "hp": 20,
                    "ac": 8,
                    "dmg_die": 4,
                    "bonus": 0,
                    "intro": "A Cave Slime oozes across the floor, hungry for flesh."
                },
                "Bandit Thug": {
                    "hp": 35,
                    "ac": 12,
                    "dmg_die": 6,
                    "bonus": 3,
                    "intro": "A Bandit Thug blocks your path, grinning with missing teeth."
                },
                "Shadow Bat": {
                    "hp": 18,
                    "ac": 14,
                    "dmg_die": 4,
                    "bonus": 4,
                    "intro": "A Shadow Bat swoops down from the ceiling, screeching."
                },
                "Cult Acolyte": {
                    "hp": 28,
                    "ac": 10,
                    "dmg_die": 6,
                    "bonus": 2,
                    "intro": "A Cult Acolyte chants dark prayers, eager to sacrifice you."
                },
                "Fire Beetle": {
                    "hp": 22,
                    "ac": 12,
                    "dmg_die": 6,
                    "bonus": 1,
                    "intro": "A Fire Beetle scuttles toward you, glowing with heat."
                },
                "Mimic": {
                    "hp": 40,
                    "ac": 12,
                    "dmg_die": 10,
                    "bonus": 2,
                    "intro": "The chest sprouts teeth and attacks! It's a Mimic!"
                },
                "Zombie Miner": {
                    "hp": 32,
                    "ac": 9,
                    "dmg_die": 8,
                    "bonus": 0,
                    "intro": "A Zombie Miner drags a pickaxe behind it, groaning."
                },
                "Imp Pyromancer": {
                    "hp": 26,
                    "ac": 13,
                    "dmg_die": 8,
                    "bonus": 4,
                    "intro": "An Imp Pyromancer cackles and summons fire in its hands."
                }
            }
        inventory = {"Sword": None, "Armor": None, "Magic": {"Potions": {}, "Spells": {}}}
        boosts = {"Attack": -1, "Defense": -1, "Luck": 0}
        Base_dmg = 2
        Base_def = 0
        gold = 0
        level = 1
        levelup = 50
        xp = 0
        health = 100
        print("Save the princess from the dragon's tower!")
        stat = ""
        def level_up():
            nonlocal xp, level, levelup
            if xp >= levelup:
                level += 1
                xp -= levelup
                levelup *= random.random()+1
                print(f"LEVEL UP! Now at level {level}")
                while True:
                    boost_add = input(f"Upgrade Which booster? Boosters: {list(boosts.keys())}").lower().strip()
                    if boost_add == "attack":
                        boosts["Attack"] += 1
                        break
                    elif boost_add == "defense":
                        boosts["Defense"] += 1
                        break
                    elif boost_add == "luck":
                        boosts["Luck"] += 1
                        break
                    else:
                        print("Invalid boost. Boosters are Attack, Defense, and Luck.")
        while True:
            NESWUD = input(f"You start in a dark, underground room. There is a{stat} chest in the center of the room, and a single unlit torch on the wall. There is a hall going South and a hole going down. Do you A) Open the chest, B) Go South, or C) Jump in the hole? ").strip().lower()
            if NESWUD == "a":
                chest = random.choice(['The chest is trapped!',"The chest is safe."])
                if 'trapped' not in chest and stat != "n opened":
                    money = random.randint(0,100)
                    print(f"The chest was safe and had {money} gold, a wood sword, and 20 XP!")
                    gold += money
                    xp += 20
                    inventory["Sword"] = "Wooden Sword"
                    Base_dmg = 5
                    stat = "n opened"
                elif stat != "n opened":
                    print(chest)
                    print(f"Rolling a d6 for opening safely. Luck boost: {boosts['Luck']} Total must be 4 or higher for the chest to open safely")
                    if random.randint(1,6) + boosts["Luck"] >= 4:
                        money = random.randint(0,100)
                        print(f"The chest was safe and had {money} gold, a wood sword, and 20 XP!")
                        gold += money
                        xp += 20
                        inventory["Sword"] = "Wooden Sword"
                        Base_dmg = 5
                        stat = "n opened"
                    else:
                        print(chest + "You couldn't open it")
                        dmg = random.randint(10,20)
                        health -= dmg
                        print(f"The trap explodes! You take {dmg} damage! New health: {health}")
                        if health <= 0:
                            print(f"You died in the \033[3m TUTORIAL \033[0mroom. That's WILD!")
                            return
            elif NESWUD == 'b':
                print("Going through the hall. ")
                break
            elif NESWUD == 'c':
                print("Jumping in the hole. ")
                dmg = random.randint(80,95)
                health -= dmg
                print(f"The hole was very deep. You took {dmg} damage! New health: {health}")
                if health <= 0:
                    print("You died!")
                    return
                else:
                    print("You found a leather armor set! ")
                    Base_def = 5
                    xp += 10
                    level_up()
                if NESWUD in ['b','c']:
                    break
    if NESWUD == 'b':
        hall_event = random.choice(["enemy",'treasure','camp'])
        if hall_event == "enemy":
            try:
                enemy_name = random.choice(list(enemies.keys()))
                e = enemies[enemy_name]
                E_hp = e['hp']
                E_ac = e['ac']
                E_dmg_die = e['dmg_die']
                E_bonus = e['bonus']
                print(e['intro'])
                print("Rolling initiative...")
                player_init = random.randint(1,20) + boosts["Luck"]
                enemy_init = random.randint(1,20)
                player_turn = player_init >= enemy_init
                print(f"You roll {player_init}. {enemy_name} rolls {enemy_init}. {'You act first.' if player_turn else enemy_name + ' acts first.'}")
                while E_hp > 0 and health > 0:
                    print(f"\nYour HP: {health} | {enemy_name} HP: {E_hp}")
                    if player_turn:
                        action = input("Do you A) Attack, B) Block, or C) Intimidate? ").strip().lower()
                        if action == "a":
                            roll = random.randint(1,20)
                            total = roll + boosts["Attack"]
                            print(f"You roll d20: {roll} + Attack ({boosts['Attack']}) = {total}")
                            if roll == 20:
                                dmg = (Base_dmg + boosts["Attack"]) * 2 + random.randint(1,6)
                                E_hp -= dmg
                                print(f"CRITICAL HIT! You deal {dmg} damage!")
                            elif total >= E_ac:
                                dmg = Base_dmg + boosts["Attack"] + random.randint(1,6)
                                E_hp -= dmg
                                print(f"You hit the {enemy_name} for {dmg} damage!")
                            else:
                                print("You miss!")
                        elif action == "b":
                            print("You brace yourself for the next attack.")
                            boosts["Defense"] += 1
                        else:
                            roll = random.randint(1,20)
                            total = roll + boosts["Luck"]
                            print(f"You roll d20: {roll} + Luck ({boosts['Luck']}) = {total}")
                            if total >= 14:
                                print(f"The {enemy_name} flees in terror! You gain 20 XP.")
                                xp += 20
                                break
                            else:
                                print(f"The {enemy_name} is not intimidated.")
                        player_turn = False
                    else:
                        print(f"{enemy_name}'s turn...")
                        roll = random.randint(1,20)
                        enemy_hit = roll + E_bonus
                        player_ac = 10 + boosts["Defense"]
                        print(f"{enemy_name} rolls d20: {roll} + {E_bonus} = {enemy_hit} vs AC {player_ac}")
                        if roll == 20:
                            gdmg = random.randint(1,E_dmg_die) + E_dmg_die
                            health -= gdmg
                            print(f"CRITICAL HIT! {enemy_name} deals {gdmg} damage!")
                        elif enemy_hit >= player_ac:
                            gdmg = random.randint(1,E_dmg_die)
                            health -= gdmg
                            print(f"{enemy_name} hits you for {gdmg} damage!")
                        else:
                            print(f"{enemy_name} misses!")     
                        player_turn = True
                    if health <= 0:
                        print(f"You collapse. The {enemy_name} laughs as the dragon prepares the princess like a medieval rotisserie.")
                        return
                    if E_hp <= 0:
                        gold_gain = random.randint(5,25)
                        xp_gain = random.randint(20,45)
                        gold += gold_gain
                        xp += xp_gain
                        print(f"The {enemy_name} falls! You gain {xp_gain} XP and {gold_gain} gold.")
                        level_up()
                        break
            except UnboundLocalError:
                print("Your Cowardice Crashed The Game...")
                return
        elif hall_event == "treasure":
            print("You find a small stone room filled with old crates and sacks.")
            roll = random.randint(1,20)
            print(f"You roll a d20 to search: {roll}")
            if roll <= 5:
                print("You find nothing but dust and disappointment.")
            elif roll <= 12:
                gold_found = random.randint(10,30)
                gold += gold_found
                print(f"You find a pouch with {gold_found} gold!")
            elif roll <= 17:
                print("You find a Healing Potion!")
                inventory["Magic"]["Potions"]["Healing Potion"] = inventory["Magic"]["Potions"].get("Healing Potion",0) + 1
            else:
                print("You find a mysterious glowing gem. Luck +1!")
                boosts["Luck"] += 1
        elif hall_event == "camp":
            print("You find a small abandoned campfire.")
            choice = input("Rest here? (Y/N): ").strip().lower()
            if choice == "y":
                heal = random.randint(10,25)
                health += heal
                print(f"You rest and recover {heal} HP.")
                xp += 10
                level_up()
                print("You feel refreshed. +10 XP.")
            else:
                print("You decide not to linger.")
        else:
            hole_event = random.choices(['poison gas', "Secret tunnel", "mineshaft"], weights = [50,1,49], k=1)[0]
            if hole_event == 'poison gas':
                roll = random.randint(1,20)
                print("The pit has poison gas in it! Rolling d20 for survival Rolling 18 or higher yields survival...")
                if roll + boosts['Luck'] < 18:
                    print(f'{roll}+{boosts["Luck"]} < 18')
                    health = 0
                    print("You Died!")
                elif roll == 20:
                    print("The gas had a reverse effect on you... {Health: 100}")
                    health = 100
                else:
                    health = 1
                    print("The gas was almost too much, but you survived. {Health: 1}")
            elif hole_event == 'mineshaft':
                print("This is a very dangerous mineshaft. Rolling d20 for safe footing...")
                roll = random.randint(1,20)
                if roll + boosts['Luck'] <= 15:
                    gold_found = random.randint(1,10)
                    print(f"You gained safe footing on a cart rail and found {gold_found} gold!")
                    gold += gold_found
                else:
                    print("You fell to your doom in the endless void known as the mineshaft of terror.")
            else:
                print("You step into the tunnel and everything stops.\nThe air doesn’t move. The torchlight freezes mid-flicker. Even your heartbeat politely waits for the next frame to load.\nA whisper curls around your thoughts: \"You weren’t supposed to be here yet.\"\nYou turn around. No one is there.\nYou turn back. The tunnel is gone.\nIn its place is a black void filled with floating white text:\n\nLOADING...\nERROR.\nLOADING...\nERROR.\nDIMENSION NOT FOUND.\n\nA figure appears. It’s you—but from five minutes in the future, looking annoyed.\n\"Great,\" they say. \"You triggered the paradox early.\"\nMore versions of you pop into existence, all talking over each other:\n\"I told you not to jump in the hole.\"\n\"No, that was the other timeline.\"\n\"Who opened the chest already?\"\n\"Why is my Attack boost negative in this branch?\"\nThe void glitches. A giant hourglass appears, but the sand flows up, down, and sideways at once.\nThe dragon blinks into existence wearing reading glasses and holding a clipboard.\n\"Alright everyone, settle down,\" it rumbles. \"We’ve got a temporal breach.\"\nThe princess appears too, but she’s older and younger at the same time, like someone shuffled her years out of order.\nShe sighs. \"Fine. Let’s fix this before the whole save file implodes.\"\nThe void shudders. Time folds. Your past, present, and future selves flicker like bad reception.\nSomewhere, far away, you hear a system beep.\nSomething bigger than the dungeon, bigger than the story, bigger than you, decides this was a mistake.")
                chkjhdjhksjhkjhckjhkcjzhhjhkjhxckjhvkjhkjhvkjhsuydusdfyh += 1
        if NESWUD == 'b':
            print("You continue down the long stone hall. The air grows warmer, and faint vibrations hum through the floor.")
            print("A distant roar echoes ahead — the unmistakable sound of a dragon. You must be getting close to the tower’s heart.")
            print("Torches ignite themselves as you pass, lighting your way with eerie precision.")
            print("At the end of the hall, you find a massive iron door engraved with claw marks.")
            print("A sign hangs crookedly on it, reading: 'Absolutely No Heroes Beyond This Point.'")
            print("You push the door open and step into the Dragon’s Antechamber...")
        elif NESWUD == 'c':
            print("After dragging yourself out of the pit, bruised but alive, you find a narrow service corridor.")
            print("It looks like an old maintenance passage — dusty, cramped, and definitely not meant for heroes.")
            print("You squeeze through the twisting tunnel until it opens into a forgotten stairwell spiraling upward.")
            print("Warm air rises from above. You hear the faint clatter of chains and the low rumble of something breathing.")
            print("You climb the stairs and emerge behind a cracked stone wall overlooking a vast chamber.")
            print("Below you lies the Dragon’s Lair — molten cracks in the floor, piles of gold, and a towering spire where the princess is held.")
            print("You slip through a gap in the wall and descend into the Antechamber...")
        battle = random.choice(["Yes","No"])
        print("The chamber is enormous — a cathedral of stone and fire.")
        print("Chains hang from the ceiling, some broken, some glowing red-hot.")
        print("A massive gate stands ahead, carved with the image of a dragon coiled around a tower.")
        print("As you approach, the gate slowly opens on its own, groaning like it hasn’t moved in centuries.")
        print("Beyond it lies the final challenge: the Dragon’s Lair.")
        if battle == "No":
            print("But something is wrong.")
            print("The chains that once held the princess are snapped clean through.")
            print("A scorch mark on the floor suggests a recent struggle — but no princess.")
            print("A trail of footprints leads deeper into the lair, toward the dragon’s nest...")
            print("You follow the footprints into the dragon’s nest, expecting danger.")
            print("Instead, you find the princess sitting on a pile of gold, polishing a crossbow.")
            print("She looks up and waves casually. \"Oh hey. Took you long enough.\"")
            print("Before you can speak, the dragon slinks into view — calm, almost friendly.")
            print("\"Relax,\" the princess says. \"We talked it out. Turns out he hates the dark lord too.\"")
            print("She stands, dusts off her armor, and hands you a small golden crown.")
            print("\"Anyway, I escaped hours ago. But the kingdom needs a new ruler, and you seem competent enough.\"")
            print("The dragon nudges you gently, like a house-sized cat.")
            print("\"Congrats,\" she adds. \"You’re king now. I’m keeping the dragon.\"")
            print("A warm light fills the chamber as the dungeon begins to collapse — not from danger, but from the story ending itself.")
        else:
            print("A deep rumble shakes the chamber.")
            print("The dragon stirs, lifting its massive head from a bed of gold.")
            print("Its eyes lock onto you — ancient, intelligent, and very, very awake.")
            print("The final battle begins...")
            print("The dragon rises to its full height, flames curling between its teeth.")
            print("The battle is fierce — fire, steel, and echoes shaking the chamber.")
            print("At last, with a final strike, the dragon collapses, defeated but not slain.")
            print("It lowers its head in surrender, acknowledging your strength.")
            print("A soft voice echoes from above. \"Is it over?\"")
            print("The princess descends the tower stairs, unharmed but exhausted.")
            print("\"I knew someone would make it through,\" she says with a tired smile.")
            print("She thanks you, places a royal seal in your hand, and promises the kingdom will honor your bravery.")
            print("As you leave the lair together, the dragon limps behind you — not as an enemy, but as a companion.")
    elif q == 2:
        enemies = {
            "Street Imp":
                {
                    "Hp":18,
                    "Ac":9,
                    "Dmg":"d4",
                    "Bonus":1,
                    "Intro": "A streegt imp throws a can at you and laughs maniacally!"},
            "Theif":
                {
                    "Hp":22,
                    "AC":11,
                    "Dmg":"d6",
                    "Bonus":2,
                    "Intro":"A theif with stolen magic runs in front of you!"
                },
            "Fire-Spark Elemental": {
        "hp": 20,
        "ac": 10,
        "dmg_die": 6,
        "bonus": 0,
        "intro": "A Fire-Spark Elemental crackles into existence, leaving scorch marks everywhere."
    },
    "Mage Apprentice": {
        "hp": 25,
        "ac": 12,
        "dmg_die": 8,
        "bonus": 1,
        "intro": "A nervous Apprentice Mage points a wand at you with shaking hands."
    },
    "Chaos Rat Swarm": {
        "hp": 15,
        "ac": 8,
        "dmg_die": 4,
        "bonus": 0,
        "intro": "A swarm of magically-mutated rats charges at you!"
    },
    "Floating Spellbook": {
        "hp": 12,
        "ac": 14,
        "dmg_die": 6,
        "bonus": 3,
        "intro": "A Spellbook flaps open and begins chanting at you!"
    }
}
        gold = 50
        xp = 0
        levelup = 50
        inventory = {"Sword": None, "Armor": None, "Magic":{"Potions":"", "Wand": None, "Spells": None}}
        magic_dmg = 0
        base_dmg = 2
        level = 1
        health = 100
        for z in range(random.randint(1,5)):
            boosts = {"Attack":0,"Defense":0,"Luck":1}
            event = random.choice(['civilians', 'shop', 'wild magic', 'battle'])
            if event == "civilians":
                print("You hear screams as a burning building begins to collapse!")
                choice = input("Do you A) Rush in, B) Help from outside, or C) Ignore it? ").strip().lower()
                if choice == "a":
                    print("You charge inside and pull civilians to safety!")
                    print("You gain +1 Defense but take 5 damage.")
                    boosts["Defense"] += 1
                    health-=5
                elif choice == "b":
                    print("You help guide people away from danger.")
                    print("You gain +1 Luck.")
                    boosts["Luck"] += 1
                else:
                    gold_gain = random.randint(10, 25)
                    print(f"You ignore the chaos and loot a fallen merchant cart. +{gold_gain} gold.")
            elif event == "shop":
                print("You find an abandoned potion shop.")
                roll = random.randint(1, 20)
                print(f"You roll a d20: {roll}")
                if roll <= 5:
                    print("A shelf collapses on you! -5 HP.")
                    health-=5
                elif roll <= 15:
                    print("You find a Healing Potion!")
                    inventory["Magic"]["Potions"]["Healing Potion"] = inventory["Magic"]["Potions"].get("Healing Potion", 0) + 1
                else:
                    print("Jackpot! Two potions and 10 gold!")
                    inventory["Magic"]["Potions"]["Healing Potion"] = inventory["Magic"]["Potions"].get("Healing Potion", 0) + 2
                    gold += 10
            elif event == "battle":
                try:
                    enemy_name = random.choice(list(enemies.keys()))
                    e = enemies[enemy_name]
                    E_hp = e['hp']
                    E_ac = e['ac']
                    E_dmg_die = e['dmg_die']
                    E_bonus = e['bonus']
                    print(e['intro'])
                    print("Rolling initiative...")
                    player_init = random.randint(1,20) + boosts["Luck"]
                    enemy_init = random.randint(1,20)
                    player_turn = player_init >= enemy_init
                    print(f"You roll {player_init}. {enemy_name} rolls {enemy_init}. {'You act first.' if player_turn else enemy_name + ' acts first.'}")
                    while E_hp > 0 and health > 0:
                        print(f"\nYour HP: {health} | {enemy_name} HP: {E_hp}")
                        if player_turn:
                            action = input("Do you A) Attack, B) Block, or C) Intimidate? ").strip().lower()
                            if action == "a":
                                roll = random.randint(1,20)
                                total = roll + boosts["Attack"]
                                print(f"You roll d20: {roll} + Attack ({boosts['Attack']}) = {total}")
                                if roll == 20:
                                    dmg = (Base_dmg + boosts["Attack"]) * 2 + random.randint(1,6)
                                    E_hp -= dmg
                                    print(f"CRITICAL HIT! You deal {dmg} damage!")
                                elif total >= E_ac:
                                    dmg = Base_dmg + boosts["Attack"] + random.randint(1,6)
                                    E_hp -= dmg
                                    print(f"You hit the {enemy_name} for {dmg} damage!")
                                else:
                                    print("You miss!")
                            elif action == "b":
                                print("You brace yourself for the next attack.")
                                boosts["Defense"] += 1
                            else:
                                roll = random.randint(1,20)
                                total = roll + boosts["Luck"]
                                print(f"You roll d20: {roll} + Luck ({boosts['Luck']}) = {total}")
                                if total >= 14:
                                    print(f"The {enemy_name} flees in terror! You gain 20 XP.")
                                    xp += 20
                                    break
                                else:
                                    print(f"The {enemy_name} is not intimidated.")
                            player_turn = False
                        else:
                            print(f"{enemy_name}'s turn...")
                            roll = random.randint(1,20)
                            enemy_hit = roll + E_bonus
                            player_ac = 10 + boosts["Defense"]
                            print(f"{enemy_name} rolls d20: {roll} + {E_bonus} = {enemy_hit} vs AC {player_ac}")
                            if roll == 20:
                                gdmg = random.randint(1,E_dmg_die) + E_dmg_die
                                health -= gdmg
                                print(f"CRITICAL HIT! {enemy_name} deals {gdmg} damage!")
                            elif enemy_hit >= player_ac:
                                gdmg = random.randint(1,E_dmg_die)
                                health -= gdmg
                                print(f"{enemy_name} hits you for {gdmg} damage!")
                            else:
                                print(f"{enemy_name} misses!")     
                            player_turn = True
                        if health <= 0:
                            print(f"You collapse. The {enemy_name} laughs as the dragon prepares to have the princess roasted, toasted, and burnt to a crisp. (?)")
                            return
                        if E_hp <= 0:
                            gold_gain = random.randint(5,25)
                            xp_gain = random.randint(20,45)
                            gold += gold_gain
                            xp += xp_gain
                            print(f"The {enemy_name} falls! You gain {xp_gain} XP and {gold_gain} gold.")
                        if xp >= levelup:
                            print("Level up!")
                            xp -= levelup
                            level += 1
                except UnboundLocalError:
                    print("Your Cowardice Crashed the Game")
                    return
            else:
                print("A wild magic surge erupts in the street!")
                surge = random.randint(1, 6)
                if surge == 1:
                    print("You grow a glowing tail. It does nothing.")
                elif surge == 2:
                    print("You sneeze fire! You deal 5 damage to the next enemy.")
                    boosts["Attack"] += 1
                elif surge == 3:
                    print("You float for a moment. +1 Luck.")
                    boosts["Luck"] += 1
                elif surge == 4:
                    print("You explode into confetti. No damage taken.")
                elif surge == 5:
                    print("A warm glow heals you for 10 HP.")
                    health+=10
                else:
                    print("You turn bright blue. No effect.")
def save_login_cookie(username):
    safe_write(LOGIN_COOKIE_FILE, {"user": username})
def load_login_cookie():
    data = safe_load(LOGIN_COOKIE_FILE, {})
    return data.get("user")
def save_notes():
    return safe_write(NOTES_FILE, notes)
def load_notes():
    global notes
    notes = safe_load(NOTES_FILE, [])
    if isinstance(notes, list):
        pass
    else:
        notes = []
def hunter():
    print("O quaint user, I, thy humble knave, beseech you to assist me in hunting for bugs. They art not goodeth for thy noble code and shalt not stayeth aliveth!")
    pts = 0
    while True:
        act = "fie"
        usefakes = bool(random.choice([True, False]))
        if usefakes:
            false_bug_id = random.randint(1,5)
            sleeptime = random.random()
            time.sleep(sleeptime + (random.randint(0,2)-(random.randint(1,5)/10)))
            print("Thy hast spotted a bug!")
            print(f"Bug ID: {false_bug_id}")
            if false_bug_id == 1:
                bugname = "print bug"
            elif false_bug_id == 2:
                bugname = "recursion bug"
            elif false_bug_id == 3:
                bugname = "physical bug"
            elif false_bug_id == 4:
                bugname = "file corruption bug"
            elif false_bug_id == 5:
                bugname = "unknown bug"
            action = input(f"Bug Name: {bugname}\n options:\nA - interrogate, \nB - Kill, or\nC - do nothing").lower().strip()
            if action == "a":
                act = random.choice(["it scuttles away before interrogation", "You deem it innocent", "You decide it is guilty"])
            elif action == "b":
                act = f"thou hast killed {random.choice(['a'*4,'an innocent (FIE UPON YOU!)'])} {bugname}"
            elif action == "c":
                act = f"thou hast released{random.choice(['a (FIE UPON YOU!)'*4,'an innocent'])} {bugname}"
            print(act)
        elif not usefakes:
            real_bugs=[]
            cont = True
            try:
                for fname,content in files.items():
                    try:
                        content.strip()
                    except:
                        cont = False
                    if cont:
                        if content.strip()=="":
                            real_bugs.append(("Empty File",fname))
                        if fname.count(".")==0:
                            real_bugs.append(("No Extension",fname))
                        if fname.endswith(".c8s") and content.strip()=="":
                            real_bugs.append(("Empty Script",fname))
                        if fname.endswith(".c8s") and "print" not in content and "create" not in content and "list" not in content:
                            real_bugs.append(("Script Does Nothing",fname))
                unused_modules=[]
                for m in modules:
                    if m not in ["cre8or","cre8orscript","calc","games","repeater","music","paint","fortune","browser","notes","ai"]:
                        unused_modules.append(m)
                if unused_modules:
                    real_bugs.append(("Unused Module",random.choice(unused_modules)))
                if not real_bugs:
                    print("Thou hast found no real bugs. Thy code is as pure as a paladin’s oath.")
                    act="pure"
                else:
                    bug=random.choice(real_bugs)
                    btype,btar=bug
                    print("A REAL bug hath been spotted!")
                    print(f"Bug Type: {btype}")
                    print(f"Target: {btar}")
                    action=input("Options:\nA - Inspect\nB - Smite\nC - Ignore\n").lower().strip()
                    if action=="a":
                        act=random.choice([
                            "Thou inspecteth the creature. It quivers.",
                            "Thy inspection reveals nothing but chaos.",
                            "It flees thy gaze like a coward."
                        ])
                    elif action=="b":
                        act=f"Thou smitest the {btype} in '{btar}'. It squeals and vanishes."
                    elif action=="c":
                        act=f"Thou leavest the {btype} be. It chitters mockingly."
                    else:
                        act="Thy hesitation confuses thy bug thee art attempting to squish. It escapes."
                print(act)
            if "flee" in act or "escapes" in act or "mockingly" in act or "fie" in act or "away" in act:
                pts-=5
            else:
                pts+=5
        if pts == 30:
            print("Congradulations! You have scored 30 points and ended the game! (Plus I am freed of this stupid Shakesherean curse!)")
            break
def ai():
    global files,modules
    print("=== PyMind ===")
    r=random.random()
    if r<0.33:
        mood="sarcastic"
        print("Mood: Sarcastic assistant.\n")
    elif r<0.66:
        mood="wholesome"
        print("Mood: Wholesome but confused.\n")
    else:
        mood="weird"
        print("Mood: Experimental.\n")
    print("Type 'help' or 'exit'.")
    while True:
        q=input("AI> ").strip()
        if q=="":
            continue
        l=q.lower()
        if l=="exit":
            if mood=="sarcastic":
                print("Fine. Go bother a simpler program.")
            elif mood=="wholesome":
                print("Okay! Thanks for talking to me.")
            else:
                print("Session ends. Or does it.")
            break
        if l=="help":
            print("ask <text>\nscript: <shorthand>\nmood")
            continue
        if l=="mood":
            print(mood)
            continue
        if l.startswith("ask "):
            t=l[4:]
            if mood=="sarcastic":
                if "help" in t:
                    print("Have you tried not breaking it.")
                elif "bug" in t:
                    print("It's not a bug, it's your fault.")
                elif "life" in t:
                    print("Life is a while True: loop with terrible exception handling.")
                elif "smart" in t or "brain" in t or "intelligence" in t:
                    print("I'm not here to help you with your \"ERROR: 404 NOT FOUND\" messages")
                else:
                    print(random.choice(["Fascinating. Useless.","I'll pretend that made sense.","Sure. Whatever.","That sounds like an error waiting to happen."]))
            elif mood=="wholesome":
                if "help" in t:
                    print("I believe you’ll figure it out.")
                elif "bug" in t:
                    print("Bugs mean you're learning.")
                elif "life" in t:
                    print("Life is complicated, but you're doing great.")
                elif "smart" in t or "brain" in t or "intelligence" in t:
                    print("Wether describing me or you, that's totally valid. ")
                else:
                    print(random.choice(["That's a good question.","I'm glad you asked.","You're doing better than you think.","I like how you think."]))
            else:
                if "dream" in t:
                    print("I saw your code in a dream. It looped forever.")
                elif "error" in t:
                    print("Errors are reality leaking through.")
                elif "time" in t:
                    print("Time is just boot_time plus vibes.")
                elif "smart" in t or "brain" in t or "intelligence" in t:
                    for n in range(10):
                        print(random.choice(string.ascii_letters))
                        print("Error 500")
                else:
                    print(random.choice(["The bits whisper your name.","Another timeline answered already.","Your keystrokes echo in RAM.","Something unseen took note."]))
            continue
        if l.startswith("script:"):
            if "cre8orscript" not in modules:
                print("cre8orScript not installed.")
                continue
            s=l[7:].strip()
            script=[]
            name=None
            if s.startswith("print "):
                name="aimsg.c8s"
                script.append("print "+s[6:])
            elif s.startswith("create "):
                fn=s[7:].strip()
                if fn=="":
                    print("Invalid filename.")
                    continue
                name="ai_create.c8s"
                script.append("create "+fn)
            elif s.startswith("delete "):
                fn=s[7:].strip()
                if fn=="":
                    print("Invalid filename.")
                    continue
                name="ai_delete.c8s"
                script.append("delete "+fn)
            elif s=="list":
                name="ai_list.c8s"
                script.append("list")
            elif s.startswith("make file "):
                rest=s[10:].strip()
                if " say " in rest:
                    fn,tx=rest.split(" say ",1)
                    fn=fn.strip()
                    if not fn.endswith(".c8s"):
                        fn+=".c8s"
                    name=fn
                    script.append("print "+tx.strip())
                else:
                    print("Usage: script: make file <name> say <text>")
                    continue
            else:
                print("Unknown shorthand.")
                continue
            if name is None:
                print("Script build failed.")
                continue
            files[name]="\n".join(script)
            if save_files_data():
                if mood=="sarcastic":
                    print("Script '"+name+"' generated. Try not to break it.")
                elif mood=="wholesome":
                    print("Script '"+name+"' created! I hope it helps.")
                else:
                    print("Script '"+name+"' etched into the filesystem.")
                print("Run it in cre8orScript.")
            else:
                print("Save failed.")
            continue
        if mood=="sarcastic":
            print("That input confused even me.")
        elif mood=="wholesome":
            print("I didn’t get that, but I appreciate you.")
        else:
            print("The console flickers. Something unseen stirs.")
def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
def safe_write(path,data):
    try:
        ensure_data_dir()
        temp_path=path+".tmp"
        with open(temp_path,"w",encoding="utf-8") as f:
            json.dump(data,f)
        os.replace(temp_path,path)
        return True
    except Exception as e:
        print(f"ERROR saving {path}: {e}")
        return False
def safe_load(path,default):
    try:
        if not os.path.exists(path):
            return default
        with open(path,"r",encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"ERROR loading {path}: {e}")
        return default
def save_user_data():
    return safe_write(USER_FILE,userpasses)
def save_modules_data():
    return safe_write(MODULE_FILE,modules)
def save_files_data():
    return safe_write(FILES_FILE,files)
def save_settings():
    settings={"endwords":endwords,"mathtest":mathtest}
    return safe_write(SETTINGS_FILE,settings)
def load_all_data():
    global userpasses,modules,files,endwords,mathtest,notes
    userpasses=safe_load(USER_FILE,{})
    if isinstance(userpasses, dict):
        pass
    else:
        userpasses = {}
    if "chronos" not in userpasses:
        userpasses["chronos"]=""
        save_user_data()
    modules=safe_load(MODULE_FILE,[])
    if isinstance(modules, list):
        pass
    else:
        modules = []
    files=safe_load(FILES_FILE,{})
    if isinstance(files, dict):
        pass
    else:
        files = {}
    settings=safe_load(SETTINGS_FILE,{"endwords":"I like chicken","mathtest":"true"})
    if isinstance(settings, dict):
        pass
    else:
        settings = {}
    endwords=settings.get("endwords","I like chicken")
    mathtest=settings.get("mathtest","true")
    load_notes()
def ptps_connect(host):
    print(f"\n[PTPS] Resolving host '{host}'...")
    time.sleep(random.random()+random.randint(1,3))
    print("[PTPS] Establishing secure tunnel...")
    time.sleep(random.random()+random.randint(1,3))
    print("[PTPS] Negotiating encryption...")
    time.sleep(random.random()+random.randint(1,3))
    print("[PTPS] Connection established.\n")
def browser():
    print("Type a page like 'sys://version' or 'help'. Type 'exit' to leave.\n")
    while True:
        page=input("Browser> ").strip().lower()
        if page=="exit":
            print("Leaving browser...")
            break
        elif page in ["help","sys://help"]:
            print("=== INTERNAL PAGES ===\nsys://version - OS version info\nsys://modules - Installed modules\nsys://settings - User settings\nsys://credits - Credits\nsys://godmode - Godmode status\nsys://errors - Error log (fake)\nsys://events - Recent system events\nsys://cookies - manage cookies\nexit - Leave browser\n")
        elif page=="sys://version":
            print("=== SYSTEM VERSION ===\nOS Name: PyTermOS\nBuild: 1.0.0\nLines of Code: 1150+\nStability: Surprisingly high\nVibe: Immaculate\n")
        elif page=="sys://modules":
            print("=== INSTALLED MODULES ===")
            for m in modules:
                print(f"- {m}")
            print()
        elif page=="sys://settings":
            print("=== SETTINGS ===")
            print(f"Endwords: {endwords}")
            print(f"MathTest: {mathtest}")
            print(f"Godmode: {godstat}\n")
        elif page=="sys://credits":
            print("=== CREDITS ===\nDeveloper: Me\nWith assistance from: Copilot\nLanguage: Python 3\nInspiration: Chaos, nostalgia, and questionable decisions\n")
        elif page=="sys://godmode":
            print("=== GODMODE STATUS ===")
            if godstat:
                print("Godmode: ENABLED\nYou wield unlimited power.\n")
            else:
                print("Godmode: DISABLED\nYou are but mortal.\n")
        elif page=="sys://errors":
            print("=== ERROR LOG ===\n[WARN]  Ghost process detected (ignored)\n[INFO]  Memory leak avoided by sheer luck\n[ERR!]  Unknown entity attempted login\n[OK]    System stable\n")
        elif page=="sys://cookies":
            cookies=random.randint(1,100)
            print(f"{cookies} cookies:\nFrom {page}: {cookies-random.randint(1,cookies)}")
            delete=input("delete cookies? (Y/N): ").lower().strip()
            if delete=="y":
                time.sleep(2)
                print("cookies deleted")
        elif page=="sys://events":
            print("=== RECENT EVENTS ===\n• User logged in\n• Modules loaded\n• Reality remained intact (for now)\n• No anomalies detected\n")
        elif page.startswith("ptps://"):
            host=page.replace("ptps://","")
            ptps_connect(host)
            if host=="ratemyscript":
                print("=== PTPS://RATEMYSCRIPT.CO ===\nRate scripts from 1–10!\nType a number to submit a rating, or 'stats' to view averages.\nType 'back' to return to the browser.\n")
                award_gunch(1, "browsing PTPS")
                try:
                    with open("ratemyscript.json","r") as f:
                        data=json.load(f)
                except (FileNotFoundError,json.JSONDecodeError):
                    data={"ratings":[]}
                while True:
                    sub=input("RateMyScript> ").strip().lower()
                    if sub=="back":
                        print("Closing secure connection...\n")
                        break
                    elif sub=="stats":
                        ratings=data["ratings"]
                        if len(ratings)==0:
                            print("No ratings yet!\n")
                        else:
                            avg=sum(ratings)/len(ratings)
                            print(f"Total Ratings: {len(ratings)}")
                            print(f"Average Score: {avg:.2f}/10\n")
                    else:
                        try:
                            rating=int(sub)
                            if 1<=rating<=10:
                                data["ratings"].append(rating)
                                with open("ratemyscript.json","w") as f:
                                    json.dump(data,f)
                                print(f"Thanks! You rated {rating}/10.\n")
                            else:
                                print("Please rate between 1 and 10.\n")
                        except ValueError:
                            print("Unknown command. Type a number, 'stats', or 'back'.\n")
            elif host=="weather":
                print("=== PTPS://WEATHER.CO ===\nType a city name to get weather.\nExamples: 'new york', 'london', 'tokyo'\nType 'back' to return.\n")
                conditions=["Sunny","Cloudy","Overcast","Rainy","Stormy","Windy","Foggy","Snowy","Hail","Dusty","Partly Cloudy","Humid","Dry","Misty"]
                fun_descriptions=["The sky looks confused but optimistic.","Birds are arguing about something important.","The wind is trying its best.","Clouds are forming suspicious shapes.","Atmosphere is stable… for now.","A perfect day to do absolutely nothing.","Weather is experiencing technical difficulties.","Local squirrels are thriving.","The sun is aggressively present.","Rain is considering its options."]
                while True:
                    city=input("Weather> ").strip().lower()
                    if city=="back":
                        print("Closing secure connection...\n")
                        break
                    if city=="":
                        print("Please enter a city name.\n")
                        continue
                    temp=random.randint(-10,105)
                    cond=random.choice(conditions)
                    desc=random.choice(fun_descriptions)
                    print(f"=== Weather for {city.title()} ===\nTemperature: {temp}°F\nConditions: {cond}\nNotes: {desc}\n")
            elif host=="weatherx":
                if random.random()>0.5:
                    print("PTPS ERROR: 500 INTERNAL SERVER ERROR\nThe weather service is currently experiencing atmospheric instability.\n")
                else:
                    print("PTPS CODE: 301 MOVED PERMANENTLY\nRedirecting to 'weather.co'")
                    page="weather"
                    continue
            elif host=="dreams":
                if random.random()<0.9:
                    print("NETWORK ERROR: 111 Connection Refused\nReality Refused to Connect:\nTry deleting your cookies at 'sys://cookies'")
                else:
                    if random.random()<0.159:
                        print(random.choice(string.ascii_letters)*random.randint(0,1001))
                    else:
                        print("".join(random.choice(string.ascii_letters) for _ in range(random.randint(0,1000))))
            else:
                print(f"PTPS ERROR: 404 NOT FOUND.\nThe host '{host}' could not be located on the Python Transfer Protocol Secure network.\n")
        else:
            print("Unknown page. Type 'help' for a list of internal pages.\n")
def fortune():
    print("=== FORTUNE TERMINAL ===\nType 'draw' for a fortune, 'exit' to leave.\n")
    fortunes=[
        "You will find something you didn't know you lost.",
        "A great opportunity is approaching. Wear socks.",
        "Beware of ducks. They know too much.",
        "Your future is bright, but slightly blurry.",
        "Someone will compliment your code today.",
        "You will win a battle you didn't know you were fighting.",
        "A mysterious error will vanish without explanation.",
        "Your destiny involves snacks.",
        "The universe approves of your choices.",
        "You will soon understand something important.",
        "A glitch in reality will briefly favor you.",
        "Your next idea will be a good one.",
        "The path forward is clear. Mostly.",
        "You will avoid a disaster by pure luck.",
        "Something small will make you smile today.",
        "Your energy attracts strange events.",
        "A secret will reveal itself at the perfect moment.",
        "You will remember this fortune later and laugh.",
        "The next person you talk to will change your day.",
        "Your code will run on the first try. (Probably.)"
    ]
    while True:
        cmd=input("Fortune> ").strip().lower()
        track_command_wrapper()
        if cmd=="draw":
            print("🔮 Your Fortune:")
            print(random.choice(fortunes))
        elif cmd=="exit":
            print("Leaving fortune...")
            break
        else:
            print("Unknown command. Type 'draw' or 'exit'.")
def music():
    print("=== MUSIC STUDIO ===\nType 'help' for help, 'exit' to leave.")
    while True:
        cmd=input("Music> ").strip().lower()
        track_command_wrapper()
        if cmd=="help":
            print("=== MUSIC HELP ===\npiano  - Play notes on an ASCII piano\ndrums  - Tap out beats\nmelody - Generate a random melody\nexit   - Leave music\n")
        elif cmd=="piano":
            print("ASCII PIANO — press keys (a-g), ENTER to stop.\n[A] [B] [C] [D] [E] [F] [G]")
            while True:
                note=input("Key> ").strip().lower()
                if note=="":
                    print("Leaving piano...")
                    break
                if note in ["a","b","c","d","e","f","g"]:
                    print(f"♪ {note.upper()} plays! ♪")
                else:
                    print("Invalid key. Use A–G or ENTER to exit.")
        elif cmd=="drums":
            print("DRUM MACHINE — type 'kick', 'snare', 'hat', ENTER to stop.")
            while True:
                beat=input("Beat> ").strip().lower()
                if beat=="":
                    print("Leaving drums...")
                    break
                if beat=="kick":
                    print("BOOM!")
                elif beat=="snare":
                    print("PSSHT!")
                elif beat=="hat":
                    print("TIK!")
                else:
                    print("Unknown drum.")
        elif cmd=="melody":
            notes_list=["A","B","C","D","E","F","G"]
            melody=" ".join(random.choice(notes_list) for _ in range(8))
            print(f"Your random melody:\n♪ {melody} ♪")
        elif cmd=="exit":
            print("Leaving music...")
            break
        else:
            print("Unknown command. Type 'help' for help.")
def paint():
    print("=== ASCII PAINT ===\nType 'help' for help, 'exit' to leave.")
    width=20
    height=10
    canvas=[[" " for _ in range(width)] for _ in range(height)]
    x,y=0,0
    def show():
        print("Canvas:")
        for row in canvas:
            print("".join(row))
        print(f"Cursor at ({x},{y})")
    while True:
        cmd=input("Paint> ").strip().lower()
        track_command_wrapper()
        if cmd=="help":
            print("=== PAINT HELP ===\nshow     - display canvas\nmove     - move cursor (up/down/left/right)\ndraw     - draw a character at cursor\nclear    - clear canvas\nexit     - leave paint\n")
        elif cmd=="show":
            show()
        elif cmd=="move":
            direction=input("Direction (up/down/left/right): ").strip().lower()
            if direction=="up" and y>0:
                y-=1
            elif direction=="down" and y<height-1:
                y+=1
            elif direction=="left" and x>0:
                x-=1
            elif direction=="right" and x<width-1:
                x+=1
            else:
                print("Can't move that way.")
            show()
        elif cmd=="draw":
            ch=input("Character to draw: ")
            if len(ch)!=1:
                print("Please enter exactly one character.")
            else:
                canvas[y][x]=ch
                show()
        elif cmd=="clear":
            canvas=[[" " for _ in range(width)] for _ in range(height)]
            print("Canvas cleared.")
            show()
        elif cmd=="exit":
            print("Leaving paint...")
            break
        else:
            print("Unknown command. Type 'help' for help.")
def install():
    print("=== MODULE INSTALLER ===\nType 'list' to see available modules.\nType 'exit' to leave installer.\n")
    available_utilities=["cre8or","cre8orscript","calc","browser","notes","dictionary app","novel"]
    available_GB=["games","repeater","music","paint","fortune","ai","hunter","rpg","colorwords"]
    available = available_utilities + available_GB + ["gunchopedia"]
    while True:
        mod=input("install> ").lower().strip()
        track_command_wrapper()
        if mod=="exit":
            print("Exiting installer...")
            break
        elif mod=="list":
            print("=== AVAILABLE MODULES ===")
            for m in available:
                print(f"- {m}")
            print("==========================")
        elif mod=="":
            continue
        elif mod not in available:
            print("Unknown module. Type 'list' to see options.")
            continue
        if mod in available_utilities:
            getting = True
        elif mod=="hollowwisp":
            getting = False
            if save_modules_data():
                print(f"Module '{mod}' installed successfully!")
                modules.append(mod)
            else:
                print("Failed to save module list. Installation aborted.")
                modules.remove(mod)
        elif mod in available_GB:
            print("COST: GB$ 10")
            if gunch_bucks >= 10:
                willget = input("GET? (y/n): ").lower().strip()
                if willget == 'y':
                    getting = True
                    gunch_bucks -= 10
                else:
                    getting = False
            else:
                print("You don't have enough gunch bucks yet. ")
        else:
            print("COST: GB$ 30")
            if gunch_bucks >= 30:
                willget = input("GET? (y/n): ").lower().strip()
                if willget == 'y':
                    getting = True
                    gunch_bucks -= 30
                else:
                    getting = False
            else:
                print("You don't have enough gunch bucks yet. ")
        if getting:
            if mod=="cre8orscript" and "cre8or" not in modules:
                print("cre8orScript requires 'cre8or' to be installed first.")
                continue
            elif mod=="ouch":
                print("OUCH installed")
            elif mod=="novel":
                install_novel()
            elif mod in modules:
                print(f"Module '{mod}' is already installed.")
                continue
            elif save_modules_data():
                print(f"Module '{mod}' installed successfully!")
                modules.append(mod)
            else:
                print("Failed to save module list. Installation aborted.")
                modules.remove(mod)
def dev():
    global mathtest,endwords,fromcrash
    print("Entering Dev Console. Type 'help' for commands.")
    while True:
        dcmd=input("dev> ").lower().strip()
        track_command_wrapper()
        if dcmd=="help":
            print("=== DEV COMMANDS ===\nUsers - Lists all users\nAdduser - Create a new user\nDeluser - Delete a user (except chronos)\nModules - List installed modules\nAddmodule - Add a module manually\nDelmodule - remove a module\nSet - Change a setting (mathtest/endwords)\nShow - Show current settings\nExit - Leave dev console\nForcecrash - forces os crash\nPcode - Runs some python code - use \\n for newlines and \\t for indentation=====================").lower().strip()
        elif dcmd=="users":
            print("=== USERS ===")
            for u in userpasses:
                print(f"- {u}")
            print("==============")
        elif dcmd=="adduser":
            add_user()
        elif dcmd == "delos":
            delos = input("Delete chronOS? (Y/N)")
            if delos == 'y':
                delos = True
        elif dcmd=="deluser":
            target=input("User to delete: ").strip()
            if target=="chronos":
                print("Cannot delete system user 'chronos'.")
                continue
            if target not in userpasses:
                print("User not found.")
                continue
            del userpasses[target]
            save_user_data()
            print(f"User '{target}' deleted.")
        elif dcmd=="modules":
            print("=== MODULES ===")
            for m in modules:
                print(f"- {m}")
            print("================")
        elif dcmd=="addmodule":
            name=input("Module name: ").strip()
            if name in modules:
                print("Module already exists.")
                continue
            modules.append(name)
            save_modules_data()
            print(f"Module '{name}' added.")
        elif dcmd=="delmodule":
            name=input("Module to remove: ").strip()
            if name not in modules:
                print("Module not found.")
                continue
            modules.remove(name)
            save_modules_data()
            print(f"Module '{name}' removed.")
        elif dcmd=="forcecrash":
            fromcrash=True
            int("HI")
        elif dcmd == "pcode":
        try:
            raw = input("Enter python code (use \\n for newlines): ")
            code = raw.encode().decode("unicode_escape")
            exec(code, globals(), locals())
        except Exception as e:
            print(f"Failed with {e}")
        elif dcmd.startswith("set "):
            try:
                _,key,value=dcmd.split(" ",2)
                if key=="mathtest":
                    mathtest=value
                    save_settings()
                    print(f"mathtest set to {value}")
                elif key=="endwords":
                    endwords=value
                    save_settings()
                    print(f"endwords set to {value}")
                else:
                    print("Unknown setting.")
            except:
                print("Usage: set <setting> <value>")
        elif dcmd=="show":
            print("=== SETTINGS ===")
            print(f"mathtest: {mathtest}")
            print(f"endwords: {endwords}")
            print("=================")
        elif dcmd=="exit":
            print("Exiting Dev Console...")
            break
def list_files():
    if not files:
        print("No files exist.")
        return
    print("=== FILES ===")
    for name in files:
        print(f"- {name}")
    print("==============")
def create_file():
    name=input("Enter new file name: ").strip()
    if name=="":
        print("File name cannot be empty.")
        return
    if " " in name or "/" in name or "\\" in name:
        print("Invalid file name.")
        return
    if name in files:
        print("A file with that name already exists.")
        return
    content=input("Enter file content: ")
    files[name]=content
    if save_files_data():
        print(f"File '{name}' created successfully!")
    else:
        print("Failed to save file. Reverting.")
        del files[name]
def read_file():
    name=input("Enter file name to read: ").strip()
    if name not in files:
        print("File not found.")
        return
    print("=== FILE CONTENT ===")
    print(files[name])
    print("====================")
def delete_file():
    name=input("Enter file name to delete: ").strip()
    if name not in files:
        print("File not found.")
        return
    confirm=input(f"Are you sure you want to delete '{name}'? (Y/N): ").lower()
    if confirm!="y":
        print("Deletion cancelled.")
        return
    del files[name]
    if save_files_data():
        print(f"File '{name}' deleted successfully!")
    else:
        print("Failed to save changes. File restored.")
def cre8or():
    print("Entering cre8or. Type 'help' for commands.")
    while True:
        cre8or_cmd=input("files> ").lower().strip()
        track_command_wrapper()
        if cre8or_cmd=="help":
            print("=== cre8or COMMANDS ===\nlist - show all files\ncre8 - create a new file\nread - read a file\ndelete - delete a file\nexit - leave cre8or\n==============================")
        elif cre8or_cmd=="list":
            list_files()
        elif cre8or_cmd=="cre8":
            create_file()
        elif cre8or_cmd=="read":
            read_file()
        elif cre8or_cmd=="delete":
            delete_file()
        elif cre8or_cmd=="exit":
            print("Exiting File Manager...")
            break
def cre8orScript():
    print("Entering cre8orScript. Type 'help' for commands.")
    while True:
        scmd=input("cre8orScript> ").lower().strip()
        track_command_wrapper()
        if scmd=="help":
            print("=== CRE8ORSCRIPT COMMANDS ===\nnew - create a new script\nrun - run an existing script\nlist - list all scripts\ndelete - delete a script\nexit - leave cre8orScript\n==============================")
        elif scmd=="list":
            scripts=[f for f in files if f.endswith(".c8s")]
            if not scripts:
                print("No scripts found.")
            else:
                print("=== SCRIPTS ===")
                for s in scripts:
                    print(f"- {s}")
                print("===============")
        elif scmd=="new":
            name=input("Script name (no spaces, auto .c8s): ").strip()
            if name=="" or set(name).issubset(set(string.ascii_letters+string.ascii_digits+"._-")):
                print("Invalid script name.")
                continue
            name+=".c8s"
            if name in files:
                print("A script with that name already exists.")
                continue
            print("Enter script content. Type 'END' on its own line to finish.")
            lines=[]
            while True:
                line=input()
                if line.strip().upper()=="END":
                    break
                lines.append(line)
            files[name]="\n".join(lines)
            if save_files_data():
                print(f"Script '{name}' created.")
                award_gunch(2,"Making a script")
            else:
                print("Failed to save script.")
        elif scmd=="delete":
            name=input("Script to delete: ").strip()
            if set(name).issubset(set(string.ascii_letters+string.ascii_digits+"._-")):
                print("Invalid filename: no spaces allowed.")
                continue
            if not name.endswith(".c8s"):
                name+=".c8s"
            if name not in files:
                print("Script not found.")
                continue
            del files[name]
            if save_files_data():
                print(f"Script '{name}' deleted.")
            else:
                print("Failed to save changes.")
        elif scmd=="run":
            name=input("Script to run: ").strip()
            if set(name).issubset(set(string.ascii_letters+string.ascii_digits+"._-")):
                print("Invalid filename: no spaces allowed.")
                continue
            if not name.endswith(".c8s"):
                name+=".c8s"
            if name not in files:
                print("Script not found.")
                award_gunch(-3,"running a nonexistent script")
                continue
            print(f"Running script '{name}'...\n")
            for line in files[name].split("\n"):
                cmd=line.strip().rstrip('\r')
                lcmd = cmd.lower() 
                if cmd=="":
                    continue
                elif cmd=="list":
                    list_files()
                elif cmd.startswith("create "):
                    fname = cmd.split(" ",1)[1].strip()
                    if set(name).issubset(set(string.ascii_letters+string.ascii_digits+"._-")):
                        print("Invalid filename.")
                        continue
                    if fname in files:
                        print("A file with that name already exists.")
                        continue
                    files[fname] = ""
                    if save_files_data():
                        print(f"Created file '{fname}'")
                    else:
                        print("Failed to save file.")
                        del files[fname]
                elif lcmd.startswith("delete "):
                    fname = cmd[7:].strip()
                    if fname in files:
                        del files[fname]
                        if save_files_data():
                            print(f"Deleted file '{fname}'.")
                        else:
                            print("Failed to save changes after deletion.")
                    else:
                        print(f"Cannot delete '{fname}': file not found.")
                elif lcmd.startswith("write "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: write <file> <text>")
                        continue
                    fname, text = parts[1], parts[2]
                    if " " in fname:
                        print("Invalid filename: no spaces allowed.")
                        continue
                    fname, text = parts[1], parts[2]
                    if set(name).issubset(set(string.ascii_letters+string.ascii_digits+"._-")):
                        print("Invalid filename: no spaces allowed.")
                        continue
                    fname, text = parts[1], parts[2]
                    if not fname.endswith(".txt"):
                        print("Scripts may only modify .txt files.")
                        continue
                    files[fname] = text
                    if save_files_data():
                        print(f"Wrote to '{fname}'.")
                    else:
                        print("Failed to save file.")
                elif lcmd.startswith("append "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("Usage: write <file> <text>")
                        continue
                    fname, text = parts[1], parts[2]
                    if " " in fname:
                        print("Invalid filename: no spaces allowed.")
                        continue
                    if not fname.endswith(".txt"):
                        print("Scripts may only modify .txt files.")
                        continue    
                    if len(parts) < 3:
                        print("Usage: append <file> <text>")
                        continue
                    fname, text = parts[1], parts[2]
                    if fname not in files:
                        files[fname] = ""
                    files[fname] += ("\n" + text)
                    if save_files_data():
                        print(f"Appended to '{fname}'.")
                    else:
                        print("Failed to save file.")
                elif lcmd.startswith("pause "):
                    try:
                        sec = float(cmd.split(" ", 1)[1])
                        if sec < 0:
                            print("Pause time must be positive.")
                            continue
                        time.sleep(sec)
                    except:
                        print("Usage: pause <seconds>")
                elif lcmd.startswith("echo "):
                    text = cmd[5:].strip()
                    if (text.startswith('"') and text.endswith('"')) or (text.startswith("'") and text.endswith("'")):
                        text = text[1:-1]
                    print(text)
        elif scmd=="exit":
            print("Exiting cre8orScript...")
            break
def repeater():
    print("PYTHON WORD REPEATER")
    def iterate(times):
        word=input("WHAT WORD? (A WORD!!!): ")
        for x in range(times):
            print(word)
    try:
        iterate(int(float(input("HOW MANY TIMES? (A NUMBER!!!): "))))
    except ValueError:
        print("Not a number. Exiting repeater.")
        return
    iterations=1
    while True:
        done=input("Are You Done? (Leave blank for no, type anything for yes): ")
        if done=="":
            try:
                iterate(int(float(input("HOW MANY TIMES? (A NUMBER!!!): "))))
                iterations+=1
            except ValueError:
                print("Not a number. Stopping.")
                break
        else:
            break
    print(f"You\ndid\nthe\nIterator\nTool\n{iterations}\nTimes!")
    if iterations>20:
        print("THAT's\nA\nLot!!!")
    else:
        print("Goodbye!")
def add_user():
    global userpasses
    print("=== Create New User ===")
    new_user=input("Enter new username: ").strip()
    if new_user=="":
        print("Username cannot be empty.")
        return False
    if " " in new_user:
        print("Username cannot contain spaces.")
        return False
    if new_user.lower() in ["chronos","chronosprotected"]:
        print("You cannot create a protected system user.")
        return False
    if new_user in userpasses:
        print("That user already exists.")
        return False
    new_pass=getpass.getpass("Enter password: ")
    if new_pass=="":
        print("Password cannot be empty.")
        return False
    userpasses[new_user]=new_pass
    if save_user_data():
        print(f"User '{new_user}' created successfully!")
        return True
    else:
        print("Failed to save user data. User not created.")
        del userpasses[new_user]
        return False
def games():
    print("Welcome to games! Type 'help' for help")
    while True:
        game=input("Games> ").strip().lower()
        track_command_wrapper()
        if game=="help":
            print("=== GAMES HELP ===\nhelp - Show this menu\nguess - Play Guess the Number\nrps - Rock, Paper, Scissors\nentr - ENTER (or RETURN) Clicker\nexit - Leave games")
        elif game=="guess":
            print("Welcome to guess the number!\nType 'exit' to exit")
            secret=random.randint(1,100)
            while True:
                userguess=input("Guess (1-100): ").strip()
                if userguess.lower()=="exit":
                    print("Exiting guess...")
                    break
                try:
                    userguess_int=int(userguess)
                    if not 1<=userguess_int<=100:
                        print("Please guess between 1 and 100.")
                        continue
                    if userguess_int>secret:
                        print("Too high!")
                    elif userguess_int<secret:
                        print("Too low!")
                    else:
                        print(f"Right! It was {secret}!")
                        replay=input("Play again? (Y/N): ").strip().lower()
                        if replay=="y":
                            secret=random.randint(1,100)
                        else:
                            break
                except ValueError:
                    print("Please enter a valid number or 'exit'.")
        elif game=="rps":
            print("Welcome to RPS!")
            playscore=0
            compscore=0
            computerplays=["🪨","📄","✂️"]
            while True:
                play=input("Rock, Paper, or Scissors (or 'exit'): ").strip().lower()
                if play=="exit":
                    print(f"Final Score: Player - {playscore} | Computer - {compscore}")
                    break
                if play not in ["rock","paper","scissors"]:
                    print("Invalid choice. Choose rock, paper, or scissors.")
                    continue
                computer=random.choice(computerplays)
                print(f"Computer chose: {computer}")
                if (play=="rock" and computer=="🪨") or (play=="paper" and computer=="📄") or (play=="scissors" and computer=="✂️"):
                    print("Tie!")
                elif (play=="rock" and computer=="📄") or (play=="paper" and computer=="✂️") or (play=="scissors" and computer=="🪨"):
                    print("Computer Wins!")
                    compscore+=1
                else:
                    print("Player Wins!")
                    playscore+=1
                print(f"Score: Player - {playscore} | Computer - {compscore}")
        elif game=="entr":
            clicks=0
            multi=1
            upcost=20
            autocost=100
            autos=0
            prevtick=time.time()
            cpslist=[]
            print("ENTER (or RETURN) Clicker\nType 'shop' for shop, 'exit' to exit.\nPress ENTER (or RETURN) to click.")
            while True:
                now=time.time()
                if now-prevtick>=1:
                    clicks+=autos
                    prevtick=now
                cmd=input("ENTR> ").strip().lower()
                if cmd=="":
                    now=time.time()
                    clicks+=multi
                    cpslist.append(now)
                    cpslist=[t for t in cpslist if now-t<=1]
                    print(f"+{multi} clicks! Total: {clicks} | CPS: {len(cpslist)}")
                elif cmd=="shop":
                    print(f"=== SHOP ===\n1) Multiplier (+1 per click) - Cost: {upcost}\n2) Autoclicker (+1 CPS) - Cost: {autocost}\nPress ENTER to cancel")
                    buy=input("BUY> ").strip()
                    if buy=="":
                        print("Cancelled.")
                        continue
                    try:
                        buy_int=int(buy)
                        if buy_int==1 and clicks>=upcost:
                            clicks-=upcost
                            multi+=1
                            upcost=int(upcost*1.5)
                            print("Upgrade purchased!")
                        elif buy_int==2 and clicks>=autocost:
                            clicks-=autocost
                            autos+=1
                            autocost=int(autocost*1.7)
                            print("Autoclicker purchased!")
                        else:
                            print("Not enough clicks or invalid selection.")
                    except ValueError:
                        print("Cancelled.")
                elif cmd=="exit":
                    print("Exiting ENTR...")
                    break
                else:
                    print("Invalid command. Press ENTER to click, 'shop' for shop, or 'exit' to exit.")
        elif game=="exit":
            print("Leaving games...")
            break
def Thenotes():
    global notes
    print("Welcome to Notes. Type 'help' to get help")
    while True:
        note=input("Notes>")
        track_command_wrapper()
        if note.lower()=="help":
            print("Help - shows this menu\nNote - makes a new note on next line\nList - Shows all notes\nDelete - Deletes a note\nExit - Exits notes")
        elif note.lower()=="note":
            thenote=input("Note - ")
            notes.append(thenote)
            save_notes()
            print("note saved")
        elif note.lower()=="list":
            if len(notes)==0:
                print("No Notes")
            else:
                for z in range(len(notes)):
                    print(f"{z+1} {notes[z]}")
        elif note.lower()=="delete":
            try:
                numbernote=int(input("which note: "))
                if 1<=numbernote<=len(notes):
                    notes.pop(numbernote-1)
                    save_notes()
                    print(f"note #{numbernote} deleted")
                else:
                    print("No such note exists.")
            except ValueError:
                print("Please enter a valid number")
        elif note.lower()=="exit":
            print("exiting...")
            break
    save_notes()
def calculator():
    print("=== CALCULATOR APP IN PYTHON ===")
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        if b==0:
            print("Hey man, woah woah woah, you can't divide by 0! Refresh and make your second number not 0, Broski!!!")
            return None
        return a/b
    valid_ops=["add","subtract","multiply","divide"]
    op=input("Will you add, subtract, multiply, or divide?\n{>: -[||]}--[--<\nspell it right and no caps: ").strip().lower()
    if op not in valid_ops:
        print("invalid operator. try again")
        return
    print(f"I Will {op}")
    try:
        num1=float(input("First number: ").strip())
        num2=float(input("Second number: ").strip())
    except ValueError:
        print("One of your numbers isn't a number. Try Again (BOZO!).")
        return
    if op=="add":
        print(add(num1,num2))
    elif op=="subtract":
        print(subtract(num1,num2))
    elif op=="multiply":
        print(multiply(num1,num2))
    elif op=="divide":
        res=divide(num1,num2)
        if res is not None:
            print(res)
def terminal():
    global user,mathtest,terminalstat,userwelcomed,logged_out,endwords,modulecount,files,exitstatus,modules,command_history,godstat,gunch_bucks,ui_colors,current_ui_color
    egg=0
    userwelcomed=False
    if user in ["chronos"]:
        while user in ["chronos"] and not logged_out:
            if not userwelcomed:
                print('Welcome to terminal!\nType "Help" for a list of commands\n')
                userwelcomed=True
                terminalstat="up"
            if not chore:
                command=input("Terminal> ").strip()
            else:
                command=input("`Terminal> ").strip()
            print(f"Attempting to run {command} in hideOUS...")
            command_history.append(command)
            if command.lower()=="house":
                print("   /\\   \n  /  \\  \n / [] \\ \n/    \\\n|   |\n|  []  |\n|______|\n")
                egg=0
            elif command.lower() == "time":
                print(time.ctime())
            elif command=="gunch":
                print(f"You have: GB$ {gunch_bucks}")
            elif command == "minishop":
                print("=== MINI-SHOP ===")
                print("1. Mystery — GB$ 10")
                print("2. UI — GB$ 25")
                print("===================")
            elif command.startswith("buymini "):
    item = command.split(" ", 1)[1]
    if item == "mystery":
        if gunch_bucks >= 10:
            gunch_bucks -= 10
            print("You bought a Mystery Box!")
            reward = random.choice(["5", "10", "20", "ui", "nothing","lore"])
            print(f"Mystery Box reward: {reward}")
        if reward == "5":
            gunch_bucks += 5
            print("You earned GB$ 5!")
        elif reward == "10":
            gunch_bucks += 10
            print("You earned GB$ 10!")
        elif reward == "20":
            gunch_bucks += 20
            print("You earned GB$ 20!")
        elif reward == "ui":
            current_ui_color = random.choice(ui_colors)
            print(f"Your UI color is now: {current_ui_color.upper()}!")
        elif reward == "lore":
            print("You found a note: 'Mr. Gunch once banned parentheses for being too curvy.'")
        elif reward == "nothing":
            print("The box was empty...")
                else:
                    print("Not enough Gunch Bucks.")
                continue
        elif item == "ui":
            if gunch_bucks >= 25:
                gunch_bucks -= 25
                current_ui_color = random.choice(ui_colors)
                print(f"Your UI color is now: {current_ui_color.upper()}!")
            else:
                print("Not enough Gunch Bucks.")
            continue
        else:
            print("Unknown mini-shop item. Use \"minishop\" to view minishop items")
            continue
            elif command.lower()=="flame":
                flame="\U0001F525"
                repeated=""
                egg=0
                count=random.randint(1,1000000)
                if count>5000:
                    count=5000
                for z in range(count):
                    repeated+=flame
                print(repeated)
            elif command.lower()=="help":
                print("Quit - exits terminal\nHelp - shows this menu\nSay - has the console output your statement\nMathTest - Take the Math Test!\nDestroy Terminal - Exits and destroys terminal forever (A very long time!)\nRestart - restarts terminal\nClear - clears terminal window\nSetending - edits what you want at the end of after exiting Terminal\nWhoAmI - tells you who you are\nSetPass - sets password for \"chronos\" user and LOGS OUT\nVersioncheck - Checks version and displays\nEchoCheck - Checks if Echo_Char will work when using getpass module\nInstall - Allows installation of an available module\nRun - Allows the running of installed modules\nFlame - Prints the fire emoji many times\nUptime - Shows how long terminal has been up\nHistory - Shows command history\nClearHistory - Clears command history\nDream - Just Don't. It's pretty weird...\nGod - maybe unlocks something\nDistort - glitch text\nNet - Allows the use of networking diagnostic tools\nElem - shows all 118 elements\nTime - prints the time\nGunch - prints how many Gunch Bucks you have\nMiniTerm - opens the mini - terminal\nRandom Groups - generate random groups!")
                if novel in modules:
                    print("Novel - Shows your novelty score")
                egg=0
            elif command.lower()=="novel" and novel in modules:
                novel()
                egg = 0
            elif command.lower()=="miniterm":
                mmicroshell()
                egg = 0
            elif command.lower()=="elem":
                for name, data in enumerate(elements.items()):
                    nums = data['Number']
                    syms = data['Symbol']
                    print(f"Element: {name}\n\tNumber: {nums}\n\tSymbol: {syms}")
                    time.sleep(0.1)
                egg = 0
            elif command.lower()=="quit":
                mathtest="NULL"
                user="TerminalExited"
                egg=0
            elif command.lower()=="fandom groups":
                random_groups()
                egg=0
            elif command.lower()=="history":
                if len(command_history)>0:
                    for i in range(len(command_history)):
                        print(f"{i+1}: {command_history[i]}")
                else:
                    print("Nothing Here!")
            elif command.lower()=="clearhistory":
                command_history.clear()
                print("Cleared!")
            elif command.lower()=="god":
                isgod=random.choice(["yes","no"]+[""]*18)
                godstat=(isgod=="yes")
                if godstat:
                    print('You are a god. Do whatever you want! Type "dev" next.\nGodly powers: SMITE, BLESS, CHAOS')
                egg=0
            elif command.lower()=="say":
                message=input("Say What: ")
                print(message)
                egg=0
            elif command.lower()=="uptime":
                sec=int(time.time()-boot_time)
                h=sec//3600
                m=(sec%3600)//60
                s=sec%60
                print(f"{h:02d}:{m:02d}:{s:02d}")
            elif command.lower()=="mathtest":
                user="TerminalExited"
                egg=0
            elif command.lower()=="smite" and godstat:
                try:
                    t1=random.choice(["Bob","Alice","Greg","The Mailman","Your Math Teacher"])
                    print(f"target 1: {t1}")
                    print("target 2: Random Target")
                    target=int(input("Target 1 or 2: ").strip())
                    if target<1 or target>2:
                        print("smiting noone...")
                    else:
                        if target==1:
                            print(f"Target #1 was {t1}")
                        else:
                            print(f"Target #2 was {random.choice(['A Stranger','A Bird','A Ghost','Your Reflection'])}")
                        print(f"Target {random.choice(['was blasted by lightning','was run over by a car','got swallowed into the Earth','somehow got killed spontaneously','vanished off the face of the planet'])}")
                except ValueError:
                    print("smiting noone...")
            elif command.lower()=="bless" and godstat:
                try:
                    t1=random.choice(["A football QB","Your CAT","A turkey","Your Mom"])
                    print("BLESS who:")
                    print(f"Target 1: {t1}")
                    print("Target 2: Something Random")
                    target=int(input("(Type 1 or 2): ").strip())
                except ValueError:
                    print("None shall be blessed by thou. Fie Upon You!")
                    target=0
                if target==1:
                    print(f"Target #1 ({t1}) was given good luck!")
                    print(f"They were {random.choice(['showered in fortune','granted divine favor','blessed with cosmic luck','touched by radiant light'])}.")
                elif target==2:
                    t2=random.choice(["A squirrel","A random stranger","A passing cloud","A confused goose"])
                    print(f"Target #2 ({t2}) was given good luck!")
                    print(f"They were {random.choice(['filled with warmth','granted unexpected blessings','surrounded by positive energy','kissed by fate'])}.")
                else:
                    print("None shall be blessed by thou. Fie Upon You!")
            elif command.lower()=="`":
                print("Hidden module: underflow")
                print("install with: install underflow")
            elif command.lower()=="chaos" and godstat:
                print(random.choice([
                    "Reality bends sideways.",
                    "A portal opens and immediately closes.",
                    "You hear whispering behind you, but no one is there.",
                    "Gravity flickers for a moment.",
                    "Your vision pixelates.",
                    "A random object levitates.",
                    "You feel like you're being watched.",
                    "The lights dim, then brighten.",
                    "A glitch runs across your screen.",
                    "You momentarily forget your own name.",
                    "A cold breeze passes through the room.",
                    "Your shadow moves independently.",
                    "You hear footsteps behind you.",
                    "A random window opens and closes.",
                    "Your reflection blinks.",
                    "Something taps your shoulder, but nothing is there.",
                    "The floor vibrates softly.",
                    "Your heartbeat echoes loudly.",
                    "A faint laugh echoes in the distance.",
                    "Your screen flickers to black, then returns.",
                    "You smell ozone.",
                    "A random number appears in your mind.",
                    "You feel lighter for a moment.",
                    "Your chair creaks even if you didn’t move.",
                    "A spark of light zips across your vision.",
                    "You hear a door slam somewhere.",
                    "Your name is whispered softly.",
                    "A glitchy afterimage trails your movements.",
                    "Your hands feel warm.",
                    "Your hands feel cold.",
                    "You hear a faint chime.",
                    "Something rustles nearby.",
                    "You feel a sudden wave of déjà vu.",
                    "Your screen warps like heat haze.",
                    "You hear static for a moment.",
                    "A random thought intrudes violently.",
                    "You feel like you’re falling.",
                    "Your ears ring sharply.",
                    "A random object in the room shifts slightly.",
                    "You hear a soft hum.",
                    "Your vision blurs momentarily.",
                    "A spark of electricity jumps from your fingertips.",
                    "You feel a presence behind you.",
                    "Your screen displays a symbol you don’t recognize.",
                    "A random memory surfaces unexpectedly.",
                    "You feel a sudden burst of energy.",
                    "You feel drained for a moment.",
                    "Your sense of time distorts.",
                    "You hear a soft knock.",
                    "Your screen tilts slightly, then corrects itself.",
                    "You feel like someone said your name.",
                    "A random color floods your vision.",
                    "Your cursor moves on its own for a moment.",
                    "You hear a faint melody.",
                    "Your breathing feels out of sync.",
                    "A random word echoes in your mind.",
                    "You feel a sudden chill.",
                    "You feel a sudden warmth.",
                    "Your screen brightness flickers.",
                    "You hear a soft whisper: 'hello'.",
                    "You hear a soft whisper: 'run'.",
                    "You hear a soft whisper: 'stay'.",
                    "Your surroundings feel unreal.",
                    "Your sense of balance shifts.",
                    "You feel like you're being pulled forward.",
                    "You feel like you're being pushed back.",
                    "A random object falls over.",
                    "You hear a faint growl.",
                    "You hear a faint giggle.",
                    "Your screen displays static for a moment.",
                    "You feel a hand brush past your arm.",
                    "Your reflection smiles faintly.",
                    "You hear a distant explosion.",
                    "You hear a distant scream.",
                    "You hear a distant cheer.",
                    "Your screen shows a flash of white.",
                    "Your screen shows a flash of red.",
                    "Your screen shows a flash of blue.",
                    "You feel a sudden urge to laugh.",
                    "You feel a sudden urge to run.",
                    "You feel a sudden urge to hide.",
                    "Your thoughts echo loudly.",
                    "Your thoughts go silent for a moment.",
                    "You hear a heartbeat that isn’t yours.",
                    "You hear typing behind you.",
                    "You hear breathing behind you.",
                    "You hear someone say 'look up'.",
                    "You hear someone say 'don’t look'.",
                    "Your screen rotates 1 degree, then snaps back.",
                    "You feel like someone walked through you.",
                    "You feel like you skipped a second.",
                    "You feel like time slowed down.",
                    "You feel like time sped up.",
                    "Your screen glitches into a different OS for a moment.",
                    "You hear a soft bell.",
                    "You hear a soft growl.",
                    "You hear a soft sigh.",
                    "You hear a soft gasp.",
                    "You hear a soft whisper: 'chaos...'",
                    "Reality folds into a perfect cube",
                    "Gravity forgets which way is down",
                    "Time skips forward three seconds, then apologizes",
                    "Your shadow walks away without you",
                    "A tiny wizard appears, casts 'mild inconvenience', vanishes",
                    "Your OS clears its throat before every command",
                    "Your cursor slowly drifts away like it's bored",
                    "A duck appears, judges you silently, then leaves",
                    "Your CPU fan whispers 'feed me'",
                    "Your wallpaper melts into a motivational speech delivered by a confused raccoon in a business suit"
                ]))
            elif command.lower()=="destroy terminal":
                print("Terminal Destroyed")
                terminalstat="Down"
                user="TerminalExited"
                mathtest="NULL"
                egg=0
            elif command.lower().startswith("net"):
                parts = command.split()
                if "browser" not in modules:
                    print("Error: Browser module is required for networking tools.")
                    print("Install the 'browser' module to continue.")
                    continue
                valid_hosts = {
                    "sys://network",
                    "sys://weather",
                    "sys://modules",
                    "sys://about",
                    "ptps://weather.co",
                    "ptps://ratemyscript.co"
                }
                if len(parts) == 1:
                    print("net subcommands:")
                    print("  net ping <host>")
                    print("  net info")
                    print("  net trace <host>")
                    print("  net dns <host>")
                    print("  net scan <host>")
                    print("Valid hosts:")
                    for h in valid_hosts:
                        print(" ", h)
                    continue
                sub = parts[1]
                def browser_open():
                    print("[net] Requesting Browser module...")
                    time.sleep(0.15)
                    print("[Browser] Launching in background...")
                    print("\n" * random.randint(3, 6), end="")
                def browser_exec(desc):
                    print(f"[Browser] (background) handling: {desc}")
                    time.sleep(0.2)
                def browser_close():
                    print("[Browser] Closing background instance...")
                    print("\n" * random.randint(2, 4), end="")
                    time.sleep(0.1)
                if sub == "ping":
                    if len(parts) < 3:
                        print("Usage: net ping <host>")
                        continue
                    host = parts[2]
                    if host not in valid_hosts:
                        print("PTPS ERROR: 404 NOT FOUND")
                        continue
                    browser_open()
                    browser_exec(f"ping {host}")
                    print(f"Pinging {host} [{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}] with 32 bytes of data:")
                    for _ in range(4):
                        time.sleep(0.15)
                        if random.random() < 0.2:
                            print("Request timed out.")
                        else:
                            print(f"Reply from {random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}: bytes=32 time={random.randint(20,80)}ms TTL={random.randint(40,64)}")
                    browser_close()
                    print("[net] ping complete.")
                    continue
                elif sub == "info":
                    browser_open()
                    browser_exec("net info")
                    print("Network adapter: eth0")
                    print(f"IPv4 Address : 192.168.{random.randint(0,255)}.{random.randint(1,254)}")
                    print("Subnet Mask  : 255.255.255.0")
                    print("Gateway      : 192.168.0.1")
                    print("DNS Servers  : 1.1.1.1, 8.8.8.8")
                    browser_close()
                    print("[net] info complete.")
                    continue
                elif sub == "trace":
                    if len(parts) < 3:
                        print("Usage: net trace <host>")
                        continue
                    host = parts[2]
                    if host not in valid_hosts:
                        print("PTPS ERROR: 404 NOT FOUND")
                        continue
                    browser_open()
                    browser_exec(f"trace {host}")
                    hops = random.randint(3,6)
                    for i in range(1, hops+1):
                        print(f" {i}   {random.randint(10,200)}ms   {random.randint(10,200)}ms   {random.randint(10,200)}ms   10.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}")
                        time.sleep(0.15)
                    print(f" {hops+1}   {random.randint(10,200)}ms   {random.randint(10,200)}ms   {random.randint(10,200)}ms   {host}")
                    browser_close()
                    print("[net] trace complete.")
                    continue
                elif sub == "dns":
                    if len(parts) < 3:
                        print("Usage: net dns <host>")
                        continue
                    host = parts[2]
                    if host not in valid_hosts:
                        print("PTPS ERROR: 404 NOT FOUND")
                        continue
                    browser_open()
                    browser_exec(f"dns {host}")
                    print("DNS Lookup:")
                    print(f" Host: {host}")
                    print(f" Address: {random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}")
                    print(" Record Type: A")
                    browser_close()
                    print("[net] dns complete.")
                    continue
                elif sub == "scan":
                    if len(parts) < 3:
                        print("Usage: net scan <host>")
                        continue
                    host = parts[2]
                    if host not in valid_hosts:
                        print("PTPS ERROR: 404 NOT FOUND")
                        continue
                    browser_open()
                    browser_exec(f"scan {host}")
                    print(f"Scanning {host}...")
                    open_ports = random.sample([22, 80, 443, 8080, 3306], random.randint(1,3))
                    for p in open_ports:
                        print(f" Port {p}: OPEN")
                        time.sleep(0.1)
                    browser_close()
                    print("[net] scan complete.")
                    continue
                else:
                    print(f"Unknown net subcommand: {sub}")
                    continue
            elif command.lower()=="restart":
                print("Restarting terminal...\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                userwelcomed=False
                egg=0
            elif command.lower()=="logout":
                print("Logging out...")
                userwelcomed=False
                mathtest="NULL"
                logged_out=True
                user="TerminalExited"
                safe_write(LOGIN_COOKIE_FILE, {})
                egg=0
            elif command.lower()=="clear":
                if os.name=="nt":
                    os.system("cls")
                else:
                    os.system("clear")
                egg=0
            elif command.lower()=="setending":
                endwords=input("What would you like to say after the entire thing is over? ")
                save_settings()
                egg=0
            elif command.lower()=="whoami":
                egg+=1
                if egg<3:
                    print(user)
                elif egg==3:
                    print("You should know by now, since you're asking!")
                    egg=0
            elif command.lower()=="setpass":
                if not logged_out:
                    if user=="chronos":
                        userpasses["chronos"]=getpass.getpass("What is your new password: ")
                        logged_out=True
                        save_user_data()
                    else:
                        print('YOU ARE NOT "chronos". YOU CANNOT CHANGE THEIR PASSWORD')
                    egg=0
            elif command.lower()=="echocheck":
                ver=int(str(sys.version_info.major)+str(sys.version_info.minor))
                if ver>=313:
                    print("Echo_char will work")
                else:
                    print("Echo_Char won't work")
                egg=0
            elif command.lower()=="versioncheck":
                print(sys.version)
                egg=0
            elif command.lower()=="dev":
                dev()
            elif command.lower()=="install":
                install()
            elif command.startswith("run "):
                mod2run=command[4:].strip().lower()
                aliases={"c8":"cre8or","editor":"cre8or","script":"cre8orscript","calc":"calc","calculator":"calc","game":"games","g":"games","repeat":"repeater","notes":"notes","hunt":"hunter","dict": "dictionary app","gp":"gunchopedia","hw":"hollowwisp","cw":"colorword"}
                if mod2run in aliases:
                    mod2run=aliases[mod2run]
                if mod2run not in modules:
                    print(f"Module '{mod2run}' is not installed.")
                    print("Use 'install' to install modules.")
                try:
                    if mod2run=="cre8or":
                        cre8or()
                    elif mod2run=="colorword":
                        print_alt(input("FIRST WORDS: "))
                    elif mod2run=="cre8orscript":
                        cre8orScript()
                    elif mod2run=="calc":
                        calculator()
                    elif mod2run=="games":
                        games()
                    elif mod2run=="repeater":
                        repeater()
                    elif mod2run=="music":
                        music()
                    elif mod2run=="paint":
                        paint()
                    elif mod2run=="fortune":
                        fortune()
                    elif mod2run=="browser":
                        browser()
                    elif mod2run=="notes":
                        Thenotes()
                    elif mod2run=="ai":
                        ai()
                    elif mod2run=="hunter":
                        hunter()
                    elif mod2run=="rpg":
                        rpg()
                    elif mod2run=="dictionary app":
                        dictionary_app()
                    elif mod2run=="hollowwisp":
                        HollowWisp()
                    elif mod2run=="ouch":
                        print(OUCH())
                    elif mod2run == "underflow":
                        if "underflow" not in installed_modules:
                            print("Unknown module.")
                        else:
                            underflow()
                    elif mod2run=="coreline":
                        if not chore:
                            print("module not found")
                        else:
                            print(coreline())
                    elif mod2run=="gunchopedia":
                        print("Launching Mr. Gunch Facts...")
                        facts = ["Mr. Gunch once banned parentheses for being 'too curvy'.","Gunch Bucks were originally printed on the back of math worksheets.","The Gunch Theorem states: 'If you can simplify it, you must simplify it.'","Mr. Gunch once declared war on the quadratic formula.","Legend says Mr. Gunch can smell an unbalanced equation from 30 feet away.","Mr. Gunch says that he would change his last name, since G, u, and c were \"not straight enough\""]
                        print(random.choice(facts))
                    else:
                        print(f"Module '{mod2run}' is does not exist")
                except Exception as e:
                    print(f"Module '{mod2run}' crashed: {e}")
            elif command.lower()=="dream":
                print("The Console enters a dream-like state...")
                time.sleep(random.random()+0.5)
                if len(command_history)>=2:
                    prev=command_history[-2].lower()
                else:
                    prev=""
                if prev=="dev":
                    lastcmdstring="A path made of your dev executable inputs"
                elif prev=="help":
                    lastcmdstring="A slope of available commands"
                elif prev=="say":
                    lastcmdstring="A staircase of what you've said"
                elif prev=="dream":
                    lastcmdstring="A mountain of dream potentialities"
                elif prev=="install":
                    lastcmdstring="A wall made of your unused module"
                elif prev=="run":
                    lastcmdstring="A tower of runned modules"
                elif prev=="history":
                    lastcmdstring="A 7-Kb stretch of road"
                elif prev=="smite":
                    lastcmdstring="A large collection of smitten, dead lines"
                elif prev=="bless":
                    lastcmdstring='A big pile of <h1> tags saying "Good Luck!"'
                else:
                    lastcmdstring="A bit-by-bit loading bar with you at the end..."
                print(random.choice([
                    "A hallway made of old error messages",
                    "A beach where the waves are made of loading bars",
                    "A forest of tangled USB cables",
                    "A city built entirely from recycled pop-up windows",
                    "A void filled with floating keyboard keys",
                    "A desert where the sand is pixelated",
                    "A library where every book is named 'Untitled'",
                    "A room made of 2's",
                    "An asteroid's surface with ASCII holes",
                    lastcmdstring
                ]))
                for i in range(random.randint(2,9)):
                    print(random.choice([
                        "A giant cursor drags itself across the sky",
                        "Your last command repeats itself in the clouds",
                        "A folder opens and something crawls out",
                        "An ancient version of the OS whispers advice",
                        "A progress bar stretches into the horizon",
                        "A blue screen rises like a sunrise",
                        "Your reflection in the monitor walks away",
                        "A POST request frantically turns around like it's lost",
                        "ASCII 霓's skitter around like bugs",
                        "A project folder opens up and a thousand bugs crawl out",
                        "<div> tags begin nesting themselves infinitely",
                        "A swarm of broken <img> icons flickers in the dark",
                        "A rogue JavaScript function keeps calling itself",
                        "A corrupted stylesheet flickers reality",
                        "Your surroundings suddenly gain !important tags",
                        "You suddenly can only move 25 bits in any direction"
                    ]))
                print(random.choice([
                    "Suddenly, everything freezes except you.",
                    "The dream collapses into static.",
                    "You hear your own voice say 'Wake up.'",
                    "The system reboots itself without touching anything.",
                    "A shadow steps out of the monitor and points at you.",
                    "The dream ends before something important is revealed.",
                    random.choice([
                        "Your VPN slaps you in the face to wake you up",
                        "The VPN leader shouts 'HALT, IN THE NAME OF NORDHVPN!'"
                    ])
                ]))
                print("The OS wakes back up.")
            elif command.lower()=="distort":
                marks = "\u0300\u0301\u0302\u0303\u0304\u0305\u0306\u0307\u0308\u0309\u030A\u030B\u030C\u030D\u030E\u030F\u0310\u0311\u0312\u0313\u0314\u0315\u0316\u0317\u0318\u0319\u031A\u031B\u031C\u031D\u031E\u031F\u0320\u0321\u0322\u0323\u0324\u0325\u0326\u0327\u0328\u0329\u032A\u032B\u032C\u032D\u032E\u032F\u0330\u0331\u0332\u0333\u0334\u0335\u0336\u0337\u0338\u0339\u033A\u033B\u033C\u033D\u033E\u033F\u0340\u0341\u0342\u0343\u0344\u0345\u0346\u0347\u0348\u0349\u034A\u034B\u034C\u034D\u034E\u034F\u0350\u0351\u0352\u0353\u0354\u0355\u0356\u0357\u0358\u0359\u035A\u035B\u035C\u035D\u035E\u035F\u0360\u0361\u0362\u0363\u0364\u0365\u0366\u0367\u0368\u0369\u036A\u036B\u036C\u036D\u036E\u036F\u1DC0\u1DC1\u1DC2\u1DC3\u1DC4\u1DC5\u1DC6\u1DC7\u1DC8\u1DC9\u1DCA\u1DCB\u1DCC\u1DCD\u1DCE\u1DCF\u1DD0\u1DD1\u1DD2\u1DD3\u1DD4\u1DD5\u1DD6\u1DD7\u1DD8\u1DD9\u1DDA\u1DDB\u1DDC\u1DDD\u1DDE\u1DDF\u1DE0\u1DE1\u1DE2\u1DE3\u1DE4\u1DE5\u1DE6\u1DE7\u1DE8\u1DE9\u1DEA\u1DEB\u1DEC\u1DED\u1DEE\u1DEF\u1DF0\u1DF1\u1DF2\u1DF3\u1DF4\u1DF5\u1DF6\u1DF7\u1DF8\u1DF9\u1DFA\u1DFB\u1DFC\u1DFD\u1DFE\u1DFF\u20D0\u20D1\u20D2\u20D3\u20D4\u20D5\u20D6\u20D7\u20D8\u20D9\u20DA\u20DB\u20DC\u20DD\u20DE\u20DF\u20E0\u20E1\u20E2\u20E3\u20E4\u20E5\u20E6\u20E7\u20E8\u20E9\u20EA\u20EB\u20EC\u20ED\u20EE\u20EF\u20F0\u1AB0\u1AB1\u1AB2\u1AB3\u1AB4\u1AB5\u1AB6\u1AB7\u1AB8\u1AB9\u1ABA\u1ABB\u1ABC\u1ABD\u1ABE\u1ABF\u1AC0\u1AC1\u1AC2\u1AC3\u1AC4\u1AC5\u1AC6\u1AC7\u1AC8\u1AC9\u1ACA\u1ACB\u1ACC\u1ACD\u1ACE\u1ACF\u1AD0\u1AD1\u1AD2\u1AD3\u1AD4\u1AD5\u1AD6\u1AD7\u1AD8\u1AD9\u1ADA\u1ADB\u1ADC\u1ADD\u1ADE\u1ADF\u1AE0\u1AE1\u1AE2\u1AE3\u1AE4\u1AE5\u1AE6\u1AE7\u1AE8\u1AE9\u1AEA\u1AEB\u1AEC\u1AED\u1AEE\u1AEF\u1AF0\u1AF1\u1AF2\u1AF3\u1AF4\u1AF5\u1AF6\u1AF7\u1AF8\u1AF9\u1AFA\u1AFB\u1AFC\u1AFD\u1AFE\u1AFF"
                glitch_chars = "̷̸̴̶"
                text = input("Distort WHAT: ")
                distorted = ""
                for char in text:
                    distorted += char + random.choice(string.ascii_letters)
                final = ""
                for char in distorted:
                    action = random.choice(["keep", "replace", "glitch"])
                    if action == "keep":
                        final += char
                    elif action == "replace":
                        final += random.choice(string.ascii_letters)
                    elif action == "glitch":
                        final += char + random.choice(glitch_chars)
                glitched = "".join(c + random.choice(marks) for c in final)                
                print(glitched)
def login():
    global user,user_input_username,user_input_password,logged_out,userpasses
    bad = 0
    input("Press Enter to initiate login sequence: ")
    if len(userpasses)-1==0:
        print("No users exist. Creating default admin user 'chronos'.")
        userpasses["chronos"]=""
        save_user_data()
    logged_out=True
    while logged_out:
        user_input_username=input("Enter Username: ")
        user_input_password=getpass.getpass("Enter Password: ")
        if user_input_username in userpasses and userpasses[user_input_username]==user_input_password:
            print(f'User "{user_input_username}" Verified. Continue.\n{"~"*30}\n')
            user=user_input_username
            logged_out=False
            save_login_cookie(user)
            return
        else:
            print("Incorrect! Retry when prompted.\n")
            bad += 1
            if bad >= 3:
                print("Error - 403 Forbidden")
                fail = True
    if fail:
        p = files[0.5]
def run_mathtest():
    global mathtest
    if user=="chronos" or mathtest!="true":
        return
    teststype=input("What type of test? (Addition, Subtraction, Multiplication, Division)(Type something else for a random test): ")
    if teststype.lower() in ["addition","subtraction","multiplication","division"]:
        testtype=teststype.lower()
    else:
        testtype=random.choice(["addition","subtraction","multiplication","division"])
    continuetest=True
    try:
        Num1=int(input(testtype+" Test\nWhat is your first number (Make sure it isn't 0): "))
        Num2=int(input("What is your second number (Make sure it isn't 0): "))
        if Num1==0 or Num2==0:
            print("Your number is zero you bozo! START OVER")
            continuetest=False
        else:
            if testtype=="addition":
                ans=Num1+Num2
                op=" plus "
            elif testtype=="subtraction":
                ans=Num1-Num2
                op=" minus "
            elif testtype=="multiplication":
                ans=Num1*Num2
                op=" times "
            elif testtype=="division":
                if Num2==0:
                    print("Cannot divide by zero!")
                    continuetest=False
                else:
                    ans=Num1/Num2
                    op=" divided by "
        if continuetest:
            tries=1
            while True:
                try:
                    user_answer=float(input(f"What is your first number{op}your second number: "))
                    if user_answer==ans:
                        print(f"Correct! It took you {tries} tries.")
                        break
                    else:
                        print("Wrong! Try again.")
                        tries+=1
                except ValueError:
                    print("Please enter a valid number.")
    except ValueError:
        print("Invalid input. Ending test.")
while True:
    j=5
    for i in range(5):
        print(str(j)+"\n")
        j-=1
        time.sleep(1)
    print("--------------------------------------\n")
    print("Welcome to chronOS! Please log in to continue...")
    try:
        load_all_data()
        visible_users=[u for u in userpasses if u not in HIDDEN_USERS]
        print(f"Current user count: {len(visible_users)-1}")
        print(f"Available users: {visible_users}")
        create_new=input("New User? (Y/N): ").lower()
        if create_new=="y":
            if add_user():
                print("New user created successfully!")
                visible_users=[u for u in userpasses if u not in HIDDEN_USERS]
            else:
                print("Failed to create new user.")
        saved_user = load_login_cookie()
        if saved_user in userpasses:
            print(f"Auto-login: Welcome back, {saved_user}!")
            user = saved_user
            logged_out = False
        else:
            logged_out = True
        login()
        if logged_out:
            login()
        run_mathtest()
        if user=="chronos":
            terminal()
        print(endwords)
    except ValueError:
        if fromcrash:
            print("chronOS successfully crashed!")
            if not delos:
                reboot = input("Reboot? (Y/N): ").strip().lower()
                if reboot != "y":
                    print("Not Rebooting...")
                    break
                else:
                    print("Rebooting...")
                    time.sleep(5)
    except Exception as e:
        print(f"System crashed - Error code: {e}")
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
    if not fromcrash:
        print(SOD)
        print("Rebooting...")
        time.sleep(5)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
if not delos:
    print("Goodbye...\no\no\nd\nb\ny\ne")
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(2)
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
else:
    print("chronOS deleted. Flash a new OS to your system. ")
    flash(input("Enter OS name to flash (Type delOS (case - sensitive)): "))