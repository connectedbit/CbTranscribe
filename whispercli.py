import hashlib
import pathlib
import argparse
import whisper
import sqlite3
import configparser
import os


def transcode(file):
    model = whisper.load_model("base.en")
    result = model.transcribe(audio=file, language="english", fp16=False, verbose=False)
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
            text = transcode(path_to_file)
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
    args = parse_arguments()

    if os.path.isdir(args.audio.resolve()):
        process_folder(args.audio.resolve())
    else:
        process_file(str(args.audio.resolve()))
