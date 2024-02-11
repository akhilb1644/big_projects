public class Warehouse extends Building {

	// Constructors
	
	public Warehouse() {
		super();
	}

	public Warehouse(String name,short x,short y,City city) {
		super(name,x,y,city);
	}

	// Copy Constructor

	public Warehouse(Warehouse warehouse) {
		super(warehouse);
	}
}