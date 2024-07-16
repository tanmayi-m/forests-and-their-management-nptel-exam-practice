import csv

questions = [
    {
        "Question": "Tropical moist forests do not include",
        "Option A": "broadleaved forests",
        "Option B": "wet evergreen forests",
        "Option C": "semi-evergreen forests",
        "Option D": "moist deciduous forests",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a use value?",
        "Option A": "direct value",
        "Option B": "indirect value",
        "Option C": "option value",
        "Option D": "existence value",
        "Correct Option": ""
    },
    {
        "Question": "The value derived from the knowledge of use of resources by others in the current generation is called",
        "Option A": "altruistic value",
        "Option B": "bequest value",
        "Option C": "existence value",
        "Option D": "option value",
        "Correct Option": ""
    },
    {
        "Question": "Montane sub-tropical forests do not include",
        "Option A": "broadleaved forests",
        "Option B": "pine forests",
        "Option C": "semi-evergreen forests",
        "Option D": "dry evergreen forests",
        "Correct Option": ""
    },
    {
        "Question": "“Plant community, predominantly comprised of trees and other woody vegetation, usually with a closed canopy\" is",
        "Option A": "silvicultural definition of forests",
        "Option B": "FAO definition of forests",
        "Option C": "legal definition of forests",
        "Option D": "ecological definition of forests",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a consumptive value?",
        "Option A": "timber",
        "Option B": "firewood",
        "Option C": "non-timber forest products",
        "Option D": "education",
        "Correct Option": ""
    },
    {
        "Question": "The term 'forest' originates from",
        "Option A": "Latin foris meaning outside",
        "Option B": "Greek foris meaning outside",
        "Option C": "Latin foris meaning trees",
        "Option D": "Greek foris meaning trees",
        "Correct Option": ""
    },
    {
        "Question": "The value of leaving use and non-use values for offspring's or future generations is called",
        "Option A": "altruistic value",
        "Option B": "bequest value",
        "Option C": "existence value",
        "Option D": "option value",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a forest type found in India?",
        "Option A": "Mediterranean dry",
        "Option B": "Tropical dry",
        "Option C": "Montane temperate",
        "Option D": "Alpine",
        "Correct Option": ""
    },
    {
        "Question": "According to the Supreme Court, the term forest land includes",
        "Option A": "some area recorded as forest in the Government record according to ownership",
        "Option B": "any area recorded as forest in the Government record according to ownership",
        "Option C": "some area recorded as forest in the Government record irrespective of ownership",
        "Option D": "any area recorded as forest in the Government record irrespective of ownership",
        "Correct Option": ""
    },
    {
        "Question": "In the context of plant nutrition, boron is",
        "Option A": "macronutrient",
        "Option B": "micronutrient",
        "Option C": "primary nutrient",
        "Option D": "secondary nutrient",
        "Correct Option": ""
    },
    {
        "Question": "The art and science of cultivating forest crops is called",
        "Option A": "foresticulture",
        "Option B": "monoculture",
        "Option C": "silviculture",
        "Option D": "silvics",
        "Correct Option": ""
    },
    {
        "Question": "The climax near Tindni village is being controlled by disturbance by cattle. This is an example of",
        "Option A": "climatic climax",
        "Option B": "edaphic climax",
        "Option C": "disclimax",
        "Option D": "catastrophic climax",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a characteristic of pioneer species",
        "Option A": "ability to grow on bare rocks",
        "Option B": "ability to tolerate extreme temperatures",
        "Option C": "large size",
        "Option D": "short life span",
        "Correct Option": ""
    },
    {
        "Question": "Which of these depicts correctly the lithosere primary succession?",
        "Option A": "Rock → Crustose lichen → Foliose lichen → Moss → Herbaceous stage → Shrub →Woodland → Climax",
        "Option B": "Rock → Foliose lichen → Crustose lichen → Moss → Herbaceous stage → Shrub →Woodland → Climax",
        "Option C": "Moss → Crustose lichen → Foliose lichen → Rock → Herbaceous stage → Shrub →Woodland → Climax",
        "Option D": "Rock → Crustose lichen → Foliose lichen → Shrub → Herbaceous stage → Moss →Woodland → Climax",
        "Correct Option": ""
    },
    {
        "Question": "The study of life history or general features of forest crops with respect to environmental factors is called",
        "Option A": "foresticulture",
        "Option B": "monoculture",
        "Option C": "silviculture",
        "Option D": "silvics",
        "Correct Option": ""
    },
    {
        "Question": "Net primary productivity is given by",
        "Option A": "APAR + LUE",
        "Option B": "APAR x LUE",
        "Option C": "APAR - LUE",
        "Option D": "APAR by LUE",
        "Correct Option": ""
    },
    {
        "Question": "A climax caused by wildfires is an example of",
        "Option A": "climatic climax",
        "Option B": "edaphic climax",
        "Option C": "disclimax",
        "Option D": "catastrophic climax",
        "Correct Option": ""
    },
    {
        "Question": "Practical application of scientific, technical and economic principles of forestry comes under which branch of forestry?",
        "Option A": "forest management",
        "Option B": "forest economics",
        "Option C": "forest mensuration",
        "Option D": "forest protection",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is abiotic factor?",
        "Option A": "vines",
        "Option B": "trees",
        "Option C": "reptiles",
        "Option D": "water",
        "Correct Option": ""
    },
    {
        "Question": "Regur is a term for",
        "Option A": "black cotton soil",
        "Option B": "alluvial soil",
        "Option C": "saline soil",
        "Option D": "red and yellow soil",
        "Correct Option": ""
    },
    {
        "Question": "Carbonation is an example of",
        "Option A": "chemical weathering",
        "Option B": "physical weathering",
        "Option C": "biological weathering",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Bangar is a type of",
        "Option A": "black cotton soil",
        "Option B": "alluvial soil",
        "Option C": "saline soil",
        "Option D": "red and yellow soil",
        "Correct Option": ""
    },
    {
        "Question": "Cryofracturing is an example of",
        "Option A": "chemical weathering",
        "Option B": "physical weathering",
        "Option C": "biological weathering",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "In soil profile, C refers to",
        "Option A": "organic surface layer",
        "Option B": "topsoil layer",
        "Option C": "subsoil layer",
        "Option D": "substratum layer",
        "Correct Option": ""
    },
    {
        "Question": "Vertical arrangement of soil horizons is called",
        "Option A": "soil texture",
        "Option B": "soil structure",
        "Option C": "soil profile",
        "Option D": "soil science",
        "Correct Option": ""
    },
    {
        "Question": "Thermal stresses lead to",
        "Option A": "chemical weathering",
        "Option B": "physical weathering",
        "Option C": "biological weathering",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Khadar is a type of",
        "Option A": "black cotton soil",
        "Option B": "alluvial soil",
        "Option C": "saline soil",
        "Option D": "red and yellow soil",
        "Correct Option": ""
    },
    {
        "Question": "Hydrolysis is an example of",
        "Option A": "chemical weathering",
        "Option B": "physical weathering",
        "Option C": "biological weathering",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Which of these has the highest organic matter content?",
        "Option A": "peaty soil",
        "Option B": "alluvial soil",
        "Option C": "saline soil",
        "Option D": "red and yellow soil",
        "Correct Option": ""
    },
    {
        "Question": "Measurement of height based on similar triangles comes under:",
        "Option A": "similar measurement",
        "Option B": "dissimilar measurement",
        "Option C": "direct measurement",
        "Option D": "indirect measurement",
        "Correct Option": ""
    },
    {
        "Question": "For normal form factor, the reference for the base of the cylinder is",
        "Option A": "base of the tree",
        "Option B": "breast height",
        "Option C": "10 percent of tree height",
        "Option D": "20 percent of tree height",
        "Correct Option": ""
    },
    {
        "Question": "In a triangle, the angle between base and hypotenuse, θ = 60° and the hypotenuse c = 2 cm. Find the length of the base b.",
        "Option A": "0.33",
        "Option B": "0.5",
        "Option C": "0.75",
        "Option D": "1",
        "Correct Option": ""
    },
    {
        "Question": "3 trees are located in a sample plot of 15 m x 15 m. Their dbh are as under: dbh = 25 cm, 30 cm, 35 cm. Find the stand basal area in sq m per Ha.",
        "Option A": "9.6",
        "Option B": "14.6",
        "Option C": "21.6",
        "Option D": "27.6",
        "Correct Option": ""
    },
    {
        "Question": "Consider a stand of eucalyptus trees that are on average 30 cm in diameter and spaced on a regular 3 m griFind the spacing factor.",
        "Option A": "5",
        "Option B": "10",
        "Option C": "15",
        "Option D": "data insufficient",
        "Correct Option": ""
    },
    {
        "Question": "For a tree with dbh = 45.6 cm, height = 27 m and total stem volume of 1.78 cum, the artificial form factor for the tree is:",
        "Option A": "0.1",
        "Option B": "0.2",
        "Option C": "0.3",
        "Option D": "0.4",
        "Correct Option": ""
    },
    {
        "Question": "For absolute form factor, the reference for the base of the cylinder is",
        "Option A": "base of the tree",
        "Option B": "breast height",
        "Option C": "10 percent of tree height",
        "Option D": "20 percent of tree height",
        "Correct Option": ""
    },
    {
        "Question": "Diameter over bark (dob), diameter under bark (dub) and bark thickness (tb) are related as:",
        "Option A": "dob = dub + tb",
        "Option B": "dob = dub - tb",
        "Option C": "dob = dub + 2 x tb",
        "Option D": "dob = dub - 2 x tb",
        "Correct Option": ""
    },
    {
        "Question": "Choose the correct statement:",
        "Option A": "For a non-circular cross-section, girth tape over-estimates the sectional area.",
        "Option B": "For a non-circular cross-section, girth tape under-estimates the sectional area.",
        "Option C": "For a non-circular cross-section, girth tape correctly estimates the sectional area.",
        "Option D": "None of these is a correct statement.",
        "Correct Option": ""
    },
    {
        "Question": "A tree has dbh of 25 cm. Find its basal area in sq m.",
        "Option A": ".049",
        "Option B": ".096",
        "Option C": ".149",
        "Option D": ".195",
        "Correct Option": ""
    },
    {
        "Question": "The frequency of flyovers is an indicator of",
        "Option A": "spatial resolution",
        "Option B": "temporal resolution",
        "Option C": "spectral resolution",
        "Option D": "radiometric resolution",
        "Correct Option": ""
    },
    {
        "Question": "___ is how close the measured values are to the correct value.",
        "Option A": "Accuracy",
        "Option B": "Precision",
        "Option C": "Bias",
        "Option D": "Variance",
        "Correct Option": ""
    },
    {
        "Question": "“This sampling employs a simple rule of selecting every kth unit starting with a number chosen at random from 1 to k as the random start.” We're talking about",
        "Option A": "Simple random sampling",
        "Option B": "Systematic sampling",
        "Option C": "Stratified sampling",
        "Option D": "Multistage sampling",
        "Correct Option": ""
    },
    {
        "Question": "A list of sampling units is called a",
        "Option A": "frame",
        "Option B": "window",
        "Option C": "sample",
        "Option D": "population",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is correct?",
        "Option A": "Plane surveying takes into account the true shape of the Earth and is used for smaller areas (< 250 sq km)",
        "Option B": "Plane surveying takes into account the true shape of the Earth and is used for larger areas (> 250 sq km)",
        "Option C": "Geodetic surveying takes into account the true shape of the Earth and is used for smaller areas (< 250 sq km)",
        "Option D": "Geodetic surveying takes into account the true shape of the Earth and is used for larger areas (> 250 sq km)",
        "Correct Option": ""
    },
    {
        "Question": "A sampling procedure such that each possible combination of sampling units out of the population has the same chance of being selected is referred to as",
        "Option A": "Simple random sampling",
        "Option B": "Systematic sampling",
        "Option C": "Stratified sampling",
        "Option D": "Multistage sampling",
        "Correct Option": ""
    },
    {
        "Question": "Bathymetric LiDAR uses",
        "Option A": "far infrared light",
        "Option B": "near infrared light",
        "Option C": "orange light",
        "Option D": "green light",
        "Correct Option": ""
    },
    {
        "Question": "IMU stands for",
        "Option A": "Imperial metering unit",
        "Option B": "Inertial metering unit",
        "Option C": "Imperial measurement unit",
        "Option D": "Inertial measurement unit",
        "Correct Option": ""
    },
    {
        "Question": "___ is how close the measured values are to each other.",
        "Option A": "Accuracy",
        "Option B": "Precision",
        "Option C": "Bias",
        "Option D": "Variance",
        "Correct Option": ""
    },
    {
        "Question": "The time of flight for LiDAR is 0.00001 seFind the distance of the object from the instrument.",
        "Option A": "500 m",
        "Option B": "1000 m",
        "Option C": "1500 m",
        "Option D": "2000 m",
        "Correct Option": ""
    },
    {
        "Question": "A scientist uses a trap to capture a monkey. In the context of Wildlife Protection Act 1972,",
        "Option A": "the trap is a weapon and capturing is hunting.",
        "Option B": "the trap is not a weapon and capturing is hunting.",
        "Option C": "the trap is a weapon and capturing is not hunting.",
        "Option D": "the trap is not a weapon and capturing is not hunting.",
        "Correct Option": ""
    },
    {
        "Question": "In the formula I = PXAXT, P refers to",
        "Option A": "professional pressure",
        "Option B": "pollution pressure",
        "Option C": "population pressure",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is a deterministic factor?",
        "Option A": "environmental variation",
        "Option B": "forest fire",
        "Option C": "death rate",
        "Option D": "diseases",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is a stochastic factor?",
        "Option A": "birth rate",
        "Option B": "death rate",
        "Option C": "population structure",
        "Option D": "forest fire",
        "Correct Option": ""
    },
    {
        "Question": "In the formula I = PXAXT, T refers to",
        "Option A": "transference",
        "Option B": "time",
        "Option C": "technology",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Which of these forms the fire triangle?",
        "Option A": "fire, air, heat",
        "Option B": "fire, oxygen, wood",
        "Option C": "fuel, air, wood",
        "Option D": "fuel, oxygen, heat",
        "Correct Option": ""
    },
    {
        "Question": "A veterinarian uses an immobilising gun to capture a deer. In the context of Wildlife Protection Act 1972,",
        "Option A": "the immobilising gun is a weapon and capturing is hunting.",
        "Option B": "the immobilising gun is not a weapon and capturing is hunting.",
        "Option C": "the immobilising gun is a weapon and capturing is not hunting.",
        "Option D": "the immobilising gun is not a weapon and capturing is not hunting.",
        "Correct Option": ""
    },
    {
        "Question": "Invasive climbers increase the probability of which of these fire types?",
        "Option A": "ground fire",
        "Option B": "surface fire",
        "Option C": "ladder fire",
        "Option D": "firestorm",
        "Correct Option": ""
    },
    {
        "Question": "The acronym HIPPO does not include",
        "Option A": "habitat loss",
        "Option B": "habitat enhancement",
        "Option C": "over-harvesting",
        "Option D": "human over-population",
        "Correct Option": ""
    },
    {
        "Question": "The acronym HIPPO does not include",
        "Option A": "habitat loss",
        "Option B": "invasive species",
        "Option C": "pollination",
        "Option D": "pollution",
        "Correct Option": ""
    },
    {
        "Question": "A site was clear-cut. Which of these methods of regeneration cannot be used in a short time-frame?",
        "Option A": "natural regeneration",
        "Option B": "artificial regeneration by direct sowing",
        "Option C": "artificial regeneration by planting seedlings",
        "Option D": "artificial regeneration by transplanting trees",
        "Correct Option": ""
    },
    {
        "Question": "Average age at which a tree is considered mature for felling is called as",
        "Option A": "crop age",
        "Option B": "felling age",
        "Option C": "rotation age",
        "Option D": "maturity age",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a feature of natural regeneration",
        "Option A": "low cost",
        "Option B": "less requirement of heavy machinery and labour",
        "Option C": "preservation of genetic variability",
        "Option D": "good control over genetic improvement",
        "Correct Option": ""
    },
    {
        "Question": "Ring weeding is primarily a feature of",
        "Option A": "natural regeneration",
        "Option B": "assisted natural regeneration",
        "Option C": "artificial regeneration by direct sowing",
        "Option D": "artificial regeneration by planting seedlings",
        "Correct Option": ""
    },
    {
        "Question": "The movement of seeds away from their place of seed production into a new area is called",
        "Option A": "translocation",
        "Option B": "migration",
        "Option C": "dispersal",
        "Option D": "drifting",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a feature of natural regeneration",
        "Option A": "seed consumption by insects and seed feeders",
        "Option B": "little control over spacing and stand density",
        "Option C": "long time needed to regenerate forest",
        "Option D": "high requirement of heavy machinery and labour",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is the correct sequence of a silvicultural system?",
        "Option A": "Stand tending -> Regeneration -> Harvesting",
        "Option B": "Harvesting -> Stand tending -> Regeneration",
        "Option C": "Harvesting -> Regeneration -> Stand tending",
        "Option D": "Regeneration -> Harvesting -> Stand tending",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not advantage of clear felling system",
        "Option A": "Simple system, easy and efficient operations",
        "Option B": "Allows for establishment of a more uniform crop",
        "Option C": "Increases soil erosion and landslides in hilly areas",
        "Option D": "Mimics natural processes of fire and large-scale insect attacks",
        "Correct Option": ""
    },
    {
        "Question": "Tending is done during",
        "Option A": "early stage of life",
        "Option B": "middle stage of life",
        "Option C": "late stage of life",
        "Option D": "any stage of life",
        "Correct Option": ""
    },
    {
        "Question": "Taungya regeneration is",
        "Option A": "natural regeneration",
        "Option B": "artificial regeneration with villagers",
        "Option C": "artificial regeneration with nomadic tribes",
        "Option D": "artificial regeneration with hunters and gatherers",
        "Correct Option": ""
    },
    {
        "Question": "Trees not putting increment are removed during",
        "Option A": "preparatory felling",
        "Option B": "seeding felling",
        "Option C": "secondary felling",
        "Option D": "final felling",
        "Correct Option": ""
    },
    {
        "Question": "For a crop with rotation age of 120 years, PB-III would have crop age",
        "Option A": "0-30 years",
        "Option B": "30-60 years",
        "Option C": "60-90 years",
        "Option D": "90-120 years",
        "Correct Option": ""
    },
    {
        "Question": "Close to nature forestry is a feature of",
        "Option A": "clear felling system",
        "Option B": "selection system",
        "Option C": "uniform shelterwood system",
        "Option D": "group shelterwood system",
        "Correct Option": ""
    },
    {
        "Question": "Shelterwood system results in",
        "Option A": "even aged stand with natural aesthetics",
        "Option B": "even aged stand with artificial aesthetics",
        "Option C": "uneven aged stand with natural aesthetics",
        "Option D": "uneven aged stand with artificial aesthetics",
        "Correct Option": ""
    },
    {
        "Question": "Inverse-J shaped number-diameter curves are seen in",
        "Option A": "clear felling system",
        "Option B": "selection system",
        "Option C": "uniform shelterwood system",
        "Option D": "group shelterwood system",
        "Correct Option": ""
    },
    {
        "Question": "Clear felling system is not used for",
        "Option A": "light demanding species",
        "Option B": "shade bearer species",
        "Option C": "plain areas",
        "Option D": "plateau areas",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is the correct sequence for shelterwood system?",
        "Option A": "Preparatory felling ->Secondary felling -> Seedling felling -> Final felling",
        "Option B": "Preparatory felling -> Seedling felling -> Secondary felling -> Final felling",
        "Option C": "Preparatory felling ->Secondary felling -> Seeding felling -> Final felling",
        "Option D": "Preparatory felling -> Seeding felling -> Secondary felling -> Final felling",
        "Correct Option": ""
    },
    {
        "Question": "Felling made with the object of opening the canopy to remove shelter and allow more light for the regenerated crop is",
        "Option A": "preparatory felling",
        "Option B": "seeding felling",
        "Option C": "secondary felling",
        "Option D": "final felling",
        "Correct Option": ""
    },
    {
        "Question": "In group shelterwood system, the regeneration area is increased",
        "Option A": "centrifugally around gaps",
        "Option B": "centripetally around gaps",
        "Option C": "parallel to gaps",
        "Option D": "perpendicular to gaps",
        "Correct Option": ""
    },
    {
        "Question": "Catchment areas are best suited for",
        "Option A": "clear felling system",
        "Option B": "selection system",
        "Option C": "uniform shelterwood system",
        "Option D": "group shelterwood system",
        "Correct Option": ""
    },
    {
        "Question": "Moving of logs from forest to landing area is known as",
        "Option A": "marking",
        "Option B": "bucking",
        "Option C": "skidding",
        "Option D": "delimbing",
        "Correct Option": ""
    },
    {
        "Question": "Research plots are shown in ___ marking colour",
        "Option A": "yellow",
        "Option B": "blue",
        "Option C": "red",
        "Option D": "white",
        "Correct Option": ""
    },
    {
        "Question": "Which of these gives the greatest accuracy in constructing face cuts",
        "Option A": "conventional face",
        "Option B": "humboldt face",
        "Option C": "open face",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "Careful selection of trees for harvesting based on a forest management prescription is known as",
        "Option A": "surveying",
        "Option B": "cruising",
        "Option C": "marking",
        "Option D": "logging",
        "Correct Option": ""
    },
    {
        "Question": "Surveying timberlands to locate and estimate the volumes and grades of standing timber meeting requirements is known as",
        "Option A": "surveying",
        "Option B": "cruising",
        "Option C": "marking",
        "Option D": "logging",
        "Correct Option": ""
    },
    {
        "Question": "Trees on boundary are shown in ___ marking colour",
        "Option A": "yellow",
        "Option B": "blue",
        "Option C": "red",
        "Option D": "white",
        "Correct Option": ""
    },
    {
        "Question": "Cutting of timber into logs is known as",
        "Option A": "marking",
        "Option B": "bucking",
        "Option C": "skidding",
        "Option D": "delimbing",
        "Correct Option": ""
    },
    {
        "Question": "Which of these gives the greatest saving of lumber",
        "Option A": "conventional face",
        "Option B": "humboldt face",
        "Option C": "open face",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "Trees to be retained are shown in ___ marking colour",
        "Option A": "yellow",
        "Option B": "blue",
        "Option C": "red",
        "Option D": "white",
        "Correct Option": ""
    },
    {
        "Question": "Net growth in initial volume is given by",
        "Option A": "V2-V1",
        "Option B": "V2-V1+H-I",
        "Option C": "V2-V1+H-I+M",
        "Option D": "V2-V1+H-I-M",
        "Correct Option": ""
    },
    {
        "Question": "Shell cracking of seeds is used for which species",
        "Option A": "amla",
        "Option B": "mango",
        "Option C": "ber",
        "Option D": "teak",
        "Correct Option": ""
    },
    {
        "Question": "Wet and dry treatment of seeds is used for which species",
        "Option A": "amla",
        "Option B": "mango",
        "Option C": "ber",
        "Option D": "teak",
        "Correct Option": ""
    },
    {
        "Question": "Agave is used for",
        "Option A": "barbed wire fencing",
        "Option B": "live fencing",
        "Option C": "chain link fencing",
        "Option D": "stone wall fencing",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a laboratory method to determine best days for seed collection?",
        "Option A": "maximum dry weight",
        "Option B": "colour of fruits",
        "Option C": "moisture content of fruits",
        "Option D": "chemical analysis of fat and nitrogen content",
        "Correct Option": ""
    },
    {
        "Question": "Which of these characterises a refractory site",
        "Option A": "soil depth < 10 cm",
        "Option B": "soil depth 10-30 cm",
        "Option C": "soil depth > 30 cm",
        "Option D": "none of these",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is a good storage condition",
        "Option A": "high moisture, high temperature",
        "Option B": "high moisture, low temperature",
        "Option C": "low moisture, high temperature",
        "Option D": "low moisture, low temperature",
        "Correct Option": ""
    },
    {
        "Question": "Which of these prevents water logging",
        "Option A": "sunken bed",
        "Option B": "raised bed",
        "Option C": "flat bed",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "Choice of spacing is dependent upon",
        "Option A": "objective of plantation",
        "Option B": "site-species matching",
        "Option C": "growth rate",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "Which of these conserves moisture",
        "Option A": "sunken bed",
        "Option B": "raised bed",
        "Option C": "flat bed",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "Number of seeds in sample that germinate upto the peak germination period expressed as percent is a definition of",
        "Option A": "germination number",
        "Option B": "germination percentage",
        "Option C": "germination energy",
        "Option D": "germination power",
        "Correct Option": ""
    },
    {
        "Question": "The tiger has a home range of several square kilometres, regulates the ecosystem through controlling herbivore populations and trophic cascades, and people come to tiger reserves to watch tigers. Thus, the tiger can be called as",
        "Option A": "umbrella species",
        "Option B": "keystone species",
        "Option C": "flagship species",
        "Option D": "all of the above",
        "Correct Option": ""
    },
    {
        "Question": "Zoo is an example of",
        "Option A": "in-situ conservation",
        "Option B": "ex-situ conservation",
        "Option C": "in-situ preservation",
        "Option D": "ex-situ preservation",
        "Correct Option": ""
    },
    {
        "Question": "Sustainable harvest of resources falls under the category of:",
        "Option A": "conservation",
        "Option B": "preservation",
        "Option C": "environmentalism",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "We prefer those areas for the creation of a conservation reserve where the level of threat is",
        "Option A": "very high",
        "Option B": "medium",
        "Option C": "very low",
        "Option D": "non-existent",
        "Correct Option": ""
    },
    {
        "Question": "Captive breeding is an example of",
        "Option A": "in-situ conservation",
        "Option B": "ex-situ conservation",
        "Option C": "in-situ preservation",
        "Option D": "ex-situ preservation",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a forest classification as per the 1894 Forest Policy:",
        "Option A": "protection forest",
        "Option B": "production forest",
        "Option C": "minor forest",
        "Option D": "major forest",
        "Correct Option": ""
    },
    {
        "Question": "In 1931, Van Panchayats were constituted in areas that are now in",
        "Option A": "Tamil Nadu",
        "Option B": "Madhya Pradesh",
        "Option C": "West Bengal",
        "Option D": "Uttarakhand",
        "Correct Option": ""
    },
    {
        "Question": "Planting along canal banks is a part of",
        "Option A": "farm forestry",
        "Option B": "community forestry",
        "Option C": "extension forestry",
        "Option D": "agroforestry",
        "Correct Option": ""
    },
    {
        "Question": "The fig tree bears fruits in times when animals do not have much access to fooIn this context, it would be a good example of",
        "Option A": "least concern species",
        "Option B": "keystone species",
        "Option C": "flagship species",
        "Option D": "extinct species",
        "Correct Option": ""
    },
    {
        "Question": "The elephant has a home range of several square kilometres, regulates the ecosystem by its habit of destructive feeding, and people can relate to this animal which is important for conservation. Given this background, the elephant can be called as",
        "Option A": "umbrella species",
        "Option B": "keystone species",
        "Option C": "flagship species",
        "Option D": "all of the above",
        "Correct Option": ""
    },
    {
        "Question": "A tree has dbh of 35 cm. Find its basal area in sq m.",
        "Option A": ".049",
        "Option B": ".096",
        "Option C": ".149",
        "Option D": ".195",
        "Correct Option": ""
    },
    {
        "Question": "In a triangle, the angle between base and hypotenuse, θ = 60° and the hypotenuse c = 4 cm. Find the length of the base b.",
        "Option A": "0.66",
        "Option B": "1",
        "Option C": "1.5",
        "Option D": "2",
        "Correct Option": ""
    },
    {
        "Question": "“allowing some places and some creatures to exist without significant human interference” is a definition of",
        "Option A": "conservation",
        "Option B": "preservation",
        "Option C": "environmentalism",
        "Option D": "all of these",
        "Correct Option": ""
    },
    {
        "Question": "In India, the breast height is considered to be",
        "Option A": "1.37 m",
        "Option B": "1.47 m",
        "Option C": "1.57 m",
        "Option D": "2.47 m",
        "Correct Option": ""
    },
    {
        "Question": "The term laterite soil is derived from Latin later which means",
        "Option A": "red",
        "Option B": "brick",
        "Option C": "fertile",
        "Option D": "infertile",
        "Correct Option": ""
    },
    {
        "Question": "Which of these is not a non-use value?",
        "Option A": "direct value",
        "Option B": "existence value",
        "Option C": "altruistic value",
        "Option D": "bequest value",
        "Correct Option": ""
    },
    {
        "Question": "“Science of relationships between organisms and their environments” is the definition of:",
        "Option A": "conservation",
        "Option B": "preservation",
        "Option C": "environmentalism",
        "Option D": "ecology",
        "Correct Option": ""
    },
    {
        "Question": "Self ploughing character is seen in",
        "Option A": "black cotton soil",
        "Option B": "alluvial soil",
        "Option C": "saline soil",
        "Option D": "red and yellow soil",
        "Correct Option": ""
    },
    {
        "Question": "Mechanical action of ocean waves is an example of",
        "Option A": "chemical weathering",
        "Option B": "physical weathering",
        "Option C": "biological weathering",
        "Option D": "none of the above",
        "Correct Option": ""
    },
    {
        "Question": "Lithosere is an example of",
        "Option A": "hydrosere",
        "Option B": "xerosere",
        "Option C": "psammosere",
        "Option D": "halosere",
        "Correct Option": ""
    }
]

# Define the CSV file and fieldnames
csv_file = 'forestsquestions.csv'
fieldnames = ["S.No.", "Question", "OptionA", "OptionB", "OptionC", "OptionD", "CorrectOption"]

# Create or open the CSV file and append the questions
with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Check if the file is empty
    if csvfile.tell() == 0:
        # If the file is empty, write the headers
        writer.writeheader()
    
    # Append questions to the file
    for i, question in enumerate(questions, start=1):
        # Print the question for debugging purposes
        print(f"Debugging Question {i}: {question['Question']}")
        
        # Write the question to the file
        writer.writerow({
            "S.No.": i,
            "Question": question["Question"],
            "OptionA": question["Option A"],
            "OptionB": question["Option B"],
            "OptionC": question["Option C"],
            "OptionD": question["Option D"],
            "CorrectOption": question["Correct Option"]
        })

print("Questions appended to the CSV file.")
