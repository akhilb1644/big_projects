public class LocalOrder extends Order {
	protected Building start;
	protected Building end;

	// Constructors

	public LocalOrder() {
		super();
		this.start = new Building();
		this.end = new Building();
	}

	public LocalOrder(int value,int payment,Building start,Building end) {
		super(value,payment);
		this.start = new Building(start);
		this.end = new Building(end);
	}

	// Getters

	public Building getStart() {
		return new Building(start);
	}

	public Building getEnd() {
		return new Building(end);
	}

	// Setters

	public void setStart(Building start) {
		this.start = new Building(start);
	}

	public void setEnd(Building end) {
		this.end = new Building(end);
	}
}