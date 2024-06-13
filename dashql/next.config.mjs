// next.config.mjs
export default {
    async redirects() {
      return [
        {
          source: '/about',
          destination: '/',
          permanent: true,
        },
        // Add more redirect rules as needed
      ];
    },
  };
  