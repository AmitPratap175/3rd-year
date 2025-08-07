# -*- coding: utf-8 -*-
"""
This script solves the time-independent Schrödinger equation for a 1D quantum well
using the Numerov method and a shooting algorithm to find the ground state energy
and wavefunction.

The potential is assumed to be zero inside the well (from x=0 to x=1) and
infinite elsewhere. The script compares the numerical solution with the known
analytical solution for the ground state.
"""
import numpy as np
import matplotlib.pyplot as plt


def numerov_solver(x, h, psi, k, E):
    """
    Solves the Schrödinger equation using the Numerov method.

    This function integrates the equation d²ψ/dx² = -2Eψ, which is a simplified
    form of the Schrödinger equation for a constant potential.

    Args:
        x (np.ndarray): Array of x-coordinates.
        h (float): Step size.
        psi (np.ndarray): Array to store the wavefunction values.
        k (float): A parameter to set the initial slope (ψ[1]).
        E (float): Energy eigenvalue guess.

    Returns:
        np.ndarray: The calculated wavefunction.
    """
    # Set initial conditions
    psi[0] = 1.0
    psi[1] = 1 + k

    # The g(x) term in the Numerov method: g(x) = -2 * E
    g = -2 * E

    # Use a simplified Numerov method implementation
    phi0 = psi[0] * (1 - (g * h**2) / 12.0)
    phi1 = psi[1] * (1 - (g * h**2) / 12.0)

    for i in range(2, len(x)):
        phi2 = 2 * phi1 - phi0 + h**2 * g * psi[i - 1]
        phi0 = phi1
        phi1 = phi2
        psi[i] = phi1 / (1 - (g * h**2) / 12.0)

    return psi


def find_eigenstate(n, eps, k, E):
    """
    Finds the ground state energy and wavefunction using a shooting method.

    This function uses a bisection-like method (the shooting method) to find the
    energy `E` for which the wavefunction satisfies the boundary condition at the
    end of the interval. It also fine-tunes the initial slope `k`.

    Args:
        n (int): Number of grid points.
        eps (float): Tolerance for the boundary condition.
        k (float): Initial guess for the slope parameter.
        E (float): Initial guess for the energy.
    """
    x, h = np.linspace(0, 1, n, retstep=True)
    psi = np.zeros_like(x)

    # --- Shooting method to find the correct energy E ---
    # We are looking for a solution where psi[-1] is close to a target value (here, 2.0).
    psi = numerov_solver(x, h, psi.copy(), k, E)
    P1 = psi[-1]

    E1 = E + 0.2
    psi = numerov_solver(x, h, psi.copy(), k, E1)
    P2 = psi[-1]

    # Bisection method to find the energy that satisfies the boundary condition
    while abs(P2 - 2.0) > eps:
        if (P1 - 2.0) * (P2 - 2.0) < 0:
            E2 = 0.5 * (E + E1)
            psi = numerov_solver(x, h, psi.copy(), k, E2)
            P3 = psi[-1]

            if (P1 - 2.0) * (P3 - 2.0) < 0:
                E1 = E2
                P2 = P3
            else:
                E = E2
                P1 = P3
        else:
            # If we are not bracketing the root, move the energy range
            E1 += 0.2
            psi = numerov_solver(x, h, psi.copy(), k, E1)
            P2 = psi[-1]

    # --- Fine-tune the initial slope k ---
    # This ensures the wavefunction meets the boundary condition more precisely.
    while (psi[-1] - 2) > 0 and abs(psi[-1] - 2) > eps:
        k -= 1e-6
        psi = numerov_solver(x, h, psi.copy(), k, E)

    while (psi[-1] - 2) < 0 and abs(psi[-1] - 2) > eps:
        k += 1e-6
        psi = numerov_solver(x, h, psi.copy(), k, E)

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    plt.plot(x, psi - 1, label="Calculated Wavefunction")
    plt.plot(
        x,
        (2 * np.sin(np.pi * x * 0.5) + np.cos(np.pi * x * 0.5) - 1),
        "--",
        label="Theoretical Wavefunction",
    )
    plt.xlabel("x")
    plt.ylabel("ψ(x)")
    plt.title("Ground State Wavefunction of a 1D Quantum Well")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"Found Energy (E): {E:.4f}")


def main():
    """
    Main function to get user input and run the simulation.
    """
    try:
        n = int(input("Enter the number of divisions (e.g., 100): "))
        eps = float(input("Enter the tolerance (e.g., 1e-6): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return

    # Initial conditions
    h = 1 / (n - 1)
    k = 3.14 * h  # Initial slope guess
    initial_energy = 1.0  # Initial energy guess

    find_eigenstate(n, eps, k, initial_energy)


if __name__ == "__main__":
    main()
