package euler.lib;

import java.math.BigInteger;
import java.util.Random;

public class EInteger extends BigInteger {

	private static final Boolean False = null;
	public EInteger(byte[] arg0) {
		super(arg0);
		// TODO Auto-generated constructor stub
	}

	public EInteger(String arg0) {
		super(arg0);
		// TODO Auto-generated constructor stub
	}

	public EInteger(int arg0, byte[] arg1) {
		super(arg0, arg1);
		// TODO Auto-generated constructor stub
	}

	public EInteger(String arg0, int arg1) {
		super(arg0, arg1);
		// TODO Auto-generated constructor stub
	}

	public EInteger(int arg0, Random arg1) {
		super(arg0, arg1);
		// TODO Auto-generated constructor stub
	}

	public EInteger(int arg0, int arg1, Random arg2) {
		super(arg0, arg1, arg2);
		// TODO Auto-generated constructor stub
	}
	public Boolean isPrime(){
		EInteger two=new EInteger("2");
		if (this.compareTo(this.ZERO)<=0){
			return false;
		}
		else if(this.remainder(two) == this.ZERO){
			return false;
		}
		else{
			EInteger Three=new EInteger("3");
			while (Three.pow(2).compareTo(this)<0){
				if(this.remainder(Three)==this.ZERO){
					return false;
				}
				Three=(EInteger) Three.add(two);
				
			}
		}
		return true;
	}
	public Boolean isPalindromic(){		
		StringBuffer a=new StringBuffer(this.toString());		
		if(this.toString().equals(a.reverse().toString())){
			return true;
		}
		else return false;
	}

}
