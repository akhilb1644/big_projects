public class Building {
	protected String name;
	protected short x;
	protected short y;
	protected City city;

	// Constructors

	public Building() {
		name = "Unknown";
		x = 0;
		y = 0;
		city = new City();
	}

	public Building(String name,short x,short y,City city) {
		this.name = name;
		this.x = x;
		this.y = y;
		this.city = new City(city);
	}

	// Copy Constructor

	public Building(Building building) {
		name = building.getName();
		x = building.getX();
		y = building.getY();
		city = building.getCity();
	}

	// Getters

	public String getName() {
		return name;
	}

	public short getX() {
		return x;
	}

	public short getY() {
		return y;
	}

	public City getCity() {
		return city;
	}

	// Setters 

	public void setName(String name) {
		this.name = name;
	}

	public void setX(short x) {
		this.x = x;
	}

	public void setY(short y) {
		this.y = y;
	}

	public void setCity(City city) {
		this.city = new City(city);
	} 
}