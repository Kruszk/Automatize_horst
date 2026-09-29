import subprocess
from pathlib import Path

# PODAJ ŚCIEŻKĘ DO SWOJEGO PLIKU thisroot.sh
ROOT_INIT_PATH = "/home/kacper-ruszkowski/root/bin/thisroot.sh" 

def run_horst_batch(
    input_dir: str = "Horst_input",
    output_dir: str = "Horst_output",
    model_path: str = "/home/kacper-ruszkowski/HIGS/Higs2026/response_simulations_zerodegree/12mm_20mm.root",
    l_param: int = 5000,
    r_param: int = 7000,
    file_extension: str = "*.txt"
):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    input_files = list(input_path.glob(file_extension))

    for input_file in input_files:
        output_file = output_path / f"{input_file.stem}_output.root"

        # Łączymy ładowanie środowiska ROOT i komendę horst w jeden ciąg tekstowy
        command_str = (
            f"source {ROOT_INIT_PATH} && "
            f"horst {input_file} -m {model_path} -l {l_param} -r {r_param} -o {output_file}"
        )

        print(f"Uruchamianie dla: {input_file.name}")
        
        try:
            # shell=True oraz executable="/bin/bash" pozwalają na użycie komendy 'source'
            result = subprocess.run(
                command_str, 
                shell=True, 
                executable="/bin/bash",
                check=True, 
                capture_output=True, 
                text=True
            )
            print(f"Sukces: Zapisano do {output_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"Błąd podczas przetwarzania {input_file.name}:")
            print(e.stderr)

if __name__ == "__main__":
    run_horst_batch()