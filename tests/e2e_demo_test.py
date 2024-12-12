import subprocess
from pathlib import Path
from tempfile import TemporaryDirectory


def test_e2e():
    with TemporaryDirectory() as temp_dir:

        root = Path(temp_dir)

        raw_input_dir = root / "raw_input_dir"
        pre_MEDS_dir = root / "pre_MEDS_dir"
        MEDS_cohort_dir = root / "MEDS_cohort_dir"

        do_overwrite = True
        do_demo = True
        do_download = True

        command_parts = [
            "MEDS_extract-MIMIC_IV",
            f"raw_input_dir={str(raw_input_dir.resolve())}",
            f"pre_MEDS_dir={str(pre_MEDS_dir.resolve())}",
            f"MEDS_cohort_dir={str(MEDS_cohort_dir.resolve())}",
            f"do_download={do_download}",
            f"do_overwrite={do_overwrite}",
            f"do_demo={do_demo}",
        ]

        full_cmd = " ".join(command_parts)
        command_out = subprocess.run(full_cmd, shell=True, capture_output=True)

        stderr = command_out.stderr.decode()
        stdout = command_out.stdout.decode()

        if command_out.returncode != 0:
            print(f"Command failed with return code {command_out.returncode}.")
            print(f"Command stdout:\n{stdout}")
            print(f"Command stderr:\n{stderr}")
            raise ValueError(f"Command failed with return code {command_out.returncode}.")