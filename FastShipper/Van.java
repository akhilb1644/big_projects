public class Van extends Vehicle {
	public Van() {
		super();
	}

	public Van(short fuelCapacity,byte milesPerGallon,int volume,int price) {
		super(fuelCapacity,milesPerGallon,volume,price);
	}

	@Override
	public void printInfo() {
		System.out.println("Type of Vehicle: Van");
		super.toString();
	}
}