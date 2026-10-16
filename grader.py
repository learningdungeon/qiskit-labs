import numpy as np
from qiskit.quantum_info import Statevector


def grade_lab0_setup(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 1:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 1 qubit."}
        return {"score": 10, "max": 10, "msg": "✅ Setup is working! You are ready for the labs."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}


def grade_lab1_single_qubit(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 1:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 1 qubit."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! |+> state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not the |+> state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}


def grade_lab2_multiqubit_cnot(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 2:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 2 qubits."}
        ops = circuit.count_ops()
        if 'h' not in ops:
            return {"score": 3, "max": 10, "msg": "⚠️ Hadamard gate is missing."}
        if 'cx' not in ops and 'cnot' not in ops:
            return {"score": 3, "max": 10, "msg": "⚠️ CNOT gate is missing."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! CNOT applied correctly."}
        return {"score": 6, "max": 10, "msg": "⚠️ Gates present but order/target wrong."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}


def grade_lab3_bell_state(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 2:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 2 qubits."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! Bell state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not a Bell state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}


def grade_lab4_ghz_state(circuit):
    try:
        circuit = circuit.remove_final_measurements(inplace=False)
        if circuit.num_qubits != 3:
            return {"score": 0, "max": 10, "msg": "❌ Need exactly 3 qubits."}
        sv = Statevector.from_instruction(circuit)
        expected = Statevector([1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 1/np.sqrt(2)])
        if np.abs(sv.inner(expected))**2 > 0.99:
            return {"score": 10, "max": 10, "msg": "✅ Perfect! GHZ state created."}
        return {"score": 5, "max": 10, "msg": "⚠️ Not a GHZ state."}
    except Exception as e:
        return {"score": 0, "max": 10, "msg": f"❌ Error: {e}"}
