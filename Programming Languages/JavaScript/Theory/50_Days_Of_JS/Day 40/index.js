const needsLicense = (kind) => {
	// code here

	return ['car', 'truck'].includes(kind);
}

const chooseVehicle = (option1, option2) => {
	// code here

	return `${option1.localeCompare(option2) === 1 ? option2 : option1} is clearly the better choice.`;
}

const calculateResellPrice = (originalPrice, age) => {
	// code here

	let factor = 0;

    if (age > 10)
        factor = 0.5
    else if (age < 3)
        factor = 0.8
    else
        factor = 0.7

    return originalPrice * factor;
}
