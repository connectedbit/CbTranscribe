import hashlib
import pathlib
import argparse
import whisper
import sqlite3
import configparser
import os


def build_transcribe_options(whisper_config):
    options = {}

    language = whisper_config.get("language", fallback="").strip()
    if language:
        options["language"] = language

    options["fp16"] = whisper_config.getboolean("fp16", fallback=False)
    options["verbose"] = whisper_config.getboolean("verbose", fallback=False)

    beam_size = whisper_config.get("beam_size", fallback="").strip()
    if beam_size:
        options["beam_size"] = int(beam_size)

    best_of = whisper_config.get("best_of", fallback="").strip()
    if best_of:
        options["best_of"] = int(best_of)

    initial_prompt = whisper_config.get("initial_prompt", fallback="").strip()
    if initial_prompt:
        options["initial_prompt"] = initial_prompt

    return options


def transcode(file, model_name, transcribe_options):
    model = whisper.load_model(model_name)
    result = model.transcribe(audio=file, **transcribe_options)
    return result["text"]


def init_db(db_file):
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Audio(hash VARCHAR(256), path TEXT, text CLOB)")
    return cur, con


def parse_arguments():
    parser = argparse.ArgumentParser(description="Transcode audio")
    parser.add_argument("audio", type=pathlib.Path)
    return parser.parse_args()


def hash_digest_found(db_parm, hash_digest_parm):
    sql = f"SELECT COUNT(*) FROM Audio WHERE hash = \"{hash_digest_parm}\""
    db_parm.execute(sql)
    return db_parm.fetchone()[0] > 0


def get_file_hash(path_to_file_parm):
    with open(path_to_file_parm, mode="rb") as file:
        data = file.read()
    return hashlib.sha256(data).hexdigest()


def process_folder(path_to_folder):
    for file in os.listdir(path_to_folder):
        if file.endswith(".mp3"):
            process_file(os.path.join(path_to_folder, file))


def process_file(path_to_file):
    hash_digest = get_file_hash(path_to_file)

    if not hash_digest_found(db, hash_digest):
        try:
            print(f"Transcoding file: {path_to_file}")
            text = transcode(path_to_file, model_name, transcribe_options)
            param_tuple = (hash_digest, path_to_file, text)
            db.execute("INSERT INTO Audio (hash, path, text) VALUES (?, ?, ?)", param_tuple)
            conn.commit()
        except Exception as ex:
            print(f"Exception: {ex}")
    else:
        print(f"Already in DB: {path_to_file}")


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("whispercli.ini")
    db, conn = init_db(config["default"]["dbfile"])

    whisper_config = config["whisper"] if config.has_section("whisper") else config["default"]
    model_name = whisper_config.get("model", fallback="base.en").strip() or "base.en"
    transcribe_options = build_transcribe_options(whisper_config)

    args = parse_arguments()

    if os.path.isdir(args.audio.resolve()):
        process_folder(args.audio.resolve())
    else:
        process_file(str(args.audio.resolve()))
