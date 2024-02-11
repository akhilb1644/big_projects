public class Building {
	protected String name;
	protected short x;
	protected short y;

	// Constructors

	public Building() {
		name = "Unknown";
		x = 0;
		y = 0;
	}

	public Building(String name,short x,short y) {
		this.name = name;
		this.x = x;
		this.y = y;
	}

	// Copy Constructor

	public Building(Building building) {
		name = building.getName();
		x = building.getX();
		y = building.getY();
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
}