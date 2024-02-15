public class City {
	protected String name;
	protected Warehouse warehouse;

	// Constructors

	public City() {
		name = "Unknown";
		warehouse = new Warehouse();
	}

	public City(String name) {
		this.name = name;
	}

	// Copy Constructor

	public City(City city) {
		this.name = city.getName();
		this.warehouse = new Warehouse(warehouse);
	}

	// Getters

	public String getName() {
		return name;
	}

	public Warehouse getWarehouse() {
		return new Warehouse(warehouse);
	}

	// Setters

	public void setName(String name) {
		this.name = name;
	}

	public void setWarehouse(Warehouse warehouse) { // Always use this method to set warehouse, there is no other way.
		this.warehouse = new Warehouse(warehouse);
	}
}