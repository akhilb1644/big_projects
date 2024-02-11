public class Order {
	protected int value;
	protected int payment;

	// Constructors
	
	public Order() {
		value = 0;
		payment = 0;
	}

	public Order(int value,int payment) {
		this.value = value;
		this.payment = payment;
	}

	// Getters
	
	public int getValue() {
		return value;
	}

	public int getPayment() {
		return payment;
	}

	// Setters

	public void setValue(int value) {
		this.value = value;
	}

	public void setPayment(int payment) {
		this.payment = payment;
	}
}