public class Plane extends Vehicle {
	public Plane() {
		super();
	}

	public Plane(short fuelCapacity,byte milesPerGallon,int volume,int price) {
		super(fuelCapacity,milesPerGallon,volume,price);
	}

	@Override
	public void printInfo() {
		System.out.println("Type of Vehicle: Plane");
		super.toString();
	}
}