// Mirrors the backend's uniform response/error shapes (docs/api-conventions.md).

export interface Paginated<T> {
  items: T[];
  total: number;
  page: number;
  size: number;
}

export interface ApiError {
  error: {
    code: string;
    message: string;
    details: unknown;
  };
}
