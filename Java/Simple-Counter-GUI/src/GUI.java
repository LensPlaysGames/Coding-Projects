import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.*;

import javax.swing.*;

public class GUI implements ActionListener {
	
	private String title = "Java GUI - Lens";
	
	private JPanel panel;
	private JLabel labelOne;
	private int count = 0;
	
	private void initui() {
		labelOne = new JLabel("Count: 0");
		panel.add(labelOne);
		
		JButton btnOne = new JButton("Click to Increment Count");
		panel.add(btnOne);
		btnOne.addActionListener(this);
	}
	
	public GUI() {
		JFrame frame = new JFrame();
		
		panel = new JPanel();
		panel.setBorder(BorderFactory.createEmptyBorder(15, 30, 10, 90));
		panel.setLayout(new GridLayout(0, 1));
		
		initui();
		
		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle(title);
		frame.pack();
		frame.setVisible(true);
		
	}
	
	public static void main(String[] args) {
		new GUI();
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		count++;
		labelOne.setText("Count: " + count);
	}
}
