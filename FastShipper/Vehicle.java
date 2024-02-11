abstract class Vehicle {
	protected short fuelCapacity;
	protected byte milesPerGallon;
	protected int volume;
	protected int price;

	// Constructors

	public Vehicle() {
		fuelCapacity = 0;
		milesPerGallon = 0;
		volume = 0;
		price = 0;
	}

	public Vehicle(short fuelCapacity,byte milesPerGallon,int volume,int price) {
		this.fuelCapacity = fuelCapacity;
		this.milesPerGallon = milesPerGallon;
		this.volume = volume;
		this.price = price;
	}

	// Getters

	public short getFuelCapacity() {
		return fuelCapacity;
	}

	public byte getMilesPerGallon() {
		return milesPerGallon;
	}

	public int getVolume() {
		return volume;
	}

	public int getPrice() {
		return price;
	}

	// Setters

	public void setFuelCapacity(short fuelCapacity) {
		this.fuelCapacity = fuelCapacity;
	}

	public void setMilesPerGallon(byte milesPerGallon) {
		this.milesPerGallon = milesPerGallon;
	}

	public void setVolume(int volume) {
		this.volume = volume;
	}

	public void setPrice(int price) {
		this.price = price;
	}

	// Other Methods
	
	public void printInfo() {
		System.out.println("   Fuel Capacity: " + fuelCapacity);
		System.out.println("   Miles Per Gallon: " + milesPerGallon);
		System.out.println("   Volume: " + volume); 
		System.out.println("   Price: " + price);
	}
}