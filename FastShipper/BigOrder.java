public class BigOrder extends Order {
	protected Warehouse start;
	protected Warehouse end;

	// Constructors

	public BigOrder() {
		super();
		this.start = new Warehouse();
		this.end = new Warehouse();
	}

	public BigOrder(int value,int payment,City start,City end) {
		super(value,payment);
		this.start = start.getWarehouse();
		this.end = end.getWarehouse();
	}

	// Getters

	public Warehouse getStart() {
		return new Warehouse(start);
	}

	public Warehouse getEnd() {
		return new Warehouse(end);
	}

	// Setters

	public void setStart(City start) {
		this.start = start.getWarehouse();
	}

	public void setEnd(City end) {
		this.end = end.getWarehouse();
	}
}