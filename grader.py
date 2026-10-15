import numpy as np
from qiskit.quantum_info import Statevector

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

def grade_lab2_bell_state(circuit):
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

def grade_lab3_ghz_state(circuit):
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
