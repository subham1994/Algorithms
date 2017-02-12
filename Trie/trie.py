class TrieNode:
	def __init__(self):
		self.value = None
		self.children = {}

	def __repr__(self):
		return '<TrieNode: {children}>'.format(children=list(self.children.keys()))


class Trie:
	def __init__(self):
		self._root = TrieNode()

	def _get(self, root, key, pos=0):
		if not root:
			return None
		if pos == len(key):
			return root
		return self._get(root.children.get(key[pos]), key, pos + 1)

	def get(self, key, default=None):
		node = self._get(self._root, key)
		return node.value if node and node.value else default

	def _longest_prefix_of(self, root, key, pos=0, valid_len=0):
		if not root:
			return pos
		if root.value:
			pos = valid_len
		if valid_len == len(key):
			return pos
		return self._longest_prefix_of(root.children.get(key[valid_len]), key, pos, valid_len+1)

	def longest_prefix_of(self, key):
		length = self._longest_prefix_of(self._root, key)
		return key[:length]

	def _keys_with_prefix(self, root, keys, prefix=''):
		if not root:
			return
		if root.value:
			keys.append(prefix)
		for child in root.children:
			self._keys_with_prefix(root.children[child], keys, prefix + child)

	def keys_with_prefix(self, prefix):
		keys = []
		node = self._get(self._root, prefix)
		self._keys_with_prefix(node, keys, prefix=prefix)
		return keys

	def keys(self):
		return self.keys_with_prefix("")

	def _put(self, root, key, value, pos=0):
		if not root:
			root = TrieNode()
		if pos == len(key):
			root.value = value
			return root
		root.children[key[pos]] = self._put(root.children.get(key[pos]), key, value, pos+1)
		return root

	def put(self, key, value):
		self._root = self._put(self._root, key, value)

	def _wildcard_match(self, root, pattern, matches, word='', pos=0):
		if not root:
			return
		if root.value and pos == len(pattern):
			matches.append(word)
		if pos == len(pattern):
			return
		for child in root.children:
			if child == pattern[pos] or pattern[pos] == '.':
				self._wildcard_match(root.children[child], pattern, matches, word + child, pos+1)

	def wildcard_match(self, pattern):
		matches = []
		self._wildcard_match(self._root, pattern, matches)
		return matches


def main():
	trie = Trie()

	trie.put('sea', 4)
	trie.put('Fan', 6)
	trie.put('ant', 14)
	trie.put('shell', 15)
	trie.put('shells', 156)
	trie.put('theater', 41)

	assert trie.get('shell') == 15
	assert trie.get('theater') == 41
	assert trie.get('tea', 0) == 0
	assert not trie.get('tea')

	assert trie.keys_with_prefix('sh') == ['shell', 'shells']
	assert trie.longest_prefix_of('tea') == ''
	assert trie.longest_prefix_of('shells') == 'shells'
	assert trie.wildcard_match('s..') == ['sea']
	assert len(trie.keys()) == 6

	print('All Test cases passed !')


if __name__ == '__main__':
    main()
