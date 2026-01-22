package structures;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class SimpleList<T extends Comparable<T>> implements SimpleSequence<T>, Iterable<T> {

    private class SimpleNode {
        T data;
        private SimpleNode prev, next;

        SimpleNode(T data) {
            this.data = data;
        }
    }

    private SimpleNode head;
    private SimpleNode tail;
    private int size;
    private int mods = 0;


    private SimpleNode get(int pos) {
        if (pos < 0 || pos >= size)
            throw new IndexOutOfBoundsException();

        SimpleNode cur;

        if (pos < size / 2) {
            cur = head;
            for (int i = 0; i < pos; i++)
                cur = cur.next;
        } else {
            cur = tail;
            for (int i = size - 1; i > pos; i--)
                cur = cur.prev;
        }

        return cur;
    }

    @Override
    public void insert(T el, int pos) {
        if (el == null)
            throw new NullPointerException();
        if (pos < 0 || pos > size)
            throw new IndexOutOfBoundsException();

        SimpleNode node = new SimpleNode(el);

        if (size == 0) {
            head = tail = node;
        } else if (pos == 0) {
            node.next = head;
            head.prev = node;
            head = node;
        } else if (pos == size) {
            tail.next = node;
            node.prev = tail;
            tail = node;
        } else {
            SimpleNode cur = get(pos);
            node.prev = cur.prev;
            node.next = cur;
            cur.prev.next = node;
            cur.prev = node;
        }

        size++; mods++;
    }

    @Override
    public void remove(T el) {
        if (el == null)
            throw new NullPointerException();

        SimpleNode cur = head;

        for (int i = 0; i < size; i++) {
            if (cur.data.equals(el)) {
                remove(i);
                return;
            }
            cur = cur.next;
        }

        throw new NoSuchElementException();
    }

    @Override
    public void remove(int pos) {
        if (pos < 0 || pos >= size)
            throw new IndexOutOfBoundsException();

        SimpleNode cur = get(pos);
        
        if (cur.prev != null)
            cur.prev.next = cur.next;
        else
            head = cur.next;

        if (cur.next != null)
            cur.next.prev = cur.prev;
        else
            tail = cur.prev;

        size--; mods++;
    }

    @Override
    public T min() {
        if (size == 0)
            throw new NoSuchElementException();

        T res = head.data;

        for (T cur : this)
            if (cur.compareTo(res) < 0)
                res = cur;

        return res;
    }

    @Override
    public T max() {
        if (size == 0)
            throw new NoSuchElementException();

        T res = head.data;

        for (T cur : this)
            if (cur.compareTo(res) > 0)
                res = cur;

        return res;
    }

    @Override
    public boolean search(T el) {
        return index(el) != -1;
    }

    @Override
    public T at(int pos) {
        return get(pos).data;
    }
    
    @Override
    public int index(T el) {
        if (el == null)
            throw new NullPointerException();

        SimpleNode cur = head;

        for (int i = 0; i < size; i++) {
            if (cur.data.equals(el))
                return i;
            cur = cur.next;
        }

        return -1;
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean empty() {
        return size == 0;
    }

    @Override
    public String toString() {
        var res = new StringBuilder("[");

        for (T el : this)
            res.append(el).append(", ");

        if (res.length() > 1)
            res.setLength(res.length() - 2);

        res.append("]");
        return res.toString();
    }

    @Override
    public Iterator<T> iterator() {
        return new SimpleListIterator();
    }

    private class SimpleListIterator implements Iterator<T> {
        private SimpleNode cur = head;
        private final int expectedModCount = mods;


        private void check() {
            if (expectedModCount != mods)
                throw new IllegalStateException("Collection modified during iteration");
        }

        @Override
        public boolean hasNext() {
            check(); return cur != null;
        }

        @Override
        public T next() {
            check();

            if (cur == null)
                throw new NoSuchElementException();

            T data = cur.data;
            cur = cur.next;

            return data;
        }
    }
}
