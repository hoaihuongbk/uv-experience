import time
import subprocess
import matplotlib.pyplot as plt

def run_command(command, iterations=5):
    times = []
    for _ in range(iterations):
        start_time = time.time()
        subprocess.run(command, shell=True, check=True)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def create_chart(pip_small, uv_small, pip_large, uv_large):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.boxplot([pip_small, uv_small], labels=['pip-compile', 'uv'])
    ax1.set_ylabel('Time (seconds)')
    ax1.set_title('Small Dependency Set')

    ax2.boxplot([pip_large, uv_large], labels=['pip-compile', 'uv'])
    ax2.set_ylabel('Time (seconds)')
    ax2.set_title('Large Dependency Set')

    plt.suptitle('Comparison of pip-compile and uv Performance')
    plt.savefig('tool_comparison.png')
    plt.close()

def main():
    print("Comparing pip-compile and uv for dependency resolution")

    pip_small = run_command("pip-compile pyproject.toml --extra small -o requirements-pip-small.txt")
    uv_small = run_command("uv pip compile pyproject.toml --extra small -o requirements-uv-small.txt")

    pip_large = run_command("pip-compile pyproject.toml --extra large -o requirements-pip-large.txt")
    uv_large = run_command("uv pip compile pyproject.toml --extra large -o requirements-uv-large.txt")

    print(f"pip-compile (small) average: {sum(pip_small)/len(pip_small):.2f} seconds")
    print(f"uv (small) average: {sum(uv_small)/len(uv_small):.2f} seconds")
    print(f"pip-compile (large) average: {sum(pip_large)/len(pip_large):.2f} seconds")
    print(f"uv (large) average: {sum(uv_large)/len(uv_large):.2f} seconds")

    create_chart(pip_small, uv_small, pip_large, uv_large)
    print("Chart saved as tool_comparison.png")

if __name__ == "__main__":
    main()
