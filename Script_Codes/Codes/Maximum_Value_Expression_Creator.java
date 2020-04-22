import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
   Scanner sc= new Scanner(System.in);    //System.in is a standard input stream   
String ra;
    ra=sc.nextLine();
        parenthesisOuter(ra);

}

private static void parenthesisOuter(String expression) {
    Object[] results = parenthesis(expression);
    System.out.println(results[MAXEXPR]);
}

private static Map<String, Object[]> resultMap = new HashMap<>();

private static final int MINVAL = 0;
private static final int MAXVAL = 1;
private static final int MINEXPR = 2;
private static final int MAXEXPR = 3;

public static Object[] parenthesis(String expression) {
    Object[] result = resultMap.get(expression);
    if (result != null) {
        return result;
    }

    try {
        Long parsedLong = new Long(expression);
        return new Object[] { parsedLong, parsedLong, expression, expression };
    } catch (NumberFormatException e) {
        // go on, it's not a number
    }

    result = new Object[] { Long.MAX_VALUE, Long.MIN_VALUE, null, null };
    for (int i = 1; i < expression.length() - 1; i++) {
        if (Character.isDigit(expression.charAt(i)))
            continue;
        Object[] left = parenthesis(expression.substring(0, i));
        Object[] right = parenthesis(expression.substring(i + 1, expression.length()));
        doOp(result, (Long) left[MINVAL], expression.charAt(i), (Long) right[MINVAL],
                (String) left[MINEXPR], (String) right[MINEXPR]);
        doOp(result, (Long) left[MINVAL], expression.charAt(i), (Long) right[MAXVAL],
                (String) left[MINEXPR], (String) right[MAXEXPR]);
        doOp(result, (Long) left[MAXVAL], expression.charAt(i), (Long) right[MINVAL],
                (String) left[MAXEXPR], (String) right[MINEXPR]);
        doOp(result, (Long) left[MAXVAL], expression.charAt(i), (Long) right[MAXVAL],
                (String) left[MAXEXPR], (String) right[MAXEXPR]);
    }

    resultMap.put(expression, result);
    return result;
}

private static void doOp(Object[] result, Long left, char op, Long right, String leftExpression,
        String rightExpression) {
    switch (op) {
    case '+':
        setResult(result, left, op, right, left + right, leftExpression, rightExpression);
        break;
    case '-':
        setResult(result, left, op, right, left - right, leftExpression, rightExpression);
        break;
    case '*':
        setResult(result, left, op, right, left * right, leftExpression, rightExpression);
        break;
    case '/':
        if (right != 0) {
            setResult(result, left, op, right, left / right, leftExpression, rightExpression);
        }
        break;
    }
}

private static void setResult(Object[] result, Long left, char op, Long right, Long leftOpRight,
        String leftExpression, String rightExpression) {
    if (result[MINEXPR] == null || leftOpRight < (Long) result[MINVAL]) {
        result[MINVAL] = leftOpRight;
        result[MINEXPR] = "(" + leftExpression + op + rightExpression + ")";
    }
    if (result[MAXEXPR] == null || leftOpRight > (Long) result[MAXVAL]) {
        result[MAXVAL] = leftOpRight;
        result[MAXEXPR] = "(" + leftExpression + op + rightExpression + ")";
    }
}
}
