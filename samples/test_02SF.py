from TensorMol import *

def evaluate_set(mset):
	"""
	Evaluate energy, force, and charge error statistics on an entire set
	using the Symmetry Function Universal network. Prints MAE, MSE, and RMSE.
	"""
	network = UniversalNetwork(name="SF_Universal_master_jeherr_Tue_May_15_10.18.25_2018")
	molset = MSet(mset)
	molset.Load()
	energy_errors, gradient_errors, charge_errors = network.evaluate_set(molset)
	print(energy_errors[:10])
	print(gradient_errors[:10])
	print(charge_errors[:10])
	mae_e = np.mean(np.abs(energy_errors))
	mse_e = np.mean(energy_errors)
	rmse_e = np.sqrt(np.mean(np.square(energy_errors)))
	mae_g = np.mean(np.abs(gradient_errors))
	mse_g = np.mean(gradient_errors)
	rmse_g = np.sqrt(np.mean(np.square(gradient_errors)))
	mae_c = np.mean(np.abs(charge_errors))
	mse_c = np.mean(charge_errors)
	rmse_c = np.sqrt(np.mean(np.square(charge_errors)))
	print("MAE  Energy: ", mae_e, " Gradients: ", mae_g, " Charges: ", mae_c)
	print("MSE  Energy: ", mse_e, " Gradients: ", mse_g, " Charges: ", mse_c)
	print("RMSE  Energy: ", rmse_e, " Gradients: ", rmse_g, " Charges: ", rmse_c)

# evaluate_set("kaggle_opt")

def evaluate_mol(mol):
	"""
	Evaluate single point energy, force, and charge for a molecule using the
	Symmetry Function Universal network.
	"""
	network = UniversalNetwork(name="SF_Universal_master_jeherr_Tue_May_15_10.18.25_2018")
	energy, forces, charges = network.evaluate_mol(mol)
	print("Energy label: ", mol.properties["energy"], " Prediction: ", energy)
	print("Force labels: ", -mol.properties["gradients"], " Prediction: ", forces)
	print("Charge label: ", mol.properties["charges"], " Prediction: ", charges)

a=MSet("kaggle_opt")
a.Load()
mol=a.mols[0]
evaluate_mol(mol)