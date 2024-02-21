from enums import Code

## Patriotic Administration Center ##
MachineGun = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.RIGHT
]

AntiMaterialRifle = [
    Code.DOWN,
    Code.LEFT,
    Code.RIGHT,
    Code.UP,
    Code.DOWN
]

Stalwart = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.UP,
    Code.LEFT
]

ExpendableAntiTank = [
    Code.DOWN,
    Code.DOWN,
    Code.LEFT,
    Code.UP,
    Code.RIGHT
]

RecoilessRifle = [
    Code.DOWN,
    Code.LEFT,
    Code.RIGHT,
    Code.RIGHT,
    Code.LEFT
]

Flamethrower = [
    Code.DOWN,
    Code.LEFT,
    Code.UP,
    Code.DOWN,
    Code.UP
]

Autocannon = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.UP,
    Code.RIGHT
]

Railgun = [
    Code.DOWN,
    Code.RIGHT,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.RIGHT
]

Spear = [
    Code.DOWN,
    Code.DOWN,
    Code.UP,
    Code.DOWN,
    Code.DOWN
]

PACList = [
    ('Machine Gun', MachineGun),
    ('Anti-Material Rifle', AntiMaterialRifle),
    ('Stalwart', Stalwart),
    ('Expendable Anti-Tank', ExpendableAntiTank),
    ('Recoiless Rifle', RecoilessRifle),
    ('Flamethrower', Flamethrower),
    ('Autocannon', Autocannon),
    ('Railgun', Railgun),
    ('Spear', Spear)
]

## Orbital Cannons ##
OrbitalGatlingBarrage = [
    Code.RIGHT,
    Code.DOWN,
    Code.LEFT,
    Code.UP,
    Code.UP
]

OrbitalAirburstStrike = [
    Code.RIGHT,
    Code.RIGHT,
    Code.RIGHT
]

Orbital120Barrage = [
    Code.RIGHT,
    Code.DOWN,
    Code.LEFT,
    Code.RIGHT,
    Code.DOWN
]

Orbital380Barrage = [
    Code.RIGHT,
    Code.DOWN,
    Code.UP,
    Code.UP,
    Code.LEFT,
    Code.DOWN,
    Code.DOWN
]

OrbitalWalkingBarrage = [
    Code.RIGHT,
    Code.RIGHT,
    Code.DOWN,
    Code.LEFT,
    Code.RIGHT,
    Code.DOWN
]

OrbitalLasers = [
    Code.RIGHT,
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.DOWN
]

OrbitalRailcannonStrike = [
    Code.RIGHT,
    Code.UP,
    Code.DOWN,
    Code.DOWN,
    Code.RIGHT
]

OrbitalCannonsList = [
    ('Orbital Gatling Barage', OrbitalGatlingBarrage),
    ('Orbital Airburst Strike', OrbitalAirburstStrike),
    ('Orbital 120mm HE Barrage', Orbital120Barrage),
    ('Orbital 380mm HE Barrage', Orbital380Barrage),
    ('Orbital Walking Barrage', OrbitalWalkingBarrage),
    ('Orbital Railcannon Strike', OrbitalRailcannonStrike)
]

## Hangar ##
EagleStrafingRun = [
    Code.UP,
    Code.RIGHT,
    Code.RIGHT
]

EagleAirstrike = [
    Code.UP,
    Code.RIGHT,
    Code.DOWN,
    Code.RIGHT
]

EagleClusterBomb = [
    Code.UP,
    Code.RIGHT,
    Code.DOWN,
    Code.DOWN,
    Code.RIGHT,
    Code.DOWN
]

EagleNapalmAirstrike = [
    Code.UP,
    Code.RIGHT,
    Code.DOWN,
    Code.UP
]

JumpPack = [
    Code.DOWN,
    Code.UP,
    Code.UP,
    Code.DOWN,
    Code.UP
]

EagleSmokeStrike = [
    Code.UP,
    Code.RIGHT,
    Code.UP,
    Code.DOWN
]

EagleRocketPods = [
    Code.UP,
    Code.RIGHT,
    Code.UP,
    Code.LEFT
]

EagleBomb = [
    Code.UP,
    Code.RIGHT,
    Code.DOWN,
    Code.DOWN,
    Code.DOWN
]

HangarList = [
    ('Eagle Strafing Run', EagleStrafingRun),
    ('Eagle Airstrike', EagleAirstrike),
    ('Eagle Cluster Bomb', EagleClusterBomb),
    ('Eagle Napam Airstrike', EagleNapalmAirstrike),
    ('Jump Pack', JumpPack),
    ('Eagle Smoke Strike', EagleSmokeStrike),
    ('Eagle 110mm Rocket Pods', EagleRocketPods),
    ('Eagle 500kg Bomb', EagleBomb)
]

## Bridge ##
OrbitalPrecisionStrike = [
    Code.LEFT,
    Code.LEFT,
    Code.UP
]

OrbitalGasStrike = [
    Code.RIGHT,
    Code.RIGHT,
    Code.DOWN,
    Code.RIGHT
]

OrbitalEMSStrike = [
    Code.RIGHT,
    Code.RIGHT,
    Code.LEFT,
    Code.DOWN
]

OrbitalSmokeStrike = [
    Code.RIGHT,
    Code.RIGHT,
    Code.DOWN,
    Code.UP
]

HMGEmplacement = [
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.RIGHT,
    Code.RIGHT,
    Code.LEFT
]

ShieldGenerationRelay = [
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.DOWN,
    Code.RIGHT,
    Code.RIGHT
]

TeslaTower = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.UP,
    Code.LEFT,
    Code.RIGHT
]

BridgeList = [
    ('Orbital Precision Strike', OrbitalPrecisionStrike),
    ('Orbital Gas Strike', OrbitalGasStrike),
    ('Orbital EMS Strike', OrbitalEMSStrike),
    ('Orbital Smoke Strike', OrbitalSmokeStrike),
    ('HMG Emplacement', HMGEmplacement),
    ('Shield Generation Relay', ShieldGenerationRelay),
    ('Tesla Tower', TeslaTower)
]

## Engineering Bay ##
AntiPersonnelMinefield = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.RIGHT
]

SupplyPack = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP, 
    Code.UP,
    Code.DOWN
]

GrenadeLauncher = [
    Code.DOWN,
    Code.LEFT,
    Code.UP,
    Code.LEFT,
    Code.DOWN
]

LaserCannon = [
    Code.DOWN,
    Code.LEFT,
    Code.DOWN,
    Code.UP,
    Code.LEFT
]

IncendiaryMines = [
    Code.DOWN,
    Code.LEFT,
    Code.LEFT,
    Code.DOWN
]

GuardDogRover = [
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.UP,
    Code.RIGHT,
    Code.RIGHT
]

BallisticShieldBackpack = [
    Code.DOWN,
    Code.LEFT,
    Code.UP,
    Code.UP,
    Code.RIGHT
]

ArcThrower = [
    Code.DOWN,
    Code.RIGHT,
    Code.UP,
    Code.LEFT,
    Code.DOWN
]

ShieldGeneratorPack = [
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.RIGHT,
    Code.LEFT,
    Code.RIGHT
]

EngineeringList = [
    ('Anti-Personnel Minefield', AntiPersonnelMinefield),
    ('Supply Pack', SupplyPack),
    ('Grenade Launcher', GrenadeLauncher),
    ('Laser Cannon', LaserCannon),
    ('Incendiary Mines', IncendiaryMines),
    ('\"Guard Dog\" Rover', GuardDogRover),
    ('Ballistic Shield Backpack', BallisticShieldBackpack),
    ('Arc Thrower', ArcThrower),
    ('Shield Generator Pack', ShieldGeneratorPack)
]

## Robotics Workshop ##
MachineGunSentry = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.DOWN,
    Code.RIGHT,
    Code.DOWN,
    Code.UP
]

GatlingSentry = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.LEFT
]

MortarSentry = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.LEFT
]

GuardDog = [
    Code.DOWN,
    Code.UP,
    Code.LEFT,
    Code.UP,
    Code.RIGHT,
    Code.DOWN
]

AutoCannonSentry = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.UP,
    Code.LEFT,
    Code.UP
]

RocketSentry = [
    Code.DOWN,
    Code.UP,
    Code.RIGHT,
    Code.UP,
    Code.LEFT,
    Code.UP
]

EMSMortarSentry = [
    Code.DOWN,
    Code.DOWN,
    Code.UP,
    Code.UP,
    Code.LEFT
]

RoboticsList = [
    ('Machine Gun Sentry', MachineGunSentry),
    ('Gatling Sentry', GatlingSentry),
    ('Mortar Sentry', MortarSentry),
    ('\"Guard Dog\"', GuardDog),
    ('Auto Cannon Sentry', AutoCannonSentry),
    ('Rocket Sentry', RocketSentry),
    ('EMS Mortar Sentry', EMSMortarSentry)
]

## Center ##
CenterList = [
    PACList,
    OrbitalCannonsList,
    HangarList,
    BridgeList,
    EngineeringList,
    RoboticsList
]