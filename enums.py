from enum import Enum


class WorkClass(str, Enum):
    STATE_GOV = "State-gov"
    SELF_EMP_NOT_INC = "Self-emp-not-inc"
    PRIVATE = "Private"
    FEDERAL_GOV = "Federal-gov"
    LOCAL_GOV = "Local-gov"
    UNKNOWN = "?"
    SELF_EMP_INC = "Self-emp-inc"
    WITHOUT_PAY = "Without-pay"
    NEVER_WORKED = "Never-worked"


class Education(str, Enum):
    BACHELORS = "Bachelors"
    HS_GRAD = "HS-grad"
    ELEVENTH = "11th"
    MASTERS = "Masters"
    NINTH = "9th"
    SOME_COLLEGE = "Some-college"
    ASSOC_ACDM = "Assoc-acdm"
    ASSOC_VOC = "Assoc-voc"
    SEVENTH_EIGHTH = "7th-8th"
    DOCTORATE = "Doctorate"
    PROF_SCHOOL = "Prof-school"
    FIFTH_SIXTH = "5th-6th"
    TENTH = "10th"
    FIRST_FOURTH = "1st-4th"
    PRESCHOOL = "Preschool"
    TWELFTH = "12th"


class MaritalStatus(str, Enum):
    NEVER_MARRIED = "Never-married"
    MARRIED_CIV_SPOUSE = "Married-civ-spouse"
    DIVORCED = "Divorced"
    MARRIED_SPOUSE_ABSENT = "Married-spouse-absent"
    SEPARATED = "Separated"
    MARRIED_AF_SPOUSE = "Married-AF-spouse"
    WIDOWED = "Widowed"


class Occupation(str, Enum):
    ADM_CLERICAL = "Adm-clerical"
    EXEC_MANAGERIAL = "Exec-managerial"
    HANDLERS_CLEANERS = "Handlers-cleaners"
    PROF_SPECIALTY = "Prof-specialty"
    OTHER_SERVICE = "Other-service"
    SALES = "Sales"
    CRAFT_REPAIR = "Craft-repair"
    TRANSPORT_MOVING = "Transport-moving"
    FARMING_FISHING = "Farming-fishing"


class Relationship(str, Enum):
    NOT_IN_FAMILY = "Not-in-family"
    HUSBAND = "Husband"
    WIFE = "Wife"
    OWN_CHILD = "Own-child"
    UNMARRIED = "Unmarried"
    OTHER_RELATIVE = "Other-relative"


class Race(str, Enum):
    WHITE = "White"
    BLACK = "Black"
    ASIAN_PAC_ISLANDER = "Asian-Pac-Islander"
    AMER_INDIAN_ESKIMO = "Amer-Indian-Eskimo"
    OTHER = "Other"


class Sex(str, Enum):
    MALE = "Male"
    FEMALE = "Female"


class NativeCountry(str, Enum):
    UNITED_STATES = "United-States"
    CAMBODIA = "Cambodia"
    ENGLAND = "England"
    PUERTO_RICO = "Puerto-Rico"
    CANADA = "Canada"
    GERMANY = "Germany"
    OUTLYING_US = "Outlying-US(Guam-USVI-etc)"
    INDIA = "India"
    JAPAN = "Japan"
    GREECE = "Greece"
    SOUTH = "South"
    CHINA = "China"
    CUBA = "Cuba"
    IRAN = "Iran"
    HONDURAS = "Honduras"
    PHILIPPINES = "Philippines"
    ITALY = "Italy"
    POLAND = "Poland"
    JAMAICA = "Jamaica"
    VIETNAM = "Vietnam"
    MEXICO = "Mexico"
    PORTUGAL = "Portugal"
    IRELAND = "Ireland"
    FRANCE = "France"
    DOMINICAN_REPUBLIC = "Dominican-Republic"
    LAOS = "Laos"
    ECUADOR = "Ecuador"
    TAIWAN = "Taiwan"
    HAITI = "Haiti"
    COLUMBIA = "Columbia"
    HUNGARY = "Hungary"
    GUATEMALA = "Guatemala"
    NICARAGUA = "Nicaragua"
    SCOTLAND = "Scotland"
    THAILAND = "Thailand"
    YUGOSLAVIA = "Yugoslavia"
    EL_SALVADOR = "El-Salvador"
    TRINADAD_TOBAGO = "Trinadad&Tobago"
    PERU = "Peru"
    HONG = "Hong"
    HOLAND_NETHERLANDS = "Holand-Netherlands"
