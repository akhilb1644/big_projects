import java.util.ArrayList;

@SuppressWarnings("unchecked")
public class Player {
	private String name;
	private ArrayList<Order> orderList = new ArrayList();
	private ArrayList<Vehicle> vehiclesOwned = new ArrayList<>();

	public Player() {
		name = "Unknown";
	}

	public Player(String name) {
		this.name = name;
	}

	// Copy constructor

	public Player(Player player) {
		this.name = player.getName();
		this.orderList = player.getOrderList();
		this.vehiclesOwned = player.getVehiclesOwned();
	}

	// Getters
	
	public String getName() {
		return name;
	}

	public ArrayList<Order> getOrderList() {
		return (ArrayList<Order>) orderList.clone();
	}

	public ArrayList<Vehicle>getVehiclesOwned() {
		return (ArrayList<Vehicle>) vehiclesOwned.clone();
	}

	// Setters

	public void setName(String name) {
		this.name = name;
	}

	public void setOrderList(ArrayList<Order> orderList) {
		this.orderList = (ArrayList<Order>) orderList.clone();
	}

	public void setVehiclesOwned(ArrayList<Vehicle> vehicleOwned) {
		this.vehiclesOwned = (ArrayList<Vehicle>) vehiclesOwned.clone();
	}
}