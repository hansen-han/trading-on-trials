import sqlite3

DB_PATH = "biotech_data.db"

# --- Utility: Connect to DB ---
def connect_db():
    return sqlite3.connect(DB_PATH)

# --- Step 1: Create Tables ---
with connect_db() as conn:
    cursor = conn.cursor()

    # Company table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT NOT NULL,
            ticker TEXT UNIQUE NOT NULL,
            type TEXT,
            comment TEXT,
            articles_comment TEXT
        )
    ''')

    # Articles table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER NOT NULL,
            url TEXT UNIQUE NOT NULL,
            date TEXT,
            time TEXT,
            raw_html TEXT,
            text TEXT,
            timezone TEXT,
            article_title TEXT,
            FOREIGN KEY (company_id) REFERENCES company (id) ON DELETE CASCADE
        )
    ''')

    # Annotations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS article_annotation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            article_id INTEGER NOT NULL,
            annotation_json TEXT,
            comment TEXT,
            FOREIGN KEY (article_id) REFERENCES articles (id) ON DELETE CASCADE
        )
    ''')

    print("✅ Tables created successfully.")

# --- Step 2: Insert Companies ---

# Helper to insert company list
def insert_companies(companies, company_type=None):
    with connect_db() as conn:
        cursor = conn.cursor()
        for name, ticker in companies:
            cursor.execute('''
                INSERT OR IGNORE INTO company (company_name, ticker, type)
                VALUES (?, ?, ?)
            ''', (name, ticker, company_type))

# First batch
batch_1 = [
    ("AbbVie", "ABBV"),
    ("Alnylam Pharmaceuticals", "ALNY"),
    ("Amgen", "AMGN"),
    ("Diffusion Pharmaceuticals", "DFFN"),
    ("Exscientia plc", "EXAI"),
    ("Faron Pharmaceuticals", "FARN"),
    ("Intellia Therapeutics", "NTLA"),
    ("Plus Therapeutics", "PSTV"),
    ("Vertex Pharmaceuticals", "VRTX"),
    ("Regeneron", "REGN"),
    ("Bristol-Myers Squibb", "BMY"),
    ("AstraZeneca PLC", "AZN"),
    ("Sutro Biopharma", "STRO"),
    ("Cytokinetics", "CYTK"),
    ("Coya Therapeutics", "COYA"),
    ("Arvinas", "ARVN"),
    ("CorMedix", "CRMD"),
    ("Johnson & Johnson", "JNJ"),
    ("Pfizer", "PFE"),
    ("Merck", "MRK"),
    ("Gilead", "GILD"),
    ("Novartis", "NVS"),
    ("Roche", "RHHBY"),
    ("GSK", "GSK"),
    ("Sanofi", "SNY"),
    ("Eli Lilly and Company", "LLY"),
    ("Biogen", "BIIB"),
    ("Moderna", "MRNA"),
    ("Ionis", "IONS"),
    ("CRISPR Therapeutics AG", "CRSP"),
    ("Editas Medicine", "EDIT"),
    ("Beam Therapeutics", "BEAM"),
    ("BioMarin Pharmaceutical", "BMRN"),
    ("Sarepta Therapeutics", "SRPT"),
    ("Incyte", "INCY"),
    ("Blueprint Medicines Corporation", "BPMC"),
    ("BridgeBio Pharma", "BBIO"),
    ("Mirati Therapeutics", "MRTX"),
    ("CervoMed", "CRVO")
]

# Second batch
batch_2 = [
    ("10x Genomics Inc.", "TXG"),
    ("23andMe Holding Co.", "ME"),
    ("2seventy bio Inc.", "TSVT"),
    ("4D Molecular Therapeutics Inc.", "FDMT"),
    ("89bio Inc.", "ETNB"),
    ("Aadi Bioscience Inc.", "AADI"),
    ("AbCellera Biologics Inc.", "ABCL"),
    ("ACADIA Pharmaceuticals Inc.", "ACAD"),
    ("ADMA Biologics Inc.", "ADMA"),
    ("Agios Pharmaceuticals Inc.", "AGIO"),
    ("Akero Therapeutics Inc.", "AKRO"),
    ("Aligos Therapeutics Inc.", "ALGS"),
    ("Allogene Therapeutics Inc.", "ALLO"),
    ("Amicus Therapeutics Inc.", "FOLD"),
    ("AnaptysBio Inc.", "ANAB"),
    ("Apellis Pharmaceuticals Inc.", "APLS"),
    ("Arcellx Inc.", "ACLX"),
    ("Arrowhead Pharmaceuticals Inc.", "ARWR"),
    ("Assembly Biosciences Inc.", "ASMB"),
    ("Atara Biotherapeutics Inc.", "ATRA"),
    ("Avidity Biosciences Inc.", "RNA"),
    ("Biohaven Ltd.", "BHVN"),
    ("BioNTech SE", "BNTX"),
    ("Cabaletta Bio Inc.", "CABA"),
    ("Caribou Biosciences Inc.", "CRBU"),
    ("Catalyst Pharmaceuticals Inc.", "CPRX"),
    ("Celldex Therapeutics Inc.", "CLDX"),
    ("Century Therapeutics Inc.", "IPSC"),
    ("Codiak BioSciences Inc.", "CDAK"),
    ("Cullinan Oncology Inc.", "CGEM"),
    ("CytomX Therapeutics Inc.", "CTMX"),
    ("Day One Biopharmaceuticals Inc.", "DAWN"),
    ("Denali Therapeutics Inc.", "DNLI"),
    ("Dyne Therapeutics Inc.", "DYN"),
    ("Eidos Therapeutics Inc.", "EIDX"),
    ("Eiger BioPharmaceuticals Inc.", "EIGR"),
    ("Eliem Therapeutics Inc.", "ELYM"),
    ("Epizyme Inc.", "EPZM"),
    ("Fate Therapeutics Inc.", "FATE"),
    ("FibroGen Inc.", "FGEN"),
    ("G1 Therapeutics Inc.", "GTHX"),
    ("Galapagos NV", "GLPG"),
    ("Generation Bio Co.", "GBIO"),
    ("Global Blood Therapeutics Inc.", "GBT"),
    ("Graphite Bio Inc.", "GRPH"),
    ("Harpoon Therapeutics Inc.", "HARP"),
    ("Homology Medicines Inc.", "FIXX"),
    ("IGM Biosciences Inc.", "IGMS"),
    ("ImmunoGen Inc.", "IMGN"),
    ("Immunovant Inc.", "IMVT"),
    ("Inovio Pharmaceuticals Inc.", "INO"),
    ("Insmed Inc.", "INSM"),
    ("Invitae Corp.", "NVTA"),
    ("Iovance Biotherapeutics Inc.", "IOVA"),
    ("Ironwood Pharmaceuticals Inc.", "IRWD"),
    ("Jounce Therapeutics Inc.", "JNCE"),
    ("Karuna Therapeutics Inc.", "KRTX"),
    ("Karyopharm Therapeutics Inc.", "KPTI"),
    ("Krystal Biotech Inc.", "KRYS"),
    ("Legend Biotech Corp.", "LEGN"),
    ("MacroGenics Inc.", "MGNX"),
    ("Madrigal Pharmaceuticals Inc.", "MDGL"),
    ("Magenta Therapeutics Inc.", "MGTA"),
    ("Marinus Pharmaceuticals Inc.", "MRNS"),
    ("MeiraGTx Holdings plc", "MGTX"),
    ("Molecular Templates Inc.", "MTEM"),
    ("Natera Inc.", "NTRA"),
    ("Nkarta Inc.", "NKTX"),
    ("Novavax Inc.", "NVAX"),
    ("Nurix Therapeutics Inc.", "NRIX"),
    ("Ocular Therapeutix Inc.", "OCUL"),
    ("Olema Pharmaceuticals Inc.", "OLMA"),
    ("Oncorus Inc.", "ONCR"),
    ("Orchard Therapeutics plc", "ORTX"),
    ("Passage Bio Inc.", "PASG"),
    ("PTC Therapeutics Inc.", "PTCT"),
    ("Recursion Pharmaceuticals Inc.", "RXRX"),
    ("Relay Therapeutics Inc.", "RLAY"),
    ("Replimune Group Inc.", "REPL"),
    ("Revolution Medicines Inc.", "RVMD"),
    ("Rocket Pharmaceuticals Inc.", "RCKT"),
    ("Rubius Therapeutics Inc.", "RUBY"),
    ("Sana Biotechnology Inc.", "SANA"),
    ("Sangamo Therapeutics Inc.", "SGMO"),
    ("Scholar Rock Holding Corp.", "SRRK"),
    ("Seagen Inc.", "SGEN"),
    ("Selecta Biosciences Inc.", "SELB"),
    ("Seres Therapeutics Inc.", "MCRB"),
    ("Shattuck Labs Inc.", "STTK"),
    ("Sigilon Therapeutics Inc.", "SGTX"),
    ("Solid Biosciences Inc.", "SLDB"),
    ("SpringWorks Therapeutics Inc.", "SWTX"),
    ("Stoke Therapeutics Inc.", "STOK"),
    ("Syndax Pharmaceuticals Inc.", "SNDX"),
    ("TCR2 Therapeutics Inc.", "TCRR"),
    ("Terns Pharmaceuticals Inc.", "TERN"),
    ("TG Therapeutics Inc.", "TGTX"),
    ("Tiziana Life Sciences plc", "TLSA"),
    ("Travere Therapeutics Inc.", "TVTX"),
    ("Twist Bioscience Corp.", "TWST"),
    ("Ultragenyx Pharmaceutical Inc.", "RARE"),
    ("United Therapeutics Corp.", "UTHR"),
    ("Vaxart Inc.", "VXRT"),
    ("Veracyte Inc.", "VCYT"),
    ("Vericel Corp.", "VCEL"),
    ("Viking Therapeutics Inc.", "VKTX"),
    ("Vor Biopharma Inc.", "VOR")
]

# Third batch
batch_3 = [
    ("Argenx SE", "ARGX"),
    ("Apellis Pharmaceuticals, Inc.", "APLS"),
    ("ACADIA Pharmaceuticals Inc.", "ACAD"),
    ("Xenon Pharmaceuticals Inc.", "XENE"),
    ("MoonLake Immunotherapeutics", "MLTX"),
    ("ImmunoGen Inc.", "IMGN"),
    ("Immunovant Inc.", "IMVT"),
    ("Iovance Biotherapeutics Inc.", "IOVA"),
    ("Krystal Biotech Inc.", "KRYS"),
    ("Kura Oncology Inc.", "KURA"),
    ("Legend Biotech Corp.", "LEGN"),
    ("Madrigal Pharmaceuticals Inc.", "MDGL"),
    ("Mirum Pharmaceuticals, Inc.", "MIRM"),
    ("Rocket Pharmaceuticals Inc.", "RCKT"),
    ("Sana Biotechnology, Inc.", "SANA"),
    ("Scholar Rock Holding Corporation", "SRRK"),
    ("SpringWorks Therapeutics, Inc.", "SWTX"),
    ("Tarsus Pharmaceuticals, Inc.", "TARS"),
    ("Terns Pharmaceuticals, Inc.", "TERN"),
    ("Travere Therapeutics, Inc.", "TVTX"),
    ("Vericel Corporation", "VCEL"),
    ("Viking Therapeutics, Inc.", "VKTX"),
    ("Vor Biopharma Inc.", "VOR"),
    ("Zymeworks Inc.", "ZYME")
]

# Insert all companies by batch
insert_companies(batch_1)
insert_companies(batch_2, company_type="biotech/pharma")
insert_companies(batch_3, company_type="biotech/pharma")

print("✅ Companies inserted successfully.")
