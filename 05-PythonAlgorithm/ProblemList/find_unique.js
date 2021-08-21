// Time  : 2021/05/28 15:27:57
// Theme :
// Description : `Create a function that determines whether all characters in a string are unique or not. Make it case-sensitive, meaning a string with both 'a' and 'A' could pass the test.`

/*
isUnique('abcdef'); // -> true
isUnique('89%df#$^a&x'); // -> true
isUnique('abcAdef'); // -> true
isUnique('abcaef'); // -> false
*/

// O(n^2)
function isUnique(str) {
	for (var i = 0; i < str.length; i++) {
		if (str.lastIndexOf(str[i]) !== i) {
			return false;
		}
	}
	return true;
}

// sort and compare
// O(n * log(n))
function isUnique(str) {
	const chars = str.split("").sort();

	for (let i = 1; i < chars.length; i++) {
		if (chars[i] === chars[i - 1]) {
			return false;
		}
	}

	return true;
}

// O(n)
function isUnique(str) {
	const chars = {};
	for (let i = 0; i < str.length; i++) {
		const thisChar = str[i];

		if (chars[thisChar]) {
			return false;
		}
		chars[thisChar] = true;
	}
	return true;
}

// USE Set
// o(n)
function isUnique(str) {
	const chars = new Set();

	for (let i = 0; i < str.length; i++) {
		const thisChar = str[i];

		if (chars.has(thisChar)) {
			return false;
		}

		chars.add(thisChar);
	}
	return true;
}

// beautiful
function isUnique(str) {
	return new Set(str).size === str.length;
}

// console.log(isUnique("abcdef"));
console.assert(isUnique("abcdefa") === true, "abcdefa----false");
console.assert(isUnique("iassde") === true, "iassde-----false");
console.assert(isUnique("abcdefa") === true, "abcdefa-----false");
console.assert(isUnique("dasqwert") === true, "dasqwert-----false");
