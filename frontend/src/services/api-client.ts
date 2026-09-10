// Single API client for the whole app. ALL backend calls go through this
// instance — auth headers, error handling and retries live here in one place.
import axios from "axios";

export const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? "/api/v1",
  timeout: 15_000,
});

// Attach auth token to every request (implement token storage when auth lands).
apiClient.interceptors.request.use((config) => {
  // const token = getAccessToken();
  // if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Central error handling: map backend's uniform error shape, handle 401 → login.
apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    // if (error.response?.status === 401) redirectToLogin();
    return Promise.reject(error);
  },
);
