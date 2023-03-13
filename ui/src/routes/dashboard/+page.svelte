<script lang="ts">
	import { authenticatedAPICall } from '../../api/util';
	let response: any;

	function getAccounts() {
		authenticatedAPICall('GET', 'accounts/').then((data) => (response = JSON.stringify(data)));
	}
</script>

<button on:click={getAccounts}>Click</button>
{response}
